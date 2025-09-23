#! python3


from brispy.abstract import Owner
from .utils import get_todays_owner, get_owners_silks


class SingleFileOwner(Owner):
    def __init__(self, name: str, silks: str):
        super().__init__()
        self.name = name
        self.silks = silks

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileOwner({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileOwner({ret[:-2]})'

    @staticmethod
    def create(row: list[str]) -> 'SingleFileOwner':
        return SingleFileOwner(
            get_todays_owner(row),
            get_owners_silks(row)
        )
