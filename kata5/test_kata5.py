#!/usr/bin/env python3
"""Quick test script for kata5"""

from question_to_sql import QuestionToSQLSystem

def test_kata5():
    print("=" * 60)
    print("Testing Kata 5: Question to SQL System")
    print("=" * 60)
    
    try:
        print("\n1. Initializing the system...")
        system = QuestionToSQLSystem()
        print("   ✓ System initialized successfully")
        
        print("\n2. Testing with a simple question...")
        test_question = "Show me the top customers"
        print(f"   Question: '{test_question}'")
        
        result = system.process_question(test_question)
        
        if result:
            print("\n   ✓ Test PASSED!")
            print("\n" + "=" * 60)
            print("KATA 5 IS WORKING CORRECTLY!")
            print("=" * 60)
            print("\nYou can now run the full demo:")
            print("  python kata5/question_to_sql.py")
            return True
        else:
            print("\n   ✗ Test FAILED - No result returned")
            return False
            
    except Exception as e:
        print(f"\n   ✗ Test FAILED with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_kata5()
