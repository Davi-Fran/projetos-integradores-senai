from pandas import DataFrame
import os

class Excel:
    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe

    def generate_report(self, report_name='report'):
        desktop_path = f'{os.getcwd()}/../../../'

        self.dataframe.to_excel(f'{desktop_path}/{report_name}.xlsx', index=False)