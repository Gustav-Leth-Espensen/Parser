import pandas as pd
import os

path = r'C:\Users\Gusta\Desktop\Python_Code\GLE_opgaver\Parser\tests'

os.chdir(path)
# path2 = r"\tests\comma_in_quote.csv"
test = pd.read_csv('comma_in_quote.csv')
print(test)