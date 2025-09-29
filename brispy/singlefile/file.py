#! python3


import csv
from dataclasses import dataclass
import os

from brispy.abstract import DataFile
from .row import SingleFileRow


@dataclass
class SingleFile(DataFile):
    rows: list[SingleFileRow]

    @staticmethod
    def create(path: str) -> 'SingleFile':
        if not os.path.exists(path):
            raise FileNotFoundError(f'file {path} does not exist')
        with open(path) as f:
            reader = csv.reader(f)
            rows: list[SingleFileRow] = []
            for row in reader:
                rows.append(SingleFileRow.create(row))
            return SingleFile(rows=rows)
