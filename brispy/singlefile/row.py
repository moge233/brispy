#! python3


from dataclasses import dataclass

from .horse import SingleFileHorse
from .jockey import SingleFileJockey
from .owner import SingleFileOwner
from .trainer import SingleFileTrainer
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


@dataclass
class SingleFileRow:
    track: str                                          # 3 characters
    date: str                                           # 8 characters
    race_number: int                                    # 2 digits
    post_position: int                                  # 2 digits
    entry: str                                          # 1 character
    distance: int                                       # 5 digits (in yards)
    surface: str                                        # 1 character
    race_type: str                                      # 2 characters
    age_sex_restrictions: str                           # 3 characters
    classification: str                                 # 14 characters
    purse: int                                          # 8 digits
    claiming_price: int                                 # 7 digits
    claiming_price_of_horse: int                        # 7 digits
    track_record: float                                 # 5 digits
    race_conditions: str                                # 500 characters
    todays_lasix_list: str                              #
    todays_bute_list: str                               #
    todays_coupled_list: str                            #
    todays_mutuel_list: str                             #
    simulcast_host_track_code: str                      # 3 characters
    simulcast_host_track_race_number: int               # 2 digits
    breed_type: str                                     # 2 characters
    todays_nasal_strip_change: int                      # 1 digit
    todays_all_weather_surface_flag: str                # 1 character
    horse: SingleFileHorse                              #
    trainer: SingleFileTrainer                          #
    jockey: SingleFileJockey                            #
    owner: SingleFileOwner                              #
    bris_par_two_furlongs: int                          # 3 digits
    bris_par_four_furlongs: int                         # 3 digits
    bris_par_six_furlongs: int                          # 3 digits
    bris_speed_par: int                                 # 3 digits
    bris_late_pace_par: int                             # 3 digits
    trainer_jockey_combo_starts: int                    # 4 digits
    trainer_jockey_combo_wins: int                      # 4 digits
    trainer_jockey_combo_places: int                    # 4 digits
    trainer_jockey_combo_shows: int                     # 4 digits
    trainer_jockey_combo_roi: int                       # 4 digits
    complete_race_conditions: str                       # 254 characters
    low_claiming_price: int                             # 7 digits
    state_bred_flag: str                                # 1 character
    wager_types: str                                    # 50 characters
    trainer_jockey_combo_meet_starts: int               # 4 digits
    trainer_jockey_combo_meet_wins: int                 # 4 digits
    trainer_jockey_combo_meet_places: int               # 4 digits
    trainer_jockey_combo_meet_shows: int                # 4 digits
    trainer_jockey_combo_meet_roi: float                # 6 digits
    post_time_pacific_military: str                     # 4 characters
    todays_equibase_abbreviated_race_conditions: str    # 17 characters

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
            trainer=SingleFileTrainer.create(row),
            jockey=SingleFileJockey.create(row),
            owner=SingleFileOwner.create(row),
            bris_par_two_furlongs=get_bris_pace_par_two_furlongs(row),
            bris_par_four_furlongs=get_bris_pace_par_four_furlongs(row),
            bris_par_six_furlongs=get_bris_pace_par_six_furlongs(row),
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
