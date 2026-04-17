import os
from .colors import Colors


def print_banner():
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
    if not results:
        Colors.print_warning(f"No results found for '{query}'")
        return

    Colors.print_success(f"Found {len(results)} result{'s' if len(results) != 1 else ''} for '{query}'")
    print()

    for i, result in enumerate(results[:20], 1):
        if i <= 3:
            badges = {1: "🥇", 2: "🥈", 3: "🥉"}
            badge = Colors.colorize(f"{badges[i]} ", Colors.YELLOW)
        else:
            badge = Colors.colorize(f"{i:2}. ", Colors.CYAN)

        if isinstance(result, dict):
            file_path = result.get('file_path', result.get('doc_id', 'Unknown'))
            score = result.get('score', None)
            preview = result.get('preview', '')
        elif isinstance(result, tuple):
            file_path = str(result[0]) if len(result) >= 1 else "Unknown"
            score = result[1] if len(result) >= 2 else None
            preview = result[2] if len(result) >= 3 else ''
        else:
            file_path = str(result)
            score = None
            preview = ''

        max_length = 70
        if len(file_path) > max_length:
            file_path = "..." + file_path[-(max_length - 3):]

        if score is not None:
            print(f"{badge}{Colors.colorize(file_path, Colors.WHITE)} {Colors.colorize(f'(score: {score:.3f})', Colors.CYAN)}")
        else:
            print(f"{badge}{Colors.colorize(file_path, Colors.WHITE)}")

        if preview:
            print(f"     {Colors.colorize(preview[:200], Colors.CYAN)}...\n")
        else:
            print()

    if len(results) > 20:
        Colors.print_info(f"... and {len(results) - 20} more results")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
