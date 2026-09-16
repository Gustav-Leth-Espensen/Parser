#### læse fil
#### checke for fejl
#### finde ud af hvad vi gør med fejl
#### omformatere fil
#### output format evt JSON

import os
class Parcer():

    def __init__(self, path: str, file_name: str, header: bool):
        self.path = path
        self.filename = file_name
        self.header = header

        os.chdir(self.path)

    def initial_checks(self):
        self.errormessage = False
        if not self.filename.lower().endswith(".csv"):
            self.errormessage = "This is not a .csv file"
            return
        if os.path.getsize(self.filename) == 0:
            self.errormessage = "This file is empty"
            return
        


    def reader(self):
        file = open(self.filename, mode='r', newline = '\n')
        self.file = file.read()

    def new_data_format(self):
        line_split = self.file.splitlines()
        file_in_words = []
        for i in range(len(line_split)):
            file_in_words.append(line_split[i].split(","))
        self.file_in_words = file_in_words

        self.missing_elements = []
        for i in range(len(file_in_words)):
            if len(file_in_words[0]) < len(file_in_words[i]):
                self.errormessage = "This file does not fit the normal csv format."
                print("testtsetsetsetstet")
                return
            if len(file_in_words[0]) != len(file_in_words[i]):
                self.missing_elements.append(i)

        self.new_data = []
        for i in range(1, len(file_in_words)):
            underlying_dict = {}
            for j in range(len(file_in_words[i])):
                underlying_dict[file_in_words[0][j]] = file_in_words[i][j]
            self.new_data.append(underlying_dict)
        

    def final(self):
        self.initial_checks()
        if self.errormessage:
            return self.errormessage
        if self.header == False:
            self.reader()
            self.new_data_format()
            if self.errormessage:
                return self.errormessage
            if self.missing_elements:
                return self.file_in_words, f"Missing data in entry: {self.missing_elements}"
            else:
                return self.file_in_words
        else:
            self.reader()
            self.new_data_format()
            if self.errormessage:
                return self.errormessage
            if self.missing_elements:
                return self.new_data, f"Missing data in entry: {self.missing_elements}" 
            else:
                return self.new_data

if __name__ == "__main__":
    newdata_type = Parcer(r'C:\Users\SPAC-B-16\GLE_Special\Opgaver\Parser\tests', "shorter_rows_h.csv", header = True).final()
    print(newdata_type)


#### TO DO
#### GØr ting med header      # DONE
#### HVad gør vi med fejl

#### UNIT TEST:
#### Tom fil         DONE
#### Fil med og uden header         DONE
#### Check at der ikke er hardcoded noget i fohold til index
#### Hvad gør jeg med "nul" værdier  #### med header gør de dem bare tomme samme uden header
#### HVad gør jeg med rækker der er for korte   DONE, fortæller hvor der er korte rækker
#### Check fil type           DONE
#### Hvad gør jeg med helt fucked documenter
#### Hvad hvis det ikke er comma sepereret
#### Find ud af hvad jeg gør med ikke ascii characterer (bl.a. æ, ø og å)