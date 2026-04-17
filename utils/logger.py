from cli.colors import Colors


class Logger:
    """Thin wrapper around Colors for consistent progress/status output."""

    def __init__(self, prefix: str = ""):
        self.prefix = f"[{prefix}] " if prefix else ""

    def info(self, message: str):
        Colors.print_info(f"{self.prefix}{message}")

    def success(self, message: str):
        Colors.print_success(f"{self.prefix}{message}")

    def warning(self, message: str):
        Colors.print_warning(f"{self.prefix}{message}")

    def error(self, message: str):
        Colors.print_error(f"{self.prefix}{message}")

    def header(self, message: str):
        Colors.print_header(f"{self.prefix}{message}")
