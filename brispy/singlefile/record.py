#! python3


from dataclasses import dataclass


@dataclass
class SingleFileRecord:
    starts: int
    wins: int
    places: int
    shows: int
    earnings: int


@dataclass
class SingleFileRecordWithYear(SingleFileRecord):
    year: int
