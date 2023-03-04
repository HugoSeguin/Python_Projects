#Downlaoding Wiki tables
import pandas as pd

table = pd.read_html('https://en.wikipedia.org/wiki/Colorado_Avalanche')

len(table)
table[0]