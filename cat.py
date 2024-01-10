import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

output_file = 'output.xlsx'
input_file = 'input\HDBR 2302.xlsx'

file_1  = pd.read_excel("input\HDBR 2302.xlsx",skiprows=[0,1,2,3,4])
file_2  = pd.read_excel("input\HDBR 2303.xlsx",skiprows=[0,1,2,3,4])
file_3  = pd.read_excel("input\HDBR 2304.xlsx",skiprows=[0,1,2,3,4])
file_4  = pd.read_excel("input\HDBR 2305.xlsx",skiprows=[0,1,2,3,4])
file_5  = pd.read_excel("input\HDMV 2301.xlsx",skiprows=[0,1,2,3,4])
file_6  = pd.read_excel("input\HDMV 2302.xlsx",skiprows=[0,1,2,3,4])
file_7  = pd.read_excel("input\HDMV 2303.xlsx",skiprows=[0,1,2,3,4])
file_8  = pd.read_excel("input\HDMV 2304.xlsx",skiprows=[0,1,2,3,4])
file_9  = pd.read_excel("input\HDMV 2305.xlsx",skiprows=[0,1,2,3,4])
file_10 = pd.read_excel("input\HDMV 2306.xlsx",skiprows=[0,1,2,3,4])
file_11 = pd.read_excel("input\HDMV 2307.xlsx",skiprows=[0,1,2,3,4])
file_12 = pd.read_excel("input\HDMV 2308.xlsx",skiprows=[0,1,2,3,4])
file_13 = pd.read_excel("input\HDMV 2309.xlsx",skiprows=[0,1,2,3,4])
file_14 = pd.read_excel("input\HDMV 2310.xlsx",skiprows=[0,1,2,3,4])
file_15 = pd.read_excel("input\HDMV 2311.xlsx",skiprows=[0,1,2,3,4])
file_16 = pd.read_excel("input\HDMV 2312.xlsx",skiprows=[0,1,2,3,4])

pdList = []
pdList.extend(value for name, value in locals().items() if name.startswith("file_"))

concat = pd.concat(pdList)

print(concat)

# Save as excel

writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

concat.to_excel(writer, sheet_name='Sheet1', index=False)

# workbook = writer.book

writer.close()