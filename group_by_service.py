import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

output_file = 'output.xlsx'
input_file = 'data\DT HIS T7denT11 -23 - gui test 2.xls'

input = pd.read_excel(input_file,skiprows=[0,1,2,3,4,5,7,8])

sorted_date = input.sort_values('Ngày yêu cầu')

# print(input)

dates = sorted_date['Ngày yêu cầu']

# print(dates)

group = sorted_date.groupby('Tên gói ', sort=False)
service_id_group = group[['Ngày yêu cầu','Thành tiền (đã tính miễn giảm)']]

all_group = group['Thành tiền (đã tính miễn giảm)'].sum()
print(all_group,'\n\n')

graph = all_group.plot(kind='bar', legend=True)
graph.ticklabel_format(style='plain', axis='y')
graph.bar_label(graph.containers[0],fmt = '%d')

# plt.savefig('date')
plt.show()
plt.close('all')

for name, group in service_id_group:
    print(name)
    # print(group)
    months = group['Ngày tiếp nhận'].dt.strftime('%b')
    days = group['Ngày tiếp nhận'].dt.strftime('%d')
    group_by_month = group.groupby([months], sort=False)['Thành tiền (đã tính miễn giảm)'].sum()
    print(group_by_month)
    print('\n\n')
    

# # plt.figure()
# concat.plot(kind='bar', legend=True)
# # plt.savefig('date')
# plt.show()
# plt.close('all')