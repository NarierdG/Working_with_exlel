import pandas as pd

def convert_txt_to_xls(txt_file, xls_file):
    data = []

    with open(txt_file, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.split(';')

        for line in lines:
            line = line.strip()
            if line:
                values = line.split(',')
                data.append(values)

    df = pd.DataFrame(data)

    df.to_excel(xls_file, index=False, header=False)

convert_txt_to_xls('ln.txt', 'output.xlsx')
