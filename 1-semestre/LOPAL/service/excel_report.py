from pandas import DataFrame
import os

class Excel:
    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe

    def generate_report(self, report_name='report'):
        try:
            os.makedirs('reports', exist_ok=True)

            self.dataframe.to_excel(f'./reports/{report_name}.xlsx', index=False)
        except PermissionError:
            return 'Feche o arquivo antes de tentar gerar um novo!', False
        except ValueError:
            return 'Tipo de arquivo inválido!', False
        except Exception as error:
            return f'Erro inesperado -> {error}', False
        
        return 'Relatório xlsx gerado em "reports" no diretório do projeto!', True