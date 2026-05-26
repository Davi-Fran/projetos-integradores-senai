from model.products import Products
from service.excel_report import Excel
from view.inventory_view import InventoryPage

def app():
    try:
        products = Products()
        df = products.get_dataframe()
        print(df)

        # Recebe os produtos no formato de dataframe e gera um relatório em .xlsx
        """ report_excel = Excel(products.get_dataframe())
        report_excel.generate_report('Relatório') """

        idk = InventoryPage(df)
        idk.generate_page()
    except FileNotFoundError:
        print('Base não encontrada!')

if __name__ == '__main__':
    app()