#! python3


from unittest import TestCase

from ..file import SingleFile
from ..row import SingleFileRow


class TestSingleFile(TestCase):

    TEST_PATH = 'C:\\Users\\mathe\\OneDrive\\Documents\\horses\\gulfstream\\pps\\data\\2025\\GPX0912.drf'

    def test_create(self):
        sf = SingleFile.create(self.TEST_PATH)
        if sf.rows:
            row: SingleFileRow = sf.rows[0]
            self.assertEqual(row.track, 'GP')
