
class parcer():

    def __init__(self, header: bool, seperator = ","):
        self.header = header
        self.seperator = seperator

    #### \r is only newline on windows, otherwise it moves the curser to the start of current line
    #### Hvad var ideen med den nye newline function?
    def split_lines(csv_text):
        split_str = []
        newline = 0
        for i in range(len(csv_text)):
            if csv_text[i] == ("\n" or "\r"):
                split_str.append(csv_text[newline:i])
                newline = i + 1
            if i == len(csv_text) - 1:
                split_str.append(csv_text[newline:i+1])

        return split_str


    #### Change seperator from , to self.seperator
    def split_words(self, csv_text):
        split_to_words = []
        newword = 0
        inbetween = False
        for i in range(len(csv_text)):
            if csv_text[i] == "\"":
                inbetween = not inbetween
                print(inbetween)
            if csv_text[i] == self.seperator and inbetween != True:
                split_to_words.append(csv_text[newword:i])
                newword = i + 1
            if i == len(csv_text) - 1:
                split_to_words.append(csv_text[newword:i+1])
                
        return split_to_words


    def parce(self, csv_text: str):
        if csv_text == "":
            return "This is an empty string"
        line_split = parcer.split_lines(csv_text)

        file_in_words = []
      
        for i in range(len(line_split)):
            file_in_words.append(self.split_words(line_split[i]))

        missing_elements = []
        for i in range(len(file_in_words)):
            if len(file_in_words[0]) < len(file_in_words[i]):
                return "This file does not fit the normal csv format."
            ### Giver det mening at lave det næste i nyt forloop
            if len(file_in_words[0]) != len(file_in_words[i]):
                missing_elements.append(i)
        if self.header == True:
            if len(file_in_words) == 1:
                return "Needs at least two lines with header."
            new_structure = []
            for i in range(1, len(file_in_words)):
                underlying_dict = {}
                for j in range(len(file_in_words[i])):
                    underlying_dict[file_in_words[0][j]] = file_in_words[i][j]
                new_structure.append(underlying_dict)
        else:
            new_structure = file_in_words

        if missing_elements:
            return new_structure, f"Missing data in entry: {missing_elements}"
        return new_structure

    def json_converter(self, csv_file):
        #### Check if self.header True or false for type of output from parce:
        test = self.parce(csv_file)
        entry = str(test)

        test_string = ""
        for pc, cc, nc, in zip(entry, entry[1:], entry[2:]):
            if cc == "\'" and pc != ("[" or "{" or " ") and nc != ("]" or "}" or ":" or " "):
                test_string += "\""
            else:
                test_string += cc

        f= open(r"myfile.json", "w")
        f.write("{")
        f.write("\"entry\":")
        f.write(test_string)
        f.write("}")
        return

##### Questions:
##### gitignore .pyc
##### Test 8 restults
##### Hvad skal man teste med unit tests, hvor mange, hvad osv.
##### Program til at dække sourcekode brugt


if __name__ == "__main__":
    t3 = parcer(True, ",")
    # print(t3.parce("Hej,med,dig \n 1,2,3"))
    # print(t3.parce("name,email,department\nDavid Kim,david.kim@example.com,Engineering"))
    # print(t3.parce("name,email,department\nDavid Kim,Engineering\nJenna,jenna@gmail.com,Staff"))
    # print(parcer.split_lines("name,email,department\nDavid Kim,Engineering\nJenna,jenna@gmail.com,Staff"))
    # print(t3.split_words("Hallo,world,\"Goodbye,Universe\""))
    t3.json_converter("Hej,med,dig\n1,2,3")



