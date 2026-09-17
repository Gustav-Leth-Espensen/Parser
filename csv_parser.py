
class parcer():

    def __init__(self, header: bool, seperator = ","):
        self.header = header
        self.seperator = seperator

    def parce(self, csv_text: str):
        if csv_text == "":
            return "This is an empty string"
        line_split = csv_text.splitlines()
        file_in_words = []
        for i in range(len(line_split)):
            file_in_words.append(line_split[i].split(self.seperator))

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


if __name__ == "__main__":
    t3 = parcer(True, ",")
    print(t3.parce("Hej,med,dig \n 1,2,3"))
    print(t3.parce("name,email,department\nDavid Kim,david.kim@example.com,Engineering"))