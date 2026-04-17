# main.py
from search import SearchEngine
from cli import Colors, print_banner, print_colored_results, handle_command, select_directory


def main():
    print_banner()
    Colors.print_info("Initializing search engine...")
    search_engine = SearchEngine()

    if not select_directory(search_engine):
        return

    while True:
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}┌─────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}  {Colors.YELLOW}🔍 READY TO SEARCH{Colors.RESET}                                      {Colors.BOLD}{Colors.MAGENTA}│{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}└─────────────────────────────────────────────────────────┘{Colors.RESET}")

        query = input(
            f"\n{Colors.BOLD}{Colors.GREEN}┌─[{Colors.CYAN}Search{Colors.GREEN}]─{Colors.RESET}\n"
            f"{Colors.BOLD}{Colors.GREEN}└─❯ {Colors.RESET}"
        ).strip()

        result = handle_command(query, search_engine)
        if result == 'quit':
            break
        if result == 'continue':
            continue

        print(f"\n{Colors.CYAN}🔍 Searching...{Colors.RESET}")
        try:
            results = search_engine.search(query)
            print()
            print_colored_results(results, query)

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
