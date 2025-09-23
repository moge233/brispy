#! python3


import csv
import os

from brispy.abstract import DataFile
from .row import SingleFileRow


class SingleFile(DataFile):
    def __init__(self, rows=None):
        super().__init__()
        self.rows: list[SingleFileRow] | None = rows

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFile({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFile({ret[:-2]})'

    @staticmethod
    def create(path: str) -> 'SingleFile':
        if not os.path.exists(path):
            raise FileNotFoundError(f'file {path} does not exist')
        with open(path) as f:
            reader = csv.reader(f)
            rows: list[SingleFileRow] = []
            for row in reader:
                rows.append(SingleFileRow.create(row))
            return SingleFile(rows)
