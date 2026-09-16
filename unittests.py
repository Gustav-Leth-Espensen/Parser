import unittest
import parser


#### test input 1 is emptry file
#### test input 2 is three rows of empleyees with header
#### test input 3 is three rows of empleyees without header
#### test input 4 is txt document
#### test input 5 is missing values within ,,
#### test input 6 is missing values and the ,,


class test_parser(unittest.TestCase):

#     def test_initial_checks(self):
#         self.assertEqual(parser.Parcer(r'C:\Users\SPAC-B-16\GLE_Special\Opgaver\Parser\tests', ).initial_checks(), "")


    def test(self):
        self.assertEqual(parser.Parcer.new_data_format("Hej, med ,det", "ewpoiruw3o eit5u"))
        self.assertEqual(parser.Parcer.new_data_format("\"hej,\"sa, med ,det", "ewpoiruw3o eit5u"))
        

if __name__ == '__main__':
    unittest.main()