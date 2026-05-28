from model.products import Products
from service.excel_report import Excel
from view.inventory_view import InventoryPage
from view.console_handler import ConsoleHandler

def app():
    products = Products() # Lê a base de dados
    df = products.get_dataframe() # Recebe os produtos no formato de dataframe

    report_excel = Excel(df) # Recebe o dataframe
    msg, success = report_excel.generate_report('Relatório') # Tenta gerar o relatório em xlsx
    ConsoleHandler.show_in_terminal(msg, success) # Relata o sucesso ou falha

    report_page = InventoryPage(df)
    msg, success = report_page.generate_page('Página') # Tenta gerar um relatório em uma página web
    ConsoleHandler.show_in_terminal(msg, success)

    if not success:
        return

if __name__ == '__main__':
    app()