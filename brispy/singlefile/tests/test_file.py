#! python3


import csv
import os
import tempfile
from unittest import TestCase

from brispy.singlefile import FieldError
from brispy.singlefile.file import SingleFile
from .rowbuilder import build_row


class TestSingleFile(TestCase):

    TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TESTDRF.DRF')

    @classmethod
    def setUpClass(cls):
        cls.sf = SingleFile.create(cls.TEST_PATH)

    def test_create(self):
        self.assertIsInstance(self.sf, SingleFile)
        self.assertIsNotNone(self.sf.rows)
        self.assertIsInstance(self.sf.rows, list)

    def test_rows_parsed(self):
        self.assertGreater(len(self.sf.rows), 0)
        self.assertEqual(len(self.sf.rows[0].horse.past_performances), 10)

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            SingleFile.create(os.path.join(os.path.dirname(self.TEST_PATH), 'missing.DRF'))


class TestSingleFileErrors(TestCase):

    def write(self, rows):
        handle = tempfile.NamedTemporaryFile('w', suffix='.DRF', delete=False, encoding='latin-1', newline='')
        with handle:
            csv.writer(handle).writerows(rows)
        self.addCleanup(os.remove, handle.name)
        return handle.name

    def test_error_names_file_and_row(self):
        path = self.write([build_row('7'), build_row('7', PURSE='lots')])
        with self.assertRaises(FieldError) as raised:
            SingleFile.create(path)
        self.assertEqual((raised.exception.path, raised.exception.row), (path, 2))
        self.assertIn(f"{path}: row 2: field 12 (PURSE): 'lots' is not a valid integer", str(raised.exception))

    def test_latin1_names(self):
        path = self.write([build_row('7', HORSE_NAME='Señor Ré')])
        self.assertEqual(SingleFile.create(path).rows[0].horse.name, 'Señor Ré')
