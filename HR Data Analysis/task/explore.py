from typing import final

import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here

    a_office = pd.read_xml('../Data/A_office_data.xml')
    b_office = pd.read_xml('../Data/B_office_data.xml')
    hr_data = pd.read_xml('../Data/hr_data.xml')
    a_office.index = 'A' + a_office['employee_office_id'].astype(str)
    b_office.index = 'B' + b_office['employee_office_id'].astype(str)
    hr_data.index = hr_data['employee_id']
    unified_office = pd.concat([a_office,b_office])
    result = unified_office.merge(hr_data, left_index = True, right_index = True,how = 'inner', indicator = True)
    final_table = result.drop(['employee_office_id', 'employee_id', '_merge'], axis = 1)
    final_table.sort_index(inplace = True)
    depart_s = final_table.sort_values(by = 'average_monthly_hours', ascending = False).Department[:10]
    #depart_s = final_table.nlargest(n = 10, columns =  'average_monthly_hours').Department
    total_n = final_table.query("Department == 'IT' & salary == 'low'").number_project.sum()
    #emplo_info = final_table.loc[final_table.index.isin(['A4','B7064','A3033']), ['last_evaluation', 'satisfaction_level']].values.tolist()
    emplo_info = []
    for emp in ['A4', 'B7064', 'A3033']:
        emp_data = final_table.loc[final_table.index == emp, ['last_evaluation', 'satisfaction_level']]
        emplo_info.append(emp_data.values[0].tolist())
    print(depart_s.tolist())
    print(total_n.tolist())
    print(emplo_info)

