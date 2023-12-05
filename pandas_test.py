import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ws = pd.read_excel('input.xlsx',skiprows=[1,2])

# print(ws)

# Names = ws['Họ và Tên']
# Dates = ws['Ngày tiếp nhận']
# Cash = ws['Thành tiền (đã tính miễn giảm)']

dates = ws['Ngày tiếp nhận']

years = dates.dt.strftime('%Y')
months = dates.dt.strftime('%b')
weeks = dates.dt.strftime('%a')

money_group = ws.groupby([years, months])['Thành tiền (đã tính miễn giảm)'].sum()

print(money_group)

# money_group.to_excel('output.xlsx')