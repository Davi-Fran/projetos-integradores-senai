from rich import print

class ConsoleHandler:
    @staticmethod
    def show_on_terminal(message, is_error: bool = False):
        if is_error:
            print(f'\n:warning: [bold red][ERRO][/bold red]: {message}')
        else:
            print(f'\n:white_check_mark: [bold blue][SUCESSO][/bold blue]: {message}')