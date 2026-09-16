#### læse fil
#### checke for fejl
#### finde ud af hvad vi gør med fejl
#### omformatere fil
#### output format evt JSON

import os
class Parcer():

    def __init__(self, path, file_name, header = True):
        self.path = path
        self.filename = file_name
        self.header = header

    def reader(self):
        os.chdir(self.path)
        file = open(self.filename, mode='r', newline = '\n')
        self.file = file.read()
        return self.file

    def new_data_format(self):
        line_split = self.file.splitlines()
        file_in_words = []
        for i in range(len(line_split)):
            file_in_words.append(line_split[i].split(","))

        array_dict_entry = []
        for i in range(1, len(file_in_words)):
            underlying_dict = {}
            for j in range(len(file_in_words[0])):
                underlying_dict[file_in_words[0][j]] = file_in_words[i][j]
            array_dict_entry.append(underlying_dict)    
        self.new_data = array_dict_entry

    def final(self):
        self.reader()
        self.new_data_format()
        return self.new_data

if __name__ == "__main__":
    newdata_type = Parcer(r'C:\Users\SPAC-B-16\GLE_Special\Opgaver\Parser', "employees.ascii.csv", header = True).final()
    print(newdata_type)


#### TO DO
#### GØr ting med header
#### HVad gør vi med fejl

#### UNIT TEST:
#### Tom fil
#### Fil med og uden header
#### Check at der ikke er hardcoded noget i fohold til index
#### Hvad gør jeg med "nul" værdier 
#### Check fil type
#### Hvad gør jeg med helt fucked documenter
#### Hvad hvis det ikke er comma sepereret
#### 