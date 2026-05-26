from pandas import DataFrame
import os

class InventoryPage:
    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe
        self.html_template_page = ''
        self.html_products_elements = ''
        self.css_styles = """<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            height: 100vh;
            width: 100vw;
            overflow-x: hidden;
        }

        header {
            width: 100%;
            height: 12%;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 0 5px #000;
        }

        h1 {
            font-size: 2.5rem;
        }

        main {
            width: 50%;
            display: block;
            margin: 0 auto;
            margin-top: 2rem;
        }

        article {

            margin: 0.5rem;
            border: 1px solid #000;
            padding: 1rem;
            border-radius: 5px;
        }

        h2 {
            margin-bottom: 0.3rem;
        }

        p {
            margin: 0.3rem 0;
        }
    </style>"""

    def generate_page(self, page_name='inventory_page.html'):
        desktop_path = f'{os.getcwd()}/../../../'

        for i in range(len(self.dataframe)):
            qtde_produto_disponivel = self.dataframe.iloc[i]['Qtde_Disponivel']
            qtde_produto_reservado = self.dataframe.iloc[i]['Qtde_Reservada']
            total_produto_estoque = qtde_produto_disponivel + qtde_produto_reservado

            html_product_template = f"""<article>
            <h2>{self.dataframe.iloc[i]['Produto']}</h2>
            <hr>
            <p>Código: <strong>{self.dataframe.iloc[i]['Codigo']}</strong></p>
            <p>Quantidade disponível: <strong>{qtde_produto_disponivel}</strong></p>
            <p>Quantidade reservada: <strong>{qtde_produto_reservado}</strong></p>
            <p>Total em estoque: <strong>{total_produto_estoque}</strong></p>
            <p>Preço Unitário: <strong>R${self.dataframe.iloc[i]['Preco']}</strong></p>
         </article>"""

            self.html_products_elements += html_product_template

        self.html_template_page = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estoque Relatório</title>
    {self.css_styles}
</head>
<body>
    <header>
        <h1>Relatório de produtos em estoque</h1>
    </header>

    <main>
        {self.html_products_elements}
    </main>
</body>
</html>"""

        with open(f'{desktop_path}/{page_name}.html', 'w', encoding='UTF-8') as file:
            file.write(self.html_template_page)