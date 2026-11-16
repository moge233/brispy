#! python3


from dataclasses import dataclass

from .utils import get_trainer_jockey_combo_starts, \
    get_trainer_jockey_combo_wins, get_trainer_jockey_combo_places, get_trainer_jockey_combo_shows, \
    get_trainer_jockey_combo_roi, get_trainer_jockey_combo_meet_starts, get_trainer_jockey_combo_meet_wins, \
    get_trainer_jockey_combo_meet_places, get_trainer_jockey_combo_meet_shows, get_trainer_jockey_combo_meet_roi


@dataclass
class SingleFileTrainerJockeyCombo:
    lifetime_starts: int | None                    # 4 digits
    lifetime_wins: int | None                      # 4 digits
    lifetime_places: int | None                    # 4 digits
    lifetime_shows: int | None                     # 4 digits
    lifetime_roi: float | None                     # e.g. -0.60
    meet_starts: int | None                        # 4 digits
    meet_wins: int | None                          # 4 digits
    meet_places: int | None                        # 4 digits
    meet_shows: int | None                         # 4 digits
    meet_roi: float | None                         # 6 digits

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
