from search import SearchEngine

def main():
    """Main interactive serach engine app"""
    print("Mini Search Engine")
    #Initialize search engine
    search_engine = SearchEngine()
    
    #Get directory to index
    while True:
        directory=input("Enter directory path to index (or '.' for current dir): ").strip()
        if not directory:
            directory="."
        
        try:
            search_engine.index_directory(directory)
            break
        except Exception as e:
            print(f"error: {e}")
            print("Try again\n")
    
    #Interactive serach loop
    print("Search Mode")

    while True:
        print("Commands: 'python programming'(enter search term), 'quit' or 'exit'(to stop), 'stats'(to see index stats)")
        query = input("Search > ").strip()
        if query.lower() in ['quit','exit']:
            print("exitng...")
            break
        elif query.lower() == 'stats':
            stats=search_engine.index.stats()
            print("\nIndex Stats:")
            print(f"-Total Docs: {stats['total_documents']}")
            print(f"-Unique Terms: {stats['unique_terms']}")
            print(f"-Term Occurrences: {stats['total_term_occurrences']}")
            continue
        elif not query:
            continue

        #Perform Search
        results=search_engine.search(query)
        search_engine.display_results(results)

if __name__ == "__main__":
    main()



