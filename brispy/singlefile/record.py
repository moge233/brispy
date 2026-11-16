#! python3


from dataclasses import dataclass


@dataclass
class SingleFileRecord:
    starts: int | None
    wins: int | None
    places: int | None
    shows: int | None
    earnings: int | None


@dataclass
class SingleFileRecordWithYear(SingleFileRecord):
    year: int | None
