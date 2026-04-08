# main.py
from search import SearchEngine
from cli import Colors  # Import Colors from your cli module

def print_banner():
    """Print a colorful banner at startup"""
    banner = f"""
{Colors.BOLD}{Colors.BLUE}╔══════════════════════════════════════╗{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}                                      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}     {Colors.CYAN}███╗   ███╗██╗███╗   ██╗██╗{Colors.RESET}      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}     {Colors.CYAN}████╗ ████║██║████╗  ██║██║{Colors.RESET}      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}     {Colors.CYAN}██╔████╔██║██║██╔██╗ ██║██║{Colors.RESET}      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}     {Colors.CYAN}██║╚██╔╝██║██║██║╚██╗██║██║{Colors.RESET}      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}     {Colors.CYAN}██║ ╚═╝ ██║██║██║ ╚████║██║{Colors.RESET}      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}     {Colors.CYAN}╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝{Colors.RESET}      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}                                      {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}║{Colors.RESET}       {Colors.YELLOW}🔍 Search Engine v1.0{Colors.RESET}          {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}
{Colors.BOLD}{Colors.BLUE}╚══════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

def print_query_help():
    """Print detailed query help with colors"""
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}┌─────────────────────────────────────────────────────────┐{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}              {Colors.YELLOW}📖 QUERY SYNTAX GUIDE{Colors.RESET}                         {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}├─────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}                                                         {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}  {Colors.GREEN}Single Term:{Colors.RESET}                                           {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.CYAN}python{Colors.RESET}              - Search for 'python'                   {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}                                                         {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}  {Colors.GREEN}Boolean Operators:{Colors.RESET}                                      {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.CYAN}python AND java{Colors.RESET}     - Both terms must appear            {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.CYAN}python OR java{Colors.RESET}      - Either term can appear             {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}                                                         {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}  {Colors.GREEN}Phrase Search:{Colors.RESET}                                         {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.CYAN}\"machine learning\"{Colors.RESET}   - Exact phrase match                 {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}                                                         {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}  {Colors.GREEN}Grouping:{Colors.RESET}                                             {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.CYAN}(python OR java) AND testing{Colors.RESET} - Group expressions        {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}                                                         {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}  {Colors.GREEN}Special Commands:{Colors.RESET}                                      {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.YELLOW}stats{Colors.RESET}                - Show index statistics             {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.YELLOW}help{Colors.RESET}                 - Show this help message            {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.YELLOW}clear{Colors.RESET}                - Clear screen                      {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}    {Colors.YELLOW}quit/exit{Colors.RESET}            - Exit the program                  {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}                                                         {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}└─────────────────────────────────────────────────────────┘{Colors.RESET}\n")

def print_colored_results(results, query):
    """Display search results with rich colors"""
    if not results:
        Colors.print_warning(f"No results found for '{query}'")
        return
    
    # Success header with count
    Colors.print_success(f"Found {len(results)} result{'s' if len(results) != 1 else ''} for '{query}'")
    print()
    
    # Display each result with colors
    for i, result in enumerate(results[:20], 1):
        # Result number with ranking badge
        if i <= 3:
            # Top 3 results get special badges
            badges = {1: "🥇", 2: "🥈", 3: "🥉"}
            badge = Colors.colorize(f"{badges[i]} ", Colors.YELLOW)
        else:
            badge = Colors.colorize(f"{i:2}. ", Colors.CYAN)
        
        # Handle both dictionary and tuple results
        if isinstance(result, dict):
            # If result is a dictionary
            file_path = result.get('file_path', result.get('doc_id', 'Unknown'))
            score = result.get('score', None)
            preview = result.get('preview', '')
        elif isinstance(result, tuple):
            # If result is a tuple (assuming (file_path, score) or (doc_id,))
            if len(result) >= 1:
                file_path = str(result[0])
            else:
                file_path = "Unknown"
            
            # Check if score exists as second element
            score = result[1] if len(result) >= 2 else None
            preview = result[2] if len(result) >= 3 else ''
        else:
            # Fallback for other types
            file_path = str(result)
            score = None
            preview = ''
        
        # File path with truncation
        max_length = 70
        if len(file_path) > max_length:
            file_path = "..." + file_path[-(max_length-3):]
        
        # Print result with score if available
        if score is not None:
            print(f"{badge}{Colors.colorize(file_path, Colors.WHITE)} {Colors.colorize(f'(score: {score:.3f})', Colors.CYAN)}")
        else:
            print(f"{badge}{Colors.colorize(file_path, Colors.WHITE)}")
        
        # Show preview if available
        if preview:
            preview_text = preview[:200]
            print(f"     {Colors.colorize(preview_text, Colors.CYAN)}...\n")
        else:
            print()  # Add empty line for spacing
    
    # Show "more results" message if needed
    if len(results) > 20:
        Colors.print_info(f"... and {len(results) - 20} more results")

def clear_screen():
    """Clear terminal screen"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main interactive search engine app"""
    # Print welcome banner
    print_banner()
    
    # Initialize search engine
    Colors.print_info("Initializing search engine...")
    search_engine = SearchEngine()
    
    # Get directory to index
    print(f"\n{Colors.BOLD}{Colors.YELLOW}📁 Directory Selection{Colors.RESET}")
    print(Colors.colorize("─" * 50, Colors.BLUE))
    
    while True:
        directory = input(f"{Colors.CYAN}Enter directory path{Colors.RESET} "
                         f"{Colors.colorize('(or . for current, q to quit)', Colors.WHITE)}: ").strip()
        
        if directory.lower() in ['q', 'quit', 'exit']:
            Colors.print_warning("Exiting...")
            return
        
        if not directory:
            directory = "."
        
        try:
            Colors.print_info(f"Indexing directory: {Colors.BOLD}{directory}{Colors.RESET}")
            search_engine.index_directory(directory)
            Colors.print_success("Successfully indexed directory!")
            break
        except Exception as e:
            Colors.print_error(f"Failed to index: {e}")
            Colors.print_info("Please try a different directory\n")
    
    # Main search loop
    while True:
        # Print search header
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}┌─────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}  {Colors.YELLOW}🔍 READY TO SEARCH{Colors.RESET}                                      {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}└─────────────────────────────────────────────────────────┘{Colors.RESET}")
        
        # Get query with colored prompt
        query = input(f"\n{Colors.BOLD}{Colors.GREEN}┌─[{Colors.CYAN}Search{Colors.GREEN}]─{Colors.RESET}\n"
                     f"{Colors.BOLD}{Colors.GREEN}└─❯ {Colors.RESET}").strip()
        
        # Handle commands
        if query.lower() in ['quit', 'exit', 'q']:
            print(f"\n{Colors.BOLD}{Colors.MAGENTA}Thank you for using Mini Search Engine!{Colors.RESET}")
            Colors.print_success("Goodbye! 👋")
            break
            
        elif query.lower() == 'stats':
            stats = search_engine.index.stats()
            Colors.print_header("\n📊 Index Statistics")
            print(f"  {Colors.colorize('Total Documents:', Colors.BOLD)} {stats.get('total_documents', 0)}")
            print(f"  {Colors.colorize('Unique Terms:', Colors.BOLD)} {stats.get('unique_terms', 0)}")
            print(f"  {Colors.colorize('Term Occurrences:', Colors.BOLD)} {stats.get('total_term_occurrences', 0)}")
            continue
            
        elif query.lower() == 'help':
            print_query_help()
            continue
            
        elif query.lower() == 'clear':
            clear_screen()
            print_banner()
            continue
            
        elif not query:
            Colors.print_warning("Please enter a search query")
            continue
        
        # Perform search
        print(f"\n{Colors.CYAN}🔍 Searching...{Colors.RESET}")
        try:
            results = search_engine.search(query)
            
            # Display results with colors
            print()
            print_colored_results(results, query)
            
            # Show tip for better searching if no results
            if not results:
                print(f"\n{Colors.YELLOW}💡 Tip:{Colors.RESET} Try using {Colors.CYAN}AND{Colors.RESET}, {Colors.CYAN}OR{Colors.RESET}, or {Colors.CYAN}quotes{Colors.RESET} for better results")
                print(f"   Type {Colors.GREEN}help{Colors.RESET} to see query syntax guide\n")
                
        except Exception as e:
            Colors.print_error(f"Search error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠ Interrupted by user{Colors.RESET}")
        Colors.print_success("Goodbye! 👋")
    except Exception as e:
        Colors.print_error(f"Fatal error: {e}")