#! python3


import os
from unittest import TestCase

from brispy.singlefile.file import SingleFile


class TestSingleFileHorse(TestCase):

    TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TESTDRF.drf')

    @classmethod
    def setUpClass(cls):
        cls.sf = SingleFile.create(cls.TEST_PATH)

    def test_row_horse(self):
        row = self.sf.rows[0]
        horse = row.horse
        self.assertIsNotNone(horse)
        self.assertIsNotNone(horse.name)
        self.assertIsInstance(horse.name, str)
