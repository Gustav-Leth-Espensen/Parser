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
        if not os.path.isfile(self.filename):
            self.errormessage = "This file does not exist."
            return
        if not self.filename.lower().endswith(".csv"):
            self.errormessage = "This is not a .csv file"
            return
        if os.path.getsize(self.filename) == 0:
            self.errormessage = "This file is empty"
            return
        

    def reader(self):
        file = open(self.filename, mode='r', encoding = "utf-8")
        self.file = file.read()
        return self.file

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
    newdata_type = Parcer(r'C:\Users\SPAC-B-16\GLE_Special\Opgaver\Parser\tests', "wetwetwetw23.csv", header = True).final()
    print(newdata_type)


#### TO DO
#### GØr ting med header      # DONE
#### HVad gør vi med fejl

#### UNIT TEST:
#### Test om filen esksisterer
#### Tom fil         DONE
#### Fil med og uden header         DONE
#### Check at der ikke er hardcoded noget i fohold til index
#### Hvad gør jeg med "nul" værdier  #### med header gør de dem bare tomme samme uden header
#### HVad gør jeg med rækker der er for korte   DONE, fortæller hvor der er korte rækker
#### Check fil type           DONE
#### Hvad gør jeg med helt fucked documenter                  Måske done, ikke sikker på hvor fucked de kan være
#### Hvad hvis det ikke er comma sepereret              #### Alt afhænging af formatet kommer de igennem eller ej, det er svært at overskue alle cases
#### Find ud af hvad jeg gør med ikke ascii characterer (bl.a. æ, ø og å)  DONE
#### Lav en split function som finder ud af hvornår den skal splitte ved kommaer og hvornår den ikke skal
#### Muligvis samme med line split

