import pandas as pd

class Products:
    def __init__(self):
        self.dataframe = pd.read_csv('./data/Produtos.csv', delimiter=';')

    def get_dataframe(self, *, show_all_rows: bool = False):
        if show_all_rows:
            pd.set_option('display.max_rows', None)

        return self.dataframe