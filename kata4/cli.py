import sys
from summarizer import NewsSummarizer

def main():
    summarizer = NewsSummarizer()
    
    while True:
        print("\n News Summarization Tool ")
        print("1. Summarize a news article")
        print("2. View all summaries")
        print("3. Ask a question about summaries")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
                url = input("Enter the news article URL: ").strip()
                date = input("Enter date (or press Enter for today): ").strip()            
                result = summarizer.summarize_article(url, date if date else None)
                print("\n Summary Created ")
                print(f"Date: {result['date']}")
                print(f"Article Type: {result['articleType']}")
                print(f"Summary: {result['summary']}")
        
        elif choice == "2":
            summaries = summarizer.get_all_summaries()
            if not summaries:
                print("\nNo summaries available yet.")
            else:
                print(f"\n--- All Summaries ({len(summaries)} total) ---")
                for i, summary in enumerate(summaries, 1):
                    print(f"\n{i}. Date: {summary['date']}")
                    print(f"   Type: {summary['articleType']}")
                    print(f"   Summary: {summary['summary']}")
                    print(f"   URL: {summary['url']}")
        
        elif choice == "3":
            if not summarizer.get_all_summaries():
                print("\nNo summaries available. Please add some articles first.")
                continue
            
            question = input("Enter your question: ").strip()
            if question:
                print("\nThinking...")
                answer = summarizer.ask_question(question)
                print(f"\nAnswer: {answer}")
        
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please try again.")
main()
