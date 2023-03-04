Import wants needed
Import os
Import pandas as pd
Import openpyxl

Open file
File = openpxl,load_workboad (‘____document na,e___)
Delete uneeded columns
Worksheet.getCells().deleteColumns(0,0, True) 
Sort values
File.sort_values(by=’___’)
#Write a cell 
Worksheet.write_formula(‘A1’, ‘[formula]’) 
for i, cellObj in enumerate(Sheet.columns[2], 1):
    cellObj.value = '=IF($A${0}=$B${0}, "Match", "Mismatch")'.format(i)
Close file
File.close()
#Run a script
$python3 {Document name}
	
