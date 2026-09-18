
class parser():

    def __init__(self, header: bool, seperator = ",", quotation_sign = "\""):
        self.header = header
        self.seperator = seperator
        self.quotation_sign = quotation_sign

    #### \r is only newline on windows, otherwise it moves the curser to the start of current line
    #### Hvad var ideen med den nye newline function?
    def split_lines(csv_text: str):
        lines = []
        newline = 0
        for i in range(len(csv_text)):
            if csv_text[i] == ("\n" or "\r"):
                lines.append(csv_text[newline:i])
                newline = i + 1
            if i == len(csv_text) - 1:
                lines.append(csv_text[newline:i+1])

        return lines

    #### isnewline():


    #### Change seperator from , to self.seperator
    def split_words(self, csv_text: str):
        split_to_words = []
        newword = 0
        inbetween = False
        for i in range(len(csv_text)):
            if csv_text[i] == self.quotation_sign:
                inbetween = not inbetween
            if csv_text[i] == self.seperator and inbetween != True:
                split_to_words.append(csv_text[newword:i])
                newword = i + 1
            if i == len(csv_text) - 1:
                split_to_words.append(csv_text[newword:i+1])
                
        return split_to_words


    def parce(self, csv_text: str):
        if csv_text == "":
            return "This is an empty string"
        line_split = parser.split_lines(csv_text)

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

    def json_converter(self, csv_file: str, file_name: str):
        #### int/float skal ikke have ""
        #### nul skal ikke have ""

        parced_text = self.parce(csv_file)
        parced_text_as_str = str(parced_text)

        if parced_text == "Needs at least two lines with header.":
            return "Needs at least two lines with header."

        json_input = ""
        for pc, cc, nc, in zip(parced_text_as_str, parced_text_as_str[1:], parced_text_as_str[2:]):
            if cc == "\'" and (pc in ("[", "{", " ", ",") or nc in ("]", "}", ":", " ", ",")):
                json_input += "\""
            else:
                json_input += cc

        f = open(f"{file_name}.json", "w")
        f.write(json_input)

        return

##### Questions:
##### gitignore .pyc
##### Hvad skal man teste med unit tests, hvor mange, hvad osv.


if __name__ == "__main__":
    t3 = parser(True, ",")
    # print(t3.parce("Hej,med,dig \n 1,2,3"))
    # print(t3.parce("name,email,department\nDavid Kim,david.kim@example.com,Engineering"))
    # print(t3.parce("name,email,department\nDavid Kim,Engineering\nJenna,jenna@gmail.com,Staff"))
    # print(parcer.split_lines("name,email,department\nDavid Kim,Engineering\nJenna,jenna@gmail.com,Staff"))
    # print(t3.split_words("Hallo,world,\"Goodbye,Universe\""))
    # t3.json_converter("O\'Brian,med,dig\n1,2,3", "")
    t4 = parser(False)
    print(t3.json_converter("O\'Brian,med,dig", "test1"))
    t4.json_converter("O\'Brian,med,dig", "test")


