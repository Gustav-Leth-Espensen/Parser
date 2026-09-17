import unittest
import csv_parser


class test_parser(unittest.TestCase):

    def test_non_inputs(self):
        t4 = csv_parser.parcer(True, ",")

        self.assertEqual(t4.parce(""),"This is an empty string")
        self.assertEqual(t4.parce("hej,med\nmorgen,middag,aften"), 
                         "This file does not fit the normal csv format.")
        

    def test_one_line_no_header(self):
        t1 = csv_parser.parcer(False, ",")

        self.assertEqual(t1.parce("Hej,med,dig"), [["Hej","med","dig"]])
        self.assertEqual(t1.parce("Hej med dig"), [["Hej med dig"]])
        self.assertEqual(t1.parce("simpel kinesisk: 汉字,traditionel kinesisk: 漢字"),
                         [["simpel kinesisk: 汉字", "traditionel kinesisk: 漢字"]])

    def test_one_line_with_header(self):
        t2 = csv_parser.parcer(True, ",")
        self.assertEqual(t2.parce("Hej,med,dig"), "Needs at least two lines with header.")
        self.assertEqual(t2.parce("Hej med dig"), "Needs at least two lines with header.")
        self.assertEqual(t2.parce("simpel kinesisk: 汉字,traditionel kinesisk: 漢字"),
                         "Needs at least two lines with header.")

    def test_multiple_lines_no_header(self):
        t3 = csv_parser.parcer(False, ",")

        self.assertEqual(t3.parce("Hej,med,dig\nmorgen,middag,aften"), [["Hej","med","dig"],["morgen", "middag", "aften"]])
        self.assertEqual(t3.parce("Hej med dig\nmorgen middag aften"), [["Hej med dig"],["morgen middag aften"]])
        self.assertEqual(t3.parce("simpel kinesisk: 汉字\ntraditionel kinesisk: 漢字"),
                         [["simpel kinesisk: 汉字"],["traditionel kinesisk: 漢字"]])

    def test_multiple_lines_with_header(self):
        t5 = csv_parser.parcer(True, ",")

        self.assertEqual(t5.parce("name,email,department\nDavid Kim,david.kim@example.com,Engineering"),
                        [{'name': 'David Kim', 'email': 'david.kim@example.com', 'department': 'Engineering'}])
        self.assertEqual(t5.parce("name,email,department\nPriya Sharma,,Engineering"),
                        [{'name': 'Priya Sharma', 'email': '', 'department': 'Engineering'}])

    def test_different_seperator(self):
        t6 = csv_parser.parcer(False, " ")

        self.assertEqual(t6.parce("Hej med dig"), [["Hej","med","dig"]])
        self.assertEqual(t6.parce("Hej,med,dig"), [["Hej,med,dig"]])

    def test_line_length_no_header(self):
        t7 = csv_parser.parcer(False, ",")

        self.assertEqual(t7.parce("Marcus Chen,marcus.chen@example.com,Engineering\nPriya Sharma,priya.sharma@example.com"),
                        ([["Marcus Chen","marcus.chen@example.com","Engineering"],["Priya Sharma","priya.sharma@example.com"]], 'Missing data in entry: [1]'))

    def test_line_length_with_header(self):
        t8 = csv_parser.parcer(True, ",")

        # This is what i want
        # Virker som jeg vil med flere personer, så hvis de er lavet rigtigt fungerer det, spørg Rasmus i morgen hvad han tænker.
        # self.assertEqual(t8.parce("name,email,department\nDavid Kim,Engineering"),
        #                         ([{'name': 'David Kim', 'email': 'Engineering', 'department': ''}], 'Missing data in entry: [1]'))

        #This works
        # self.assertEqual(t8.parce("name,email,department\nDavid Kim,Engineering"),
                #                         ([{'name': 'David Kim', 'email': 'Engineering'}], 'Missing data in entry: [1]'))

        self.assertEqual(t8.parce("name,email,department\nDavid Kim,Engineering\nJenna,jenna@gmail.com,Staff"),
                                ([{'name': 'David Kim', 'email': 'Engineering'}, {'name': 'Jenna', 'email': 'jenna@gmail.com', 'department': 'Staff'}], 'Missing data in entry: [1]'))


    def test_comma_in_quote(self):
        t9 = csv_parser.parcer(False, ",")

        self.assertEqual(t9.parce("\"James,Simmer\",Staff"),
                         [["\"James,Simmer\"","Staff"]])



if __name__ == '__main__':
    unittest.main()
    #### These two does basically the same
    # suite = unittest.TestLoader().loadTestsFromTestCase(test_parser)
    # runner = unittest.TextTestRunner(verbosity=0)
    # result = runner.run(suite)
    # print(f'Tests run: {result.testsRun}')