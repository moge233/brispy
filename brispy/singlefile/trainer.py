#! python3


from brispy.abstract import Trainer
from .utils import get_todays_trainer, get_todays_trainer_starts, get_todays_trainer_wins, get_todays_trainer_places, \
    get_todays_trainer_shows, get_trainer_current_year_starts, get_trainer_current_year_wins, \
    get_trainer_current_year_places, get_trainer_current_year_shows, get_trainer_current_year_roi, \
    get_trainer_previous_year_starts, get_trainer_previous_year_wins, get_trainer_previous_year_places, \
    get_trainer_previous_year_shows, get_trainer_previous_year_roi


class SingleFileTrainer(Trainer):
    def __init__(self, name: str, starts: int, wins: int, places: int, shows: int,
                 current_year_starts: int, current_year_wins: int, current_year_places: int,
                 current_year_shows: int, current_year_roi: float,
                 previous_year_starts: int, previous_year_wins: int, previous_year_places: int,
                 previous_year_shows: int, previous_year_roi: float):
        super().__init__()
        self.name: str = name                                   # 30 characters
        self.starts: int = starts                               # 4 digits
        self.wins: int = wins                                   # 3 digits
        self.places: int = places                               # 3 digits
        self.shows: int = shows                                 # 3 digits
        self.current_year_starts: int = current_year_starts     # 4 digits
        self.current_year_wins: int = current_year_wins         # 4 digits
        self.current_year_places: int = current_year_places     # 4 digits
        self.current_year_shows: int = current_year_shows       # 4 digits
        self.current_year_roi: float = current_year_roi         # 6 digits
        self.prevous_year_starts: int = previous_year_starts    # 4 digits
        self.prevous_year_wins: int = previous_year_wins        # 4 digits
        self.prevous_year_places: int = previous_year_places    # 4 digits
        self.prevous_year_shows: int = previous_year_shows      # 4 digits
        self.prevous_year_roi: float = previous_year_roi        # 6 digits

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileTrainer({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileTrainer({ret[:-2]})'

    @staticmethod
    def create(row: list[str]) -> 'SingleFileTrainer':
        return SingleFileTrainer(
            get_todays_trainer(row),
            get_todays_trainer_starts(row),
            get_todays_trainer_wins(row),
            get_todays_trainer_places(row),
            get_todays_trainer_shows(row),
            get_trainer_current_year_starts(row),
            get_trainer_current_year_wins(row),
            get_trainer_current_year_places(row),
            get_trainer_current_year_shows(row),
            get_trainer_current_year_roi(row),
            get_trainer_previous_year_starts(row),
            get_trainer_previous_year_wins(row),
            get_trainer_previous_year_places(row),
            get_trainer_previous_year_shows(row),
            get_trainer_previous_year_roi(row),
        )
