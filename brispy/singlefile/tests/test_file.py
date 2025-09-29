#! python3


from unittest import TestCase

from ..file import SingleFile


class TestSingleFile(TestCase):

    TEST_PATH = 'C:\\Users\\mathe\\OneDrive\\Documents\\horses\\gulfstream\\pps\\2025\\data\\GPX0912.drf'

    def test_create(self):
        sf = SingleFile.create(self.TEST_PATH)
        self.assertIsInstance(sf, SingleFile)
        self.assertIsNotNone(sf.rows)
        self.assertIsInstance(sf.rows, list)
