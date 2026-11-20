import json
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

class QuestionToSQLSystem:
    def __init__(self, model_name="llama3.2"):
        self.llm = ChatOllama(model=model_name, temperature=0)
        
        self.database_schemas = {
            "sales_db": {
                "description": "Sales and customer transaction database",
                "tables": {
                    "customers": {
                        "columns": ["customer_id", "name", "email", "region", "signup_date"],
                        "description": "Customer information"
                    },
                    "orders": {
                        "columns": ["order_id", "customer_id", "order_date", "total_amount", "status"],
                        "description": "Order transactions"
                    },
                    "products": {
                        "columns": ["product_id", "name", "category", "price", "stock"],
                        "description": "Product catalog"
                    },
                    "order_items": {
                        "columns": ["order_item_id", "order_id", "product_id", "quantity", "price"],
                        "description": "Individual items in orders"
                    }
                }
            },
            "hr_db": {
                "description": "Human resources and employee database",
                "tables": {
                    "employees": {
                        "columns": ["employee_id", "name", "department", "position", "salary", "hire_date"],
                        "description": "Employee information"
                    },
                    "departments": {
                        "columns": ["department_id", "name", "manager_id", "budget"],
                        "description": "Department details"
                    },
                    "attendance": {
                        "columns": ["attendance_id", "employee_id", "date", "status", "hours_worked"],
                        "description": "Employee attendance records"
                    }
                }
            },
            "inventory_db": {
                "description": "Warehouse and inventory management database",
                "tables": {
                    "warehouses": {
                        "columns": ["warehouse_id", "location", "capacity", "manager"],
                        "description": "Warehouse locations"
                    },
                    "inventory": {
                        "columns": ["inventory_id", "warehouse_id", "product_id", "quantity", "last_updated"],
                        "description": "Current inventory levels"
                    },
                    "shipments": {
                        "columns": ["shipment_id", "warehouse_id", "destination", "ship_date", "status"],
                        "description": "Outgoing shipments"
                    }
                }
            }
        }
    
    def stage1_refine_question(self, generic_question):
        
        db_context = "\n".join([
            f"- {db_name}: {info['description']}"
            for db_name, info in self.database_schemas.items()
        ])
        
        prompt = f"""Hey, I need your help understanding what someone is really asking for.

I have these three databases:
{db_context}

Someone just asked: "{generic_question}"

Can you figure out which database they need and make their question more specific? Like, if they say "top customers", they probably mean top 10 by spending this year, right?

Return a single JSON object (not an array) with:
- refined_question: the clearer version
- database: which one to use
- reasoning: why you picked that

Just the JSON object please, nothing else."""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        response_text = response.content.strip()
        
        try:
            if "```json" in response_text:
                start = response_text.index("```json") + 7
                end = response_text.index("```", start)
                json_str = response_text[start:end].strip()
            elif "```" in response_text:
                start = response_text.index("```") + 3
                end = response_text.index("```", start)
                json_str = response_text[start:end].strip()
            elif "{" in response_text and "}" in response_text:
                start = response_text.index("{")
                end = response_text.rindex("}") + 1
                json_str = response_text[start:end]
            else:
                print(f"Couldn't find JSON in response: {response_text}")
                return None
            
            result = json.loads(json_str)
            
            if isinstance(result, list) and len(result) > 0:
                result = result[0]
            
            return result
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Response text: {response_text}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            print(f"Response text: {response_text}")
            return None
    
    def stage2_generate_sql(self, refined_question, database_name):
        
        if database_name not in self.database_schemas:
            return {"error": f"Database {database_name} not found"}
        
        schema = self.database_schemas[database_name]
        
        schema_description = f"Database: {database_name}\n{schema['description']}\n\nTables:\n"
        for table_name, table_info in schema['tables'].items():
            columns = ", ".join(table_info['columns'])
            schema_description += f"\n{table_name} ({columns})\n"
        
        prompt = f"""Alright, I need you to write a SQL query for me.

Here's what I'm working with:
{schema_description}

The question is: {refined_question}

Write me a query that answers this. Make sure to:
- Join tables properly if you need multiple ones
- Add filters where it makes sense
- Use SUM, COUNT, AVG if you're aggregating stuff
- Order results and maybe limit them

Return valid JSON with:
- sql_query: the actual query (as a single string with spaces instead of newlines)
- explanation: what it does
- tables_used: array of table names you're using

Make sure the SQL query is on ONE line in the JSON. JSON only please."""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        response_text = response.content.strip()
        
        try:
            if "```json" in response_text:
                start = response_text.index("```json") + 7
                end = response_text.index("```", start)
                json_str = response_text[start:end].strip()
            elif "```" in response_text:
                start = response_text.index("```") + 3
                end = response_text.index("```", start)
                json_str = response_text[start:end].strip()
            elif "{" in response_text and "}" in response_text:
                start = response_text.index("{")
                end = response_text.rindex("}") + 1
                json_str = response_text[start:end]
            else:
                print(f"Couldn't find JSON in response: {response_text}")
                return None
            
            json_str = json_str.replace('\n"', ' ').replace('"\n', ' ').replace('\\n', ' ')
            
            result = json.loads(json_str)
            return result
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Trying to fix malformed JSON...")
            try:
                import re
                sql_match = re.search(r'"sql_query"\s*:\s*"([^"]+(?:\n[^"]+)*)"', response_text)
                exp_match = re.search(r'"explanation"\s*:\s*"([^"]+)"', response_text)
                tables_match = re.search(r'"tables_used"\s*:\s*\[([^\]]+)\]', response_text)
                
                if sql_match and exp_match and tables_match:
                    sql = sql_match.group(1).replace('\n', ' ').replace('"', '').strip()
                    exp = exp_match.group(1)
                    tables_str = tables_match.group(1)
                    tables = [t.strip().strip('"') for t in tables_str.split(',')]
                    
                    return {
                        "sql_query": sql,
                        "explanation": exp,
                        "tables_used": tables
                    }
            except Exception as e2:
                print(f"Couldn't fix JSON: {e2}")
            
            print(f"Response text: {response_text}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            print(f"Response text: {response_text}")
            return None
    
    def process_question(self, generic_question):
        
        
        print(f"GENERIC QUESTION: {generic_question}")
        
        
        print("STAGE 1: Refining question...")
        stage1_result = self.stage1_refine_question(generic_question)
        
        if not stage1_result:
            print("Failed to refine question")
            return None
        
        print(f"\nRefined Question: {stage1_result['refined_question']}")
        print(f"Target Database: {stage1_result['database']}")
        print(f"Reasoning: {stage1_result['reasoning']}")
        
        
        print("STAGE 2: Generating SQL query...")
        stage2_result = self.stage2_generate_sql(
            stage1_result['refined_question'],
            stage1_result['database']
        )
        
        if not stage2_result:
            print("Failed to generate SQL")
            return None
        
        print(f"\nSQL Query:\n{stage2_result['sql_query']}")
        print(f"\nExplanation: {stage2_result['explanation']}")
        print(f"Tables Used: {', '.join(stage2_result['tables_used'])}")
        
        full_result = {
            "generic_question": generic_question,
            "stage1_output": stage1_result,
            "stage2_output": stage2_result
        }
        
        return full_result

def main():
    system = QuestionToSQLSystem()
    
    test_questions = [
        "Show me the top customers",
        "What's the employee count?",
        "How's our inventory looking?",
        "Who are the best performers?",
        "What's the revenue trend?",
        "Which products are low in stock?",
        "Show me recent hires",
        "What are the biggest orders?"
    ]
    
    results = []
    
    
    print("\n QUESTION TO SQL SYSTEM - DEMO")
    
    
    for question in test_questions[:3]:
        result = system.process_question(question)
        if result:
            results.append(result)
    
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to results.json")
    
    
    print("INTERACTIVE MODE")
    print("Enter your generic questions (or 'quit' to exit)\n")
    
    while True:
        user_question = input("Your question: ").strip()
        
        if user_question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_question:
            continue
        
        system.process_question(user_question)

if __name__ == "__main__":
    main()
