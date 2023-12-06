import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def main(opt):
    input_file = opt.input
    output_file = opt.output
    input = pd.read_excel(input_file,skiprows=[1,2])
    sorted_date = input.sort_values('Ngày tiếp nhận')
    
    # print(input)

    # Names = input['Họ và Tên']
    # Dates = input['Ngày tiếp nhận']
    # Cash = input['Thành tiền (đã tính miễn giảm)']

    dates = sorted_date['Ngày tiếp nhận']

    years = dates.dt.strftime('%Y')
    months = dates.dt.strftime('%b')
    weeks = dates.dt.strftime('%a')
    days = dates.dt.strftime('%d')

    money_group = sorted_date.groupby([months], sort=False)['Thành tiền (đã tính miễn giảm)'].sum()

    # service_group = sorted_date.groupby('Tên gói ')['Thành tiền (đã tính miễn giảm)'].sum()

    total_money = money_group.cumsum()

    money_group.name = 'Thành tiền'
    total_money.name = 'Tổng thành tiền'

    concat = pd.concat([money_group, total_money], axis=1)

    print(months)
    # money_group.to_excel('test.xlsx')

    # plt.figure()
    # money_group.plot(kind='bar', legend=True)
    # plt.show()
    # plt.close('all')

    # Save as excel
    if(opt.save):
        writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

        concat.to_excel(writer, sheet_name='Sheet1')

        workbook = writer.book

        chartsheet = workbook.add_chartsheet()
        chart = workbook.add_chart({'type': 'column'})

        chart.add_series({
            'values': '=Sheet1!$B$2:$B$9',
            'categories':'=Sheet1!$A$2:$A$9',
            'name':'money'
        })

        chartsheet.set_chart(chart)

        writer.close()
        
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', metavar='path/to/input.xlsx', type=str, default='data/input.xlsx', help='Path to the xlsx file')
    parser.add_argument('-o','--output', metavar='path/to/output.xlsx', type=str,default='output.xlsx', help='output location')
    parser.add_argument('--save', action='store_true', help='write output to xlsx file')
    
    opt = parser.parse_args()
    main(opt)