#! python3


from dataclasses import dataclass

from brispy.abstract import Owner
from .utils import get_todays_owner, get_owners_silks


@dataclass
class SingleFileOwner(Owner):
    name: str
    silks: str

    @staticmethod
    def create(row: list[str]) -> 'SingleFileOwner':
        return SingleFileOwner(
            name=get_todays_owner(row),
            silks=get_owners_silks(row)
        )
