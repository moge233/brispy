#! python3


from dataclasses import dataclass

from .utils import get_bris_pace_par_two_furlongs, get_bris_pace_par_four_furlongs, \
    get_bris_pace_par_six_furlongs, get_bris_speed_par, get_bris_late_pace_par


@dataclass
class SingleFileBrisPars:
    two_furlongs: int                          # 3 digits
    four_furlongs: int                         # 3 digits
    six_furlongs: int                          # 3 digits
    speed_par: int                             # 3 digits
    late_pace: int                             # 3 digits

    @staticmethod
    def create(row: list[str]) -> 'SingleFileBrisPars':
        return SingleFileBrisPars(
            two_furlongs=get_bris_pace_par_two_furlongs(row),
            four_furlongs=get_bris_pace_par_four_furlongs(row),
            six_furlongs=get_bris_pace_par_six_furlongs(row),
            speed_par=get_bris_speed_par(row),
            late_pace=get_bris_late_pace_par(row)
        )
