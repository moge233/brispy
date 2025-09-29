#! python3


from dataclasses import dataclass

from .utils import get_trainer_jockey_combo_starts, \
    get_trainer_jockey_combo_wins, get_trainer_jockey_combo_places, get_trainer_jockey_combo_shows, \
    get_trainer_jockey_combo_roi, get_trainer_jockey_combo_meet_starts, get_trainer_jockey_combo_meet_wins, \
    get_trainer_jockey_combo_meet_places, get_trainer_jockey_combo_meet_shows, get_trainer_jockey_combo_meet_roi


@dataclass
class SingleFileTrainerJockeyCombo:
    lifetime_starts: int                    # 4 digits
    lifetime_wins: int                      # 4 digits
    lifetime_places: int                    # 4 digits
    lifetime_shows: int                     # 4 digits
    lifetime_roi: int                       # 4 digits
    meet_starts: int                        # 4 digits
    meet_wins: int                          # 4 digits
    meet_places: int                        # 4 digits
    meet_shows: int                         # 4 digits
    meet_roi: float                         # 6 digits

    @staticmethod
    def create(row: list[str]) -> 'SingleFileTrainerJockeyCombo':
        return SingleFileTrainerJockeyCombo(
            lifetime_starts=get_trainer_jockey_combo_starts(row),
            lifetime_wins=get_trainer_jockey_combo_wins(row),
            lifetime_places=get_trainer_jockey_combo_places(row),
            lifetime_shows=get_trainer_jockey_combo_shows(row),
            lifetime_roi=get_trainer_jockey_combo_roi(row),
            meet_starts=get_trainer_jockey_combo_meet_starts(row),
            meet_wins=get_trainer_jockey_combo_meet_wins(row),
            meet_places=get_trainer_jockey_combo_meet_places(row),
            meet_shows=get_trainer_jockey_combo_meet_shows(row),
            meet_roi=get_trainer_jockey_combo_meet_roi(row),
        )
