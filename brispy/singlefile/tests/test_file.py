#! python3


import os
from unittest import TestCase

from brispy.singlefile.file import SingleFile


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
