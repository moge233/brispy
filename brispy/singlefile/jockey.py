#! python3


from abstract import Jockey
from .utils import get_apprentice_weight_allowed, get_todays_jockey, get_todays_jockey_starts, get_todays_jockey_wins, \
    get_todays_jockey_places, get_todays_jockey_shows, get_jockey_current_year_starts, get_jockey_current_year_wins, \
    get_jockey_current_year_places, get_jockey_current_year_shows, get_jockey_current_year_roi, \
    get_jockey_previous_year_starts, get_jockey_previous_year_wins, get_jockey_previous_year_places, \
    get_jockey_previous_year_shows, get_jockey_previous_year_roi


class SingleFileJockey(Jockey):
    def __init__(self, name: str, apprentice_weight_allowed: int, starts: int, wins: int, places: int, shows: int,
                 current_year_starts: int, current_year_wins: int, current_year_places: int, current_year_shows: int,
                 current_year_roi: float, preivous_year_starts: int, previous_year_wins: int, previous_year_places: int,
                 previous_year_shows: int, previous_year_roi: float):
        super().__init__()
        self.name: str = name
        self.apprentice_weight_allowed: int = apprentice_weight_allowed
        self.starts: int = starts
        self.wins: int = wins
        self.place: int = places
        self.shows: int = shows
        self.current_year_starts: int = current_year_starts
        self.current_year_wins: int = current_year_wins
        self.current_year_places: int = current_year_places
        self.current_year_shows: int = current_year_shows
        self.current_year_roi: float = current_year_roi
        self.preivous_year_starts: int = preivous_year_starts
        self.previous_year_wins: int = previous_year_wins
        self.previous_year_places: int = previous_year_places
        self.previous_year_shows: int = previous_year_shows
        self.previous_year_roi: float = previous_year_roi

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileJockey({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileJockey({ret[:-2]})'

    @staticmethod
    def create(row: list[str]) -> 'SingleFileJockey':
        return SingleFileJockey(
            get_todays_jockey(row),
            get_apprentice_weight_allowed(row),
            get_todays_jockey_starts(row),
            get_todays_jockey_wins(row),
            get_todays_jockey_places(row),
            get_todays_jockey_shows(row),
            get_jockey_current_year_starts(row),
            get_jockey_current_year_wins(row),
            get_jockey_current_year_places(row),
            get_jockey_current_year_shows(row),
            get_jockey_current_year_roi(row),
            get_jockey_previous_year_starts(row),
            get_jockey_previous_year_wins(row),
            get_jockey_previous_year_places(row),
            get_jockey_previous_year_shows(row),
            get_jockey_previous_year_roi(row)
        )
