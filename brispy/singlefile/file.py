#! python3


import csv
from dataclasses import dataclass
import os

from brispy.abstract import DataFile
from .row import SingleFileRow
from .utils import FieldError


@dataclass
class SingleFile(DataFile):
    rows: list[SingleFileRow]

    @staticmethod
    def create(path: str) -> 'SingleFile':
        if not os.path.exists(path):
            raise FileNotFoundError(f'file {path} does not exist')
        with open(path, encoding='latin-1', newline='') as f:
            reader = csv.reader(f)
            rows: list[SingleFileRow] = []
            for number, row in enumerate(reader, 1):
                try:
                    rows.append(SingleFileRow.create(row))
                except FieldError as error:
                    raise error.at(path, number) from None
            return SingleFile(rows=rows)
