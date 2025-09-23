#! python3


class SingleFileRecord:
    def __init__(self, starts: int, wins: int, places: int, shows: int, earnings: int):
        self.starts: int = starts
        self.wins: int = wins
        self.places: int = places
        self.shows: int = shows
        self.earnings: int = earnings

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileHorseRecord({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileHorseRecord({ret[:-2]})'


class SingleFileRecordWithYear(SingleFileRecord):
    def __init__(self, starts: int, wins: int, places: int, shows: int, earnings: int, year: int):
        super().__init__(starts, wins, places, shows, earnings)
        self.year = year

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileRecordWithYear({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileRecordWithYear({ret[:-2]})'
