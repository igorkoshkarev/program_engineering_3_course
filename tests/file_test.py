import unittest
import sys

sys.path.append('..')

import file


class FileTest(unittest.TestCase):

    def test_get_parameters(self):
        parameters = {'name': 'name.pdf', 'date': '10.10.2003', 'size': 1024, 'pages': 100}
        f = file.PDFFile(**parameters)
        self.assertEqual(f.get_parameters(), ['pdf', 'name.pdf', '10.10.2003', 1024, 100])

        parameters = {'name': 'name.png', 'date': '10.10.2003', 'size': 1024, 'width': 100, 'height': 50}
        f = file.PNGFile(**parameters)
        self.assertEqual(f.get_parameters(), ['png', 'name.png', '10.10.2003', 1024, 100, 50])

    def test_get_class_by_name(self):
        self.assertEqual(file.FILE_TYPE.PDF, file.FILE_TYPE.get_type_on_name('pdf'))
        self.assertEqual(file.FILE_TYPE.PNG, file.FILE_TYPE.get_type_on_name('png'))
        with self.assertRaises(AssertionError):
            file.FILE_TYPE.get_type_on_name('PNG')
            file.FILE_TYPE.get_type_on_name('none')

if __name__ == '__main__':
    unittest.main()