#! python3


from dataclasses import dataclass

from brispy.abstract import Trainer
from .utils import get_todays_trainer, get_todays_trainer_starts, get_todays_trainer_wins, get_todays_trainer_places, \
    get_todays_trainer_shows, get_trainer_current_year_starts, get_trainer_current_year_wins, \
    get_trainer_current_year_places, get_trainer_current_year_shows, get_trainer_current_year_roi, \
    get_trainer_previous_year_starts, get_trainer_previous_year_wins, get_trainer_previous_year_places, \
    get_trainer_previous_year_shows, get_trainer_previous_year_roi, get_trainer_key_stat_category, \
    get_trainer_key_stat_number_of_starts, get_trainer_key_stat_win_percentage, get_trainer_key_stat_itm_percentage, \
    get_trainer_key_stat_roi, \
    TrainerKeyStatNumber


@dataclass
class SingleFileTrainerKeyStat:
    category: str               # 16 characters
    number_of_starts: int       # 4 digits
    win_percentage: float       # 5 digits
    itm_percentage: float       # 5 digits
    roi: float                  # 5 digits

    @staticmethod
    def create(row: list[str], number: TrainerKeyStatNumber) -> 'SingleFileTrainerKeyStat':
        return SingleFileTrainerKeyStat(
            category=get_trainer_key_stat_category(row, number),
            number_of_starts=get_trainer_key_stat_number_of_starts(row, number),
            win_percentage=get_trainer_key_stat_win_percentage(row, number),
            itm_percentage=get_trainer_key_stat_itm_percentage(row, number),
            roi=get_trainer_key_stat_roi(row, number)
        )


@dataclass
class SingleFileTrainer(Trainer):
    name: str                                   # 30 characters
    starts: int                                 # 4 digits
    wins: int                                   # 3 digits
    places: int                                 # 3 digits
    shows: int                                  # 3 digits
    current_year_starts: int                    # 4 digits
    current_year_wins: int                      # 4 digits
    current_year_places: int                    # 4 digits
    current_year_shows: int                     # 4 digits
    current_year_roi: float                     # 6 digits
    prevous_year_starts: int                    # 4 digits
    prevous_year_wins: int                      # 4 digits
    prevous_year_places: int                    # 4 digits
    prevous_year_shows: int                     # 4 digits
    prevous_year_roi: float                     # 6 digits
    key_stats: list[SingleFileTrainerKeyStat]   # 6 key stats

    @staticmethod
    def create(row: list[str]) -> 'SingleFileTrainer':
        return SingleFileTrainer(
            name=get_todays_trainer(row),
            starts=get_todays_trainer_starts(row),
            wins=get_todays_trainer_wins(row),
            places=get_todays_trainer_places(row),
            shows=get_todays_trainer_shows(row),
            current_year_starts=get_trainer_current_year_starts(row),
            current_year_wins=get_trainer_current_year_wins(row),
            current_year_places=get_trainer_current_year_places(row),
            current_year_shows=get_trainer_current_year_shows(row),
            current_year_roi=get_trainer_current_year_roi(row),
            prevous_year_starts=get_trainer_previous_year_starts(row),
            prevous_year_wins=get_trainer_previous_year_wins(row),
            prevous_year_places=get_trainer_previous_year_places(row),
            prevous_year_shows=get_trainer_previous_year_shows(row),
            prevous_year_roi=get_trainer_previous_year_roi(row),
            key_stats=[
                SingleFileTrainerKeyStat.create(row, number) for number in TrainerKeyStatNumber
            ]
        )
