import camelot

tables = camelot.read_pdf('food.pdf', pages='1')
print (tables)

table.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('food.csv')

