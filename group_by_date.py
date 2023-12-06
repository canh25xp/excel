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

# Names = input['Họ và Tên']
# Dates = input['Ngày tiếp nhận']
# Cash = input['Thành tiền (đã tính miễn giinput)']

dates = sorted_date['Ngày tiếp nhận']

years = dates.dt.strftime('%Y')
months = dates.dt.strftime('%b')
weeks = dates.dt.strftime('%a')
days = dates.dt.strftime('%d')

money_group = sorted_date.groupby([months], sort=False)['Thành tiền (đã tính miễn giảm)'].sum()
total_money = money_group.cumsum()

money_group.name = 'Thành tiền'
total_money.name = 'Tổng thành tiền'

concat = pd.concat([money_group, total_money], axis=1)

print(concat)

# plt.figure()
concat.plot(kind='bar', legend=True)
# plt.savefig('date')
plt.show()
plt.close('all')

# Save as excel

# writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

# # sorted_date.to_excel(writer, sheet_name='Sheet1', index=False)
# concat.to_excel(writer, sheet_name='Sheet1')

# workbook = writer.book

# chartsheet = workbook.add_chartsheet()
# chart = workbook.add_chart({'type': 'column'})

# chart.add_series({
#     'values': '=Sheet1!$B$2:$B$9',
#     'categories':'=Sheet1!$A$2:$A$9',
#     'name':'money'
# })

# # chart.add_series({
# #     'values': '=Sheet1!$C$2:$C$9',
# #     'gap': 2,
# #     'name':'total money'
# # })


# chartsheet.set_chart(chart)

# writer.close()