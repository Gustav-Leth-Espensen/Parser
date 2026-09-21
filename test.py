import unittest
import csv_parser
import pathlib as pl

class test_parser(unittest.TestCase):

    def test_non_inputs(self):
        t4 = csv_parser.parser(True, ",", "\"")
        self.assertEqual(t4.parce(""),"This is an empty string")
        self.assertEqual(t4.parce("hej,med\nmorgen,middag,aften"), 
                         "This file does not fit the normal csv format.")
        
    def test_one_line_no_header(self):
        t1 = csv_parser.parser(False, ",")
        self.assertEqual(t1.parce("Hej,med,dig"), [["Hej","med","dig"]])
        self.assertEqual(t1.parce("Hej med dig"), [["Hej med dig"]])
        self.assertEqual(t1.parce("simpel kinesisk: 汉字,traditionel kinesisk: 漢字"),
                         [["simpel kinesisk: 汉字", "traditionel kinesisk: 漢字"]])

    def test_one_line_with_header(self):
        t2 = csv_parser.parser(True, ",")
        self.assertEqual(t2.parce("Hej,med,dig"), "Needs at least two lines with header.")
        self.assertEqual(t2.parce("Hej med dig"), "Needs at least two lines with header.")
        self.assertEqual(t2.parce("simpel kinesisk: 汉字,traditionel kinesisk: 漢字"),
                         "Needs at least two lines with header.")

    def test_multiple_lines_no_header(self):
        t3 = csv_parser.parser(False, ",")
        self.assertEqual(t3.parce("Hej,med,dig\nmorgen,middag,aften"), [["Hej","med","dig"],["morgen", "middag", "aften"]])
        self.assertEqual(t3.parce("Hej med dig\nmorgen middag aften"), [["Hej med dig"],["morgen middag aften"]])
        self.assertEqual(t3.parce("simpel kinesisk: 汉字\ntraditionel kinesisk: 漢字"),
                         [["simpel kinesisk: 汉字"],["traditionel kinesisk: 漢字"]])

    def test_multiple_lines_with_header(self):
        t5 = csv_parser.parser(True, ",")
        self.assertEqual(t5.parce("name,email,department\nDavid Kim,david.kim@example.com,Engineering"),
                        [{'name': 'David Kim', 'email': 'david.kim@example.com', 'department': 'Engineering'}])
        self.assertEqual(t5.parce("name,email,department\nPriya Sharma,,Engineering"),
                        [{'name': 'Priya Sharma', 'email': '', 'department': 'Engineering'}])

    def test_different_seperator(self):
        t6 = csv_parser.parser(False, " ")
        self.assertEqual(t6.parce("Hej med dig"), [["Hej","med","dig"]])
        self.assertEqual(t6.parce("Hej,med,dig"), [["Hej,med,dig"]])

    def test_line_length_no_header(self):
        t7 = csv_parser.parser(False, ",")
        self.assertEqual(t7.parce("Marcus Chen,marcus.chen@example.com,Engineering\nPriya Sharma,priya.sharma@example.com"),
                        ([["Marcus Chen","marcus.chen@example.com","Engineering"],["Priya Sharma","priya.sharma@example.com"]], 'Missing data in entry: [1]'))

    def test_line_length_with_header(self):
        t8 = csv_parser.parser(True, ",")
        self.assertEqual(t8.parce("name,email,department\nDavid Kim,Engineering"),
                                  ([{'name': 'David Kim', 'email': 'Engineering'}], 'Missing data in entry: [1]'))

        self.assertEqual(t8.parce("name,email,department\nDavid Kim,Engineering\nJenna,jenna@gmail.com,Staff"),
                                ([{'name': 'David Kim', 'email': 'Engineering'}, {'name': 'Jenna', 'email': 'jenna@gmail.com', 'department': 'Staff'}], 'Missing data in entry: [1]'))


    def test_comma_in_quote(self):
        t9 = csv_parser.parser(False, ",")
        self.assertEqual(t9.parce("\"James,Simmer\",Staff"),
                         [["\"James,Simmer\"","Staff"]])
        self.assertEqual(t9.parce("\"James,Simmer\",Staff\n\'Katy,Kast\' Engineer"),
                         [["\"James,Simmer\"","Staff"],["\'Katy","Kast\' Engineer"]])

    def test_different_quotation_signs(self):
        t10 = csv_parser.parser(False, ",", "\'")
        self.assertEqual(t10.parce("\"James,Simmer\",Staff\n\'Katy,Kast\' Engineer"),
                         ([["\"James","Simmer\"","Staff"],["\'Katy,Kast\' Engineer"]], 'Missing data in entry: [1]'))


    def test_double_quote_inside(self):
        t11 = csv_parser.parser(False)
        self.assertEqual(t11.parce("Hej,med"",dig"), [["Hej","med","dig"]])

    def test_new_line_within_quote(self):
        t12 = csv_parser.parser(False)
        self.assertEqual(t12.parce("\"Hej\",\"test\ntest\",\"dig\""), [["\"Hej\"","\"test\ntest\"","\"dig\""]])

    def test_json(self):
        t11 = csv_parser.parser(False)

        input = t11._parser__json_converter("Hej,med,dig")
        expected = '["Hej", "med", "dig"]'
        self.assertEqual(input,expected)

    def test_jason_header_one_line(self):
        t12 = csv_parser.parser(True)

        input = t12._parser__json_converter("Hej,med,dig")
        expected = "Needs at least two lines with header."
        self.assertEqual(input,expected)

        input1 = t12.create_json_file("Hej,med,dig", "test1")
        expected1 = "Needs at least two lines with header."
        self.assertEqual(input1,expected1)


    def test_jason_header(self):
        t13 = csv_parser.parser(True)

        input = t13._parser__json_converter("O\'Brian,med,dig\n1,2,3")
        expected = '{"O\'Brian": "1", "med": "2", "dig": "3"}'
        self.assertEqual(input,expected)

    def test_json_file_exists(self):
        t14 = csv_parser.parser(True)

        t14.create_json_file("O\'Brian,med,dig\n1,2,3", "test14")
        path = pl.Path("test14.json")
        self.assertEqual((str(path), path.is_file()), (str(path), True))
        path.unlink()

if __name__ == '__main__': #pragma: no cover
    unittest.main()
    #### These two does basically the same
    # suite = unittest.TestLoader().loadTestsFromTestCase(test_parser)
    # runner = unittest.TextTestRunner(verbosity=0)
    # result = runner.run(suite)
    # print(f'Tests run: {result.testsRun}')

####    deactive ####går ud af uv
####    .venv\Scripts\activate ### for at komme ind igen
####    coverage html
####    coverage run -m unittest discover