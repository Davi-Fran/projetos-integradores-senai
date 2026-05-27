from model.products import Products
from service.excel_report import Excel
from view.inventory_view import InventoryPage
from view.console_handler import ConsoleHandler

def app():
    try:
        products = Products()
        df = products.get_dataframe()

        # Recebe os produtos no formato de dataframe e gera um relatório em .xlsx
        """ report_excel = Excel(df)
        report_excel.generate_report('Relatório') """

        # Recebe o dataframe e gera um relatório em uma página web
        """ idk = InventoryPage(df)
        idk.generate_page() """

        ConsoleHandler.show_on_terminal('nsei')
    except FileNotFoundError:
        print('Base não encontrada!')

if __name__ == '__main__':
    app()