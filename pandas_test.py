import pandas as pd
import os

# path = r'C:\Users\Gusta\Desktop\Python_Code\GLE_opgaver\Parser\tests'
path2 = r"C:\Users\SPAC-B-16\GLE_Special\Opgaver\Parser\tests"

os.chdir(path2)

# path2 = r"\tests\comma_in_quote.csv"
test = pd.read_csv('comma_in_quote.csv')
print(test)