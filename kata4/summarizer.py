import json
import os
from datetime import datetime
from typing import Dict, List
import requests
from bs4 import BeautifulSoup
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

class NewsSummarizer:
    def __init__(self, model_name="llama3.2"):
        self.llm = OllamaLLM(model=model_name)
        self.summaries_file = "summaries.json"
        self.summaries = self._load_summaries()
    
    def _load_summaries(self) -> List[Dict]:
        if os.path.exists(self.summaries_file):
            with open(self.summaries_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_summaries(self):
        with open(self.summaries_file, 'w') as f:
            json.dump(self.summaries, f, indent=2)
    
    def extract_article_content(self, url: str) -> str:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
            tag.decompose()
        
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
        
        return content[:5000]
    
    def classify_article_type(self, content: str) -> str:
        prompt = PromptTemplate(
            input_variables=["content"],
            template="""Classify this article into ONE category: technology, financial, sports, entertainment, politics, health, or general.
            
Article: {content}

Category (one word only):"""
        )
        
        chain = prompt | self.llm
        article_type = chain.invoke({"content": content[:1000]}).strip().lower()
        
        valid_types = ["technology", "financial", "sports", "entertainment", "politics", "health", "general"]
        for vtype in valid_types:
            if vtype in article_type:
                return vtype
        return "general"
    
    def generate_summary(self, content: str) -> str:
        prompt = PromptTemplate(
            input_variables=["content"],
            template="""Provide a concise 3-4 sentence summary of this article. Focus on the key points and main ideas.

Article: {content}

Summary:"""
        )
        
        chain = prompt | self.llm
        summary = chain.invoke({"content": content})
        
        return summary.strip()
    
    def summarize_article(self, url: str, date: str = None) -> Dict:
        if date is None:
            date = datetime.now().strftime("%d %B %Y")
        
        print(f"Extracting content from {url}...")
        content = self.extract_article_content(url)
        
        print("Classifying article type...")
        article_type = self.classify_article_type(content)
        
        print("Generating summary...")
        summary = self.generate_summary(content)
        
        result = {
            "date": date,
            "summary": summary,
            "articleType": article_type,
            "url": url
        }
        
        self.summaries.append(result)
        self._save_summaries()
        
        return result
    
    def ask_question(self, question: str) -> str:
        context = json.dumps(self.summaries, indent=2)
        
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""Based on the following news summaries, answer the question.

News Summaries:
{context}

Question: {question}

Answer:"""
        )
        
        chain = prompt | self.llm
        answer = chain.invoke({"context": context, "question": question})
        
        return answer.strip()
    
    def get_all_summaries(self) -> List[Dict]:
        return self.summaries
