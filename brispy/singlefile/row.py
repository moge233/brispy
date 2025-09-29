#! python3


from .horse import SingleFileHorse
from .utils import get_track, get_date, get_race_number, get_post_position, get_entry, get_distance, \
    get_surface, get_race_type, get_age_sex_restrictions, get_classification, get_purse, get_claiming_price, \
    get_claiming_price_of_horse, get_track_record, get_race_conditions, get_todays_lasix_list, \
    get_todays_bute_list, get_todays_coupled_list, get_todays_mutuel_list, get_simulcast_host_track_code, \
    get_simulcast_host_track_race_number, get_breed_type, get_todays_nasal_strip_change, \
    get_todays_all_weather_surface_flag, get_bris_pace_par_two_furlongs, get_bris_pace_par_four_furlongs, \
    get_bris_pace_par_six_furlongs, get_bris_speed_par, get_bris_late_pace_par, get_trainer_jockey_combo_starts, \
    get_trainer_jockey_combo_wins, get_trainer_jockey_combo_places, get_trainer_jockey_combo_shows, \
    get_trainer_jockey_combo_roi, get_complete_race_conditions, get_low_claiming_price, \
    get_state_bred_flag, get_wager_types, get_trainer_jockey_combo_meet_starts, get_trainer_jockey_combo_meet_wins, \
    get_trainer_jockey_combo_meet_places, get_trainer_jockey_combo_meet_shows, get_trainer_jockey_combo_meet_roi, \
    get_post_time_pacific_military, get_todays_equibase_abbreviated_race_conditions


class SingleFileRow:

    def __init__(self, track: str, date: str, race_number: int, post_position: int, entry: str, distance: int,
                 surface: str, race_type: str, age_sex_restrictions: str, classification: str, purse: int,
                 claiming_price: int, claiming_price_of_horse: int, track_record: float, race_conditions: str,
                 todays_lasix_list: str, todays_bute_list: str, todays_coupled_list: str, todays_mutuel_list: str,
                 simulcast_host_track_code: str, simulcast_host_track_race_number: int, breed_type: str,
                 todays_nasal_strip_change: int, todays_all_weather_surface_flag: str, horse: SingleFileHorse,
                 bris_pace_par_two_furlongs: int, bris_pace_par_four_furlongs: int, bris_pace_par_six_furlongs: int,
                 bris_speed_par: int, bris_late_pace_par: int, trainer_jockey_combo_starts: int,
                 trainer_jockey_combo_wins: int, trainer_jockey_combo_places: int, trainer_jockey_combo_shows: int,
                 trainer_jockey_combo_roi: int, complete_race_conditions: str, low_claiming_price: int,
                 state_bred_flag: str, wager_types: str, trainer_jockey_combo_meet_starts: int,
                 trainer_jockey_combo_meet_wins: int, trainer_jockey_combo_meet_places: int,
                 trainer_jockey_combo_meet_shows: int, trainer_jockey_combo_meet_roi: float,
                 post_time_pacific_military: str, todays_equibase_abbreviated_race_conditions: str):
        self.track: str = track                                                         # 3 characters
        self.date: str = date                                                           # 8 characters
        self.race_number: int = race_number                                             # 2 digits
        self.post_position: int = post_position                                         # 2 digits
        self.entry: str = entry                                                         # 1 character
        self.distance: int = distance                                                   # 5 digits (in yards)
        self.surface: str = surface                                                     # 1 character
        self.race_type: str = race_type                                                 # 2 characters
        self.age_sex_restrictions: str = age_sex_restrictions                           # 3 characters
        self.classification: str = classification                                       # 14 characters
        self.purse: int = purse                                                         # 8 digits
        self.claiming_price: int = claiming_price                                       # 7 digits
        self.claiming_price_of_horse: int = claiming_price_of_horse                     # 7 digits
        self.track_record: float = track_record                                         # 5 digits
        self.race_conditions: str = race_conditions                                     # 500 characters
        self.todays_lasix_list: str = todays_lasix_list                                 #
        self.todays_bute_list: str = todays_bute_list                                   #
        self.todays_coupled_list: str = todays_coupled_list                             #
        self.todays_mutuel_list: str = todays_mutuel_list                               #
        self.simulcast_host_track_code = simulcast_host_track_code                      # 3 characters
        self.simulcast_host_track_race_number = simulcast_host_track_race_number        # 2 digits
        self.breed_type: str = breed_type                                               # 2 characters
        self.todays_nasal_strip_change: int = todays_nasal_strip_change                 # 1 digit
        self.todays_all_weather_surface_flag: str = todays_all_weather_surface_flag     # 1 character
        self.horse: SingleFileHorse = horse                                             #
        self.bris_par_two_furlongs: int = bris_pace_par_two_furlongs                    # 3 digits
        self.bris_par_four_furlongs: int = bris_pace_par_four_furlongs                  # 3 digits
        self.bris_par_six_furlongs: int = bris_pace_par_six_furlongs                    # 3 digits
        self.bris_speed_par: int = bris_speed_par                                       # 3 digits
        self.bris_late_pace_par: int = bris_late_pace_par                               # 3 digits
        self.trainer_jockey_combo_starts: int = trainer_jockey_combo_starts             # 4 digits
        self.trainer_jockey_combo_wins: int = trainer_jockey_combo_wins                 # 4 digits
        self.trainer_jockey_combo_places: int = trainer_jockey_combo_places             # 4 digits
        self.trainer_jockey_combo_shows: int = trainer_jockey_combo_shows               # 4 digits
        self.trainer_jockey_combo_roi: int = trainer_jockey_combo_roi                   # 4 digits
        self.complete_race_conditions: str = complete_race_conditions                   # 254 characters
        self.low_claiming_price: int = low_claiming_price                               # 7 digits
        self.state_bred_flag: str = state_bred_flag                                     # 1 character
        self.wager_types: str = wager_types                                             # 50 characters
        self.trainer_jockey_combo_meet_starts: int = trainer_jockey_combo_meet_starts   # 4 digits
        self.trainer_jockey_combo_meet_wins: int = trainer_jockey_combo_meet_wins       # 4 digits
        self.trainer_jockey_combo_meet_places: int = trainer_jockey_combo_meet_places   # 4 digits
        self.trainer_jockey_combo_meet_shows: int = trainer_jockey_combo_meet_shows     # 4 digits
        self.trainer_jockey_combo_meet_roi: float = trainer_jockey_combo_meet_roi       # 6 digits
        self.post_time_pacific_military: str = post_time_pacific_military               # 4 characters
        self.todays_equibase_abbreviated_race_conditions: str = todays_equibase_abbreviated_race_conditions

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileRow({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileRow({ret[:-2]})'

    @staticmethod
    def create(row: list[str]) -> 'SingleFileRow':
        return SingleFileRow(
            track=get_track(row),
            date=get_date(row),
            race_number=get_race_number(row),
            post_position=get_post_position(row),
            entry=get_entry(row),
            distance=get_distance(row),
            surface=get_surface(row),
            race_type=get_race_type(row),
            age_sex_restrictions=get_age_sex_restrictions(row),
            classification=get_classification(row),
            purse=get_purse(row),
            claiming_price=get_claiming_price(row),
            claiming_price_of_horse=get_claiming_price_of_horse(row),
            track_record=get_track_record(row),
            race_conditions=get_race_conditions(row),
            todays_lasix_list=get_todays_lasix_list(row),
            todays_bute_list=get_todays_bute_list(row),
            todays_coupled_list=get_todays_coupled_list(row),
            todays_mutuel_list=get_todays_mutuel_list(row),
            simulcast_host_track_code=get_simulcast_host_track_code(row),
            simulcast_host_track_race_number=get_simulcast_host_track_race_number(row),
            breed_type=get_breed_type(row),
            todays_nasal_strip_change=get_todays_nasal_strip_change(row),
            todays_all_weather_surface_flag=get_todays_all_weather_surface_flag(row),
            horse=SingleFileHorse.create(row),
            bris_pace_par_two_furlongs=get_bris_pace_par_two_furlongs(row),
            bris_pace_par_four_furlongs=get_bris_pace_par_four_furlongs(row),
            bris_pace_par_six_furlongs=get_bris_pace_par_six_furlongs(row),
            bris_speed_par=get_bris_speed_par(row),
            bris_late_pace_par=get_bris_late_pace_par(row),
            trainer_jockey_combo_starts=get_trainer_jockey_combo_starts(row),
            trainer_jockey_combo_wins=get_trainer_jockey_combo_wins(row),
            trainer_jockey_combo_places=get_trainer_jockey_combo_places(row),
            trainer_jockey_combo_shows=get_trainer_jockey_combo_shows(row),
            trainer_jockey_combo_roi=get_trainer_jockey_combo_roi(row),
            complete_race_conditions=get_complete_race_conditions(row),
            low_claiming_price=get_low_claiming_price(row),
            state_bred_flag=get_state_bred_flag(row),
            wager_types=get_wager_types(row),
            trainer_jockey_combo_meet_starts=get_trainer_jockey_combo_meet_starts(row),
            trainer_jockey_combo_meet_wins=get_trainer_jockey_combo_meet_wins(row),
            trainer_jockey_combo_meet_places=get_trainer_jockey_combo_meet_places(row),
            trainer_jockey_combo_meet_shows=get_trainer_jockey_combo_meet_shows(row),
            trainer_jockey_combo_meet_roi=get_trainer_jockey_combo_meet_roi(row),
            post_time_pacific_military=get_post_time_pacific_military(row),
            todays_equibase_abbreviated_race_conditions=get_todays_equibase_abbreviated_race_conditions(row)
        )

    def distance_to_furlongs(self) -> float:
        return self.distance / 220.0
