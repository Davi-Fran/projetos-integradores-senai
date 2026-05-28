from rich import print

class ConsoleHandler:
    @staticmethod
    def show_in_terminal(message, is_success: bool):
        if is_success:
            print(f'\n:white_heavy_check_mark: [bold blue][SUCESSO][/bold blue]: {message}')
        else:
            print(f'\n:warning: [bold red][ERRO][/bold red]: {message}')