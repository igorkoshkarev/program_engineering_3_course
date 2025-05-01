import sys
import csv
from csvvalidator import *
from file import FILE_TYPE


class FileCSVValidator(CSVValidator):
    FIELD_NAMES = ('type','name','date','size')
    
    def __init__(self, field_names=None):
        super().__init__(self.FIELD_NAMES)
        self.add_header_check('EX1', 'bad header')
        self.add_record_length_check('EX2', 'unexpected record length')
        self.add_value_check('type', enumeration(FILE_TYPE.get_all_string_types()),
                                'EX3', f'file type must be one of this: {FILE_TYPE.get_all_string_types()}')
        self.add_value_check('date', int,
                                'EX4', 'invalid date')
        self.add_value_check('size', int,
                                'EX5', 'invalid size')
        self.add_record_check(self.check_negative_size_and_date)

    def check_negative_size_and_date(self, r):
        date = int(r['date'])
        size = int(r['size'])
        if date < 0:
            raise RecordError('EX6', 'negative values in date')
        if size < 0:
            raise RecordError('EX7', 'negative values in size')



if __name__ == '__main__':
    with open('./1.csv', 'r', newline='') as f:
        data = csv.reader(f, delimiter=',')
        validator = FileCSVValidator()
        problems = validator.validate(data)
        print(problems)