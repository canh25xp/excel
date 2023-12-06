import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

output_file = 'output.xlsx'
input_file = 'data/input.xlsx'

input = pd.read_excel(input_file,skiprows=[1,2])

sorted_date = input.sort_values('Ngày tiếp nhận')

# print(input)

dates = sorted_date['Ngày tiếp nhận']

# years = dates.dt.strftime('%Y')
# months = dates.dt.strftime('%b')
# weeks = dates.dt.strftime('%a')
# days = dates.dt.strftime('%d')

group = sorted_date.groupby('Tên gói ', sort=False)
service_id_group = group[['Ngày tiếp nhận','Thành tiền (đã tính miễn giảm)']]

print(group['Thành tiền (đã tính miễn giảm)'].sum(),'\n\n')

for name, group in service_id_group:
    print(name)
    # print(group)
    months = group['Ngày tiếp nhận'].dt.strftime('%b')
    days = group['Ngày tiếp nhận'].dt.strftime('%d')
    group_by_month = group.groupby([months, days], sort=False)['Thành tiền (đã tính miễn giảm)'].sum()
    print(group_by_month)
    print('\n\n')
    

# # plt.figure()
# concat.plot(kind='bar', legend=True)
# # plt.savefig('date')
# plt.show()
# plt.close('all')