# cli/colors.py
"""Color utilities for CLI output"""

class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    @staticmethod
    def colorize(text, color):
        """Wrap text with color codes"""
        return f"{color}{text}{Colors.RESET}"
    
    @staticmethod
    def print_error(text):
        """Print error message in red"""
        print(f"{Colors.RED}✗ {text}{Colors.RESET}")
    
    @staticmethod
    def print_success(text):
        """Print success message in green"""
        print(f"{Colors.GREEN}✓ {text}{Colors.RESET}")
    
    @staticmethod
    def print_warning(text):
        """Print warning message in yellow"""
        print(f"{Colors.YELLOW}⚠ {text}{Colors.RESET}")
    
    @staticmethod
    def print_info(text):
        """Print info message in cyan"""
        print(f"{Colors.CYAN}ℹ {text}{Colors.RESET}")
    
    @staticmethod
    def print_header(text):
        """Print header in bold blue"""
        print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.RESET}")
    
    @staticmethod
    def print_success_header(text):
        """Print success header in bold green"""
        print(f"{Colors.BOLD}{Colors.GREEN}{text}{Colors.RESET}")
    
    @staticmethod
    def print_table_row(columns, col_widths, colors=None):
        """Print a formatted table row with colors"""
        row = "│ "
        for i, (col, width) in enumerate(zip(columns, col_widths)):
            if colors and i < len(colors):
                color = colors[i]
            else:
                color = Colors.WHITE
            row += f"{color}{str(col)[:width]:<{width}}{Colors.RESET} │ "
        print(row)
    
    @staticmethod
    def print_progress_bar(percentage, width=30, message=""):
        """Print a colored progress bar"""
        filled = int(width * percentage / 100)
        bar = '█' * filled + '░' * (width - filled)
        
        if percentage < 30:
            color = Colors.RED
        elif percentage < 70:
            color = Colors.YELLOW
        else:
            color = Colors.GREEN
        
        print(f"\r{message} [{color}{bar}{Colors.RESET}] {Colors.BOLD}{percentage:.1f}%{Colors.RESET}", end='')
    
    @staticmethod
    def print_card(title, content, title_color=None):
        """Print a card-style UI element"""
        if title_color is None:
            title_color = Colors.YELLOW
        
        print(f"\n{Colors.BOLD}{Colors.BLUE}┌─ {title_color}{title}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BLUE}│{Colors.RESET}")
        for line in content.split('\n'):
            print(f"{Colors.BOLD}{Colors.BLUE}│{Colors.RESET}   {line}")
        print(f"{Colors.BOLD}{Colors.BLUE}└──────────────────────────────────────────{Colors.RESET}\n")