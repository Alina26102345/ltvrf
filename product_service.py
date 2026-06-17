import pandas as pd

def load_products():

    file_path = "excel/Tovar.xlsx"

    data = pd.read_excel(file_path)

    return data