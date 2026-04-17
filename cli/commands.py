from .colors import Colors
from .formatter import print_query_help, print_colored_results, clear_screen, print_banner


def handle_command(query, search_engine):
    """
    Process a REPL command. Returns:
      'quit'     - user wants to exit
      'continue' - command was handled, re-prompt
      None       - not a command, caller should treat as a search query
    """
    cmd = query.lower()

    if cmd in ('quit', 'exit', 'q'):
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}Thank you for using Mini Search Engine!{Colors.RESET}")
        Colors.print_success("Goodbye! 👋")
        return 'quit'

    if cmd == 'stats':
        stats = search_engine.index.stats()
        Colors.print_header("\n📊 Index Statistics")
        print(f"  {Colors.colorize('Total Documents:', Colors.BOLD)} {stats.get('total_documents', 0)}")
        print(f"  {Colors.colorize('Unique Terms:', Colors.BOLD)} {stats.get('unique_terms', 0)}")
        print(f"  {Colors.colorize('Term Occurrences:', Colors.BOLD)} {stats.get('total_term_occurrences', 0)}")
        return 'continue'

    if cmd == 'help':
        print_query_help()
        return 'continue'

    if cmd == 'clear':
        clear_screen()
        print_banner()
        return 'continue'

    if not query:
        Colors.print_warning("Please enter a search query")
        return 'continue'

    return None


def select_directory(search_engine):
    """Prompt the user to pick a directory and index it. Returns when indexing succeeds."""
    print(f"\n{Colors.BOLD}{Colors.YELLOW}📁 Directory Selection{Colors.RESET}")
    print(Colors.colorize("─" * 50, Colors.BLUE))

    while True:
        directory = input(
            f"{Colors.CYAN}Enter directory path{Colors.RESET} "
            f"{Colors.colorize('(or . for current, q to quit)', Colors.WHITE)}: "
        ).strip()

        if directory.lower() in ('q', 'quit', 'exit'):
            Colors.print_warning("Exiting...")
            return False

        if not directory:
            directory = "."

        try:
            Colors.print_info(f"Indexing directory: {Colors.BOLD}{directory}{Colors.RESET}")
            search_engine.index_directory(directory)
            Colors.print_success("Successfully indexed directory!")
            return True
        except Exception as e:
            Colors.print_error(f"Failed to index: {e}")
            Colors.print_info("Please try a different directory\n")
