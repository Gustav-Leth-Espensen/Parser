
class parser():

    def __init__(self, header: bool, seperator = ",", quotation_sign = "\""):
        self.header = header
        self.seperator = seperator
        self.quotation_sign = quotation_sign

    #### \r is only newline on windows, otherwise it moves the curser to the start of current line
    #### Hvad var ideen med den nye newline function?
    def __split_lines(self, csv_text: str):
        lines = []
        newline = 0
        inbetween_quote = False
        for i in range(len(csv_text)):
            if csv_text[i] == self.quotation_sign:
                inbetween_quote = not inbetween_quote
            if csv_text[i] == ("\n") and inbetween_quote != True:
                ### \n or \r in python, how do we make sure no error
                lines.append(csv_text[newline:i])
                newline = i + 1
            if i == len(csv_text) - 1:
                lines.append(csv_text[newline:i+1])

        return lines

    #### isnewline():

    def __split_words(self, csv_text: str):
        split_to_words = []
        newword = 0
        inbetween_quote = False
        for i in range(len(csv_text)):
            if csv_text[i] == self.quotation_sign:
                inbetween_quote = not inbetween_quote
            if csv_text[i] == self.seperator and inbetween_quote != True:
                split_to_words.append(csv_text[newword:i])
                newword = i + 1
            if i == len(csv_text) - 1:
                split_to_words.append(csv_text[newword:i+1])
                
        return split_to_words


    def parse(self, csv_text: str):
        if csv_text == "":
            return "This is an empty string"
        line_split = self.__split_lines(csv_text)

        file_in_words = []
      
        for i in range(len(line_split)):
            file_in_words.append(self.__split_words(line_split[i]))

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

    def __json_converter(self, csv_file: str):
        #### int/float skal ikke have ""
        #### nul skal ikke have ""

        parsed_text = self.parse(csv_file)
        parsed_text_as_str = str(parsed_text)

        if parsed_text == "Needs at least two lines with header.":
            return parsed_text

        json_input = ""
        for pc, cc, nc, in zip(parsed_text_as_str, parsed_text_as_str[1:], parsed_text_as_str[2:]):
            if cc == "\'" and (pc in ("[", "{", " ", ",") or nc in ("]", "}", ":", " ", ",")):
                json_input += "\""
            else:
                json_input += cc

        return json_input

    def create_json_file(self, csv_file: str, file_name: str):
        json_format = self.__json_converter(csv_file)
        print(json_format)
        if json_format == "Needs at least two lines with header.":
            return json_format
        f = open(f"{file_name}.json", "w")
        f.write("[")
        f.write(json_format)
        f.write("]")
        ### I STEDET FOR DET TO ENKELT WRITE STATEMENTS SÅ ÆDNRER DEN I LOOPET DER LAVER JSON FORMATET I __josn_converter
        
        return

##### Questions:
##### gitignore .pyc
##### Hvad skal man teste med unit tests, hvor mange, hvad osv.


# if __name__ == "__main__":
    # t3 = parser(True, ",")
    # print(t3.parse("Hej,med,dig \n 1,2,3"))
    # print(t3.parse("name,email,department\nDavid Kim,david.kim@example.com,Engineering"))
    # print(t3.parse("name,email,department\nDavid Kim,Engineering\nJenna,jenna@gmail.com,Staff"))
    # # print(parser.split_lines("name,email,department\nDavid Kim,Engineering\nJenna,jenna@gmail.com,Staff"))
    # print(t3.split_words("Hallo,world,\"Goodbye,Universe\""))
    # t3.json_converter("O\'Brian,med,dig\n1,2,3")
    # t4 = parser(False)
    # print(t3.json_converter("O\'Brian,med,dig", "test1"))
    # t4.json_converter("O\'Brian,med,dig", "test")
    # t4.create_json_file("Hej,med,dig", "test1")
    # print("Hej med""ig")


    # example = parser(True, ",", "\"")
    # print(example.parse("name,email,department\n" \
    #                     "Marcus Chen,marcus.chen@example.com,Engineering\n" \
    #                     "Priya Sharma,priya.sharma@example.com,Engineering"))






    # example.create_json_file(("name,email,department\n" \
    #                     "Marcus Chen,marcus.chen@example.com,Engineering\n" \
    #                     "Priya Sharma,priya.sharma@example.com,Engineering"), "example")



