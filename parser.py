

#### læse fil
#### checke for fejl
#### finde ud af hvad vi gør med fejl
#### omformatere fil
#### output format evt JSON

import os


#### Includes path to folder
#### Name of csv_file
#### IF the csv file contain a header or not

def reader(path, csv_file, header = True):
    os.chdir(path)
    if header == True:
        ### Need to make the first line do something
        1+1

    else:
        ###
        1+1
    return ### Read file checked for wierd stuff


path = r'C:\Users\SPAC-B-16\GLE_Special\Opgaver\Parser'
os.chdir(path)

file = open("test.csv", mode='r', newline = '\n')
# print(file.read())

### Make file into nested list with each line being the under
### underlying list
file_in_lines = file.read().splitlines()
file_in_words = []
for i in range(len(file_in_lines)):
    file_in_words.append(file_in_lines[i].split(","))

### Creating a nested dictionary
entry = []
for i in range(1, len(file_in_words)):
    under = {}
    for j in range(len(file_in_words[0])):
        under[file_in_words[0][j]] = file_in_words[i][j]
    entry.append(under)

print(entry[0]["name"])
print(entry[0])
