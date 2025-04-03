import unittest
import sys

sys.path.append('..')

import model
import file


class ModelTest(unittest.TestCase):

    def test_create_pdf(self):
        db = model.Model()
        file_type = file.FILE_TYPE.PDF

        parameters = {'name': 'file.pdf', 'date': '10.12.2023', 'size': 1024, 'pages': 10}
        id = db.create(file_type, **parameters)
        file_1 = db.select_by_id(id)
        file_2 = file.PDFFile(**parameters)
        self.assertEqual(file_1.get_parameters(), file_2.get_parameters())

        parameters = ['file.pdf', '10.12.2023', 1024, 10]
        id = db.create(file_type, *parameters)
        file_1 = db.select_by_id(id)
        file_2 = file.PDFFile(*parameters)
        self.assertEqual(file_1.get_parameters(), file_2.get_parameters())
    
    def test_create_png(self):
        db = model.Model()
        file_type = file.FILE_TYPE.PNG
        
        parameters = {'name': 'file.png', 'date': '10.12.2023', 'size': 1024, 'width': 100, 'height': 50}
        id = db.create(file_type, **parameters)
        file_1 = db.select_by_id(id)
        file_2 = file.PNGFile(**parameters)
        self.assertEqual(file_1.get_parameters(), file_2.get_parameters())

        parameters = ['file.pdf', '10.12.2023', 1024, 100, 50]
        id = db.create(file_type, *parameters)
        file_1 = db.select_by_id(id)
        file_2 = file.PNGFile(*parameters)
        self.assertEqual(file_1.get_parameters(), file_2.get_parameters())

    def test_wrong_create(self):
        db = model.Model()

        parameters_dict = {'name': 'file.png', 'date': '10.12.2023', 'size': 1024, 'width': 100, 'height': 50}
        parameters_list = ['file.pdf', '10.12.2023', 1024, 10]

        with self.assertRaises(AssertionError):
            db.create(*parameters_list, **parameters_dict)
            db.create(*[], **{})
            db.create(*[])
            db.create(*{})

    def test_remove(self):
        db = model.Model()
        db.remove(1000)

        file_type = file.FILE_TYPE.PDF
        parameters = {'name': 'file.pdf', 'date': '10.12.2023', 'size': 1024, 'pages': 10}

        id = db.create(file_type, **parameters)
        db.remove(id)

        with self.assertRaises(AssertionError):
            db.select_by_id(id)

    
    def test_select_by_wrong_id(self):
        db = model.Model()
        with self.assertRaises(AssertionError):
            db.select_by_id(1001)
            db.select_by_id(-1)
    
    def test_select_all(self):
        db = model.Model()
        
        file_type1 = file.FILE_TYPE.PDF
        parameters1 = {'name': 'file.png', 'date': '10.12.2023', 'size': 1024, 'pages': 10}

        file_type2 = file.FILE_TYPE.PNG
        parameters2 = {'name': 'file.png', 'date': '10.12.2023', 'size': 1024, 'width': 100, 'height': 50}

        id1 = db.create(file_type1, **parameters1)
        id2 = db.create(file_type2, **parameters2)

        result = {id1: file.PDFFile(**parameters1), id2: file.PNGFile(**parameters2)}

        for i, v in db.select_all().items():
            self.assertEqual(v.get_parameters(), result[i].get_parameters())


if __name__ == '__main__':
    unittest.main()