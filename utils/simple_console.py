class ConsoleUtils:
    """Simple console-based utilities for user interaction."""

    def send_message(self, message: str):
        print(message)
        return "Sent message successfully."

    def ask_user(self, prompt: str):
        try:
            return input(f"{prompt}\n")
        except KeyboardInterrupt:
            raise
