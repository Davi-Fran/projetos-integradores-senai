from pandas import DataFrame
import os

class InventoryPage:
    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe
        
        
    def _get_styles(self):
        """ Método interno da classe, que retorna o CSS da página, para deixar o código mais organizado """

        return """
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Arial', sans-serif; }
            body { height: 100vh; width: 100vw; overflow-x: hidden; }
            header { width: 100%; height: 12%; display: flex; justify-content: center; align-items: center; box-shadow: 0 0 5px #000; }
            h1 { font-size: 2.5rem; }
            main { width: 50%; display: block; margin: 0 auto; margin-top: 2rem; }
            article { margin: 0.5rem; border: 1px solid #000; padding: 1rem; border-radius: 5px; }
            h2 { margin-bottom: 0.3rem; }
            p { margin: 0.3rem 0; }
        </style>"""

    def generate_page(self, page_name='inventory_page'):
        os.makedirs('reports', exist_ok=True)

        articles_list = []

        for row in self.dataframe.itertuples(index=False):
            inventory_total = row.Qtde_Disponivel + row.Qtde_Reservada

            html_product_template = f"""
            <article>
                <h2>{row.Produto}</h2>
                <hr>
                <p>Código: <strong>{row.Codigo}</strong></p>
                <p>Quantidade disponível: <strong>{row.Qtde_Disponivel}</strong></p>
                <p>Quantidade reservada: <strong>{row.Qtde_Reservada}</strong></p>
                <p>Total em estoque: <strong>{inventory_total}</strong></p>
                <p>Preço Unitário: <strong>R${row.Preco}</strong></p>
            </article>"""

            articles_list.append(html_product_template)

        html_products_elements = '\n'.join(articles_list)

        html_template_page = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estoque Relatório</title>
    {self._get_styles()}
</head>
<body>
    <header>
        <h1>Relatório de produtos em estoque</h1>
    </header>

    <main>
        {html_products_elements}
    </main>
</body>
</html>"""

        try:
            with open(f'./reports/{page_name}.html', 'w', encoding='UTF-8') as file:
                file.write(html_template_page)
        except Exception as error:
            return f'Erro inesperado -> {error}', False

        return 'Página web de relatório gerada em "reports" com sucesso!', True