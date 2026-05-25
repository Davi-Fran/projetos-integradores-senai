class InventoryPage:
    def __init__(self):
        self.html_products_elements = """"""
        self.html_template_page = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estoque Relatório</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            height: 100vh;
            width: 100vw;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        h1 {
            font-size: 2.5rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>Relatório de produtos em estoque</h1>
    </header>
</body>
</html>"""

        

    def generate_page(self, page_name='inventory_page.html'):
        with open(page_name, 'w', encoding='UTF-8') as file:
            file.write(self.html_template_page)