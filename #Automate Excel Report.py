#Automate Excel Report
from openpyxl import load_workbook

wb = load_workbook('report.xlsx')
sheet = wb['Report']

sheet ['A1'] = 'Sales Report'
sheet ['A2'] = 'January'

sheet ['A1'],front =Font('Arial', bold=True, size = 20)
sheet ['A2'],front =Font('Arial', bold=True, size = 20)

wb.save(f'report_{month}.xlsx')

