import unittest
import sys
import csv

sys.path.append('..')

from csv_validator import FileCSVValidator


class CSVValidatorTest(unittest.TestCase):
    def test_correct_csv(self):
        validator = FileCSVValidator()
        with open('./test_csv/correct_csv.csv', newline='') as f:
            self.assertEqual(validator.validate(csv.reader(f)), [])
    
    def test_invalid_header(self):
        validator = FileCSVValidator()
        with open('./test_csv/invalid_header.csv', newline='') as f:
            self.assertEqual(validator.validate(csv.reader(f))[0]['code'], 'EX1')
        
        with open('./test_csv/invalid_rows_2.csv', newline='') as f:
            self.assertEqual(validator.validate(csv.reader(f))[0]['code'], 'EX1')
    
    def test_invalid_row_type(self):
        validator = FileCSVValidator()
        with open('./test_csv/invalid_type.csv', newline='') as f:
            self.assertEqual(validator.validate(csv.reader(f))[0]['code'], 'EX3')
        
        with open('./test_csv/invalid_date.csv', newline='') as f:
            self.assertEqual(validator.validate(csv.reader(f))[0]['code'], 'EX6')
        
        with open('./test_csv/invalid_size.csv', newline='') as f:
            self.assertEqual(validator.validate(csv.reader(f))[0]['code'], 'EX7')

if __name__ == '__main__':
    unittest.main()