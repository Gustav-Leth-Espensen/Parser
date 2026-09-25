# Parser
Exercise week 2 spcialisterne, reformat af CSV file to another datastructure

# Description
Programmet består af en class parser og en class reader. Reader bliver brugt til at importere csv filer så de kan læses af parser. Denne class er ikke gennemtestet.

Parser class består af 5 functioner. split_lines og split_words er private funktioner som spliiter heldholdvis linjer og ord op i lister. parce funktionen laver tjekker for fejl i input og kalder derefter split_lines og split_words. Hvis der er en header laver den filen om til at en liste af dictionaries ellers laver den det til en liste af lister. 
json_converter konverterer outputtet fra parce functionen om til en string som passer med json fil formattet. create_json_file laver outputtet fra json_converter om til en reel json fil.

Programmet er blevet test med 14 unittest fra filen test.py ved hjælp af pakken unittest. 

Unittest dækker 100% af kildekoden. Disse test er blevet lavet ved hjælp af uv vituel environment og den indbyggede funktion uv coverage.

# UML diagram
![Activity diagram](https://github.com/Gustav-Leth-Espensen/Parser/blob/main/uml_diagrams/parser_activity_dia.png)

# Getting Started
## Dependencies 
Version Python 3.13.15 \
coverage 7.16.1

# Executing program
Create an object \
`example = parser(header = True, seperator = "," = quotation_sign = "\"")` \
run the parser \
`example.create_json_file(("header1,header2,header3\nitem1,item2,item3"), "example")`


# Authors
Gustav Leth-Espensen gustavle@hotmail.com

# Version History
*0.1
- Initial handin


