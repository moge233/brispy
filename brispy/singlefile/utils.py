#! python3


from brispy.abstract import SpecialEnum
from .index import SingleFileIndex


class WorkoutNumber(SpecialEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11
    TWELVE = 12


class PastPerformanceNumber(SpecialEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10


class TrainerKeyStatNumber(SpecialEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6


def __try_get_str(row: list[str], index: SingleFileIndex) -> str:
    try:
        return row[index.value].rstrip()
    except (IndexError, ValueError, TypeError):
        return ''


def __try_get_int(row: list[str], index: SingleFileIndex) -> int:
    try:
        return int(row[index.value].rstrip())
    except (IndexError, ValueError, TypeError):
        return 0


def __try_get_float(row: list[str], index: SingleFileIndex) -> float:
    try:
        return float(row[index.value].rstrip())
    except (IndexError, ValueError, TypeError):
        return 0.0


def get_track(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TRACK_INDEX)


def get_date(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.DATE_INDEX)


def get_race_number(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.RACE_NUMBER_INDEX)


def get_post_position(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.POST_POSITION_INDEX)


def get_entry(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.ENTRY_INDEX)


def get_distance(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.DISTANCE_INDEX)


def get_surface(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.SURFACE_INDEX)


def get_race_type(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.RACE_TYPE_INDEX)


def get_age_sex_restrictions(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.AGE_SEX_RESTRICTIONS_INDEX)


def get_classification(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.CLASSIFICATION_INDEX)


def get_purse(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.PURSE_INDEX)


def get_claiming_price(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.CLAIMING_PRICE_INDEX)


def get_claiming_price_of_horse(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.CLAIMING_PRICE_OF_HORSE_INDEX)


def get_track_record(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.TRACK_RECORD_INDEX)


def get_race_conditions(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.RACE_CONDITIONS_INDEX)


def get_todays_lasix_list(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_LASIX_LIST_INDEX)


def get_todays_bute_list(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_BUTE_LIST_INDEX)


def get_todays_coupled_list(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_COUPLED_LIST_INDEX)


def get_todays_mutuel_list(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_MUTUEL_LIST_INDEX)


def get_simulcast_host_track_code(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.SIMULCAST_HOST_TRACK_CODE_INDEX)


def get_simulcast_host_track_race_number(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.SIMULCAST_HOST_TRACK_RACE_NUMBER_INDEX)


def get_breed_type(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.BREED_TYPE_INDEX)


def get_todays_nasal_strip_change(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_NASAL_STRIP_CHANGE_INDEX)


def get_todays_all_weather_surface_flag(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_ALL_WEATHER_SURFACE_FLAG_INDEX)


def get_todays_trainer(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_TRAINER_INDEX)


def get_todays_trainer_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_TRAINER_STARTS_INDEX)


def get_todays_trainer_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_TRAINER_WINS_INDEX)


def get_todays_trainer_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_TRAINER_PLACES_INDEX)


def get_todays_trainer_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_TRAINER_SHOWS_INDEX)


def get_todays_jockey(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_JOCKEY_INDEX)


def get_apprentice_weight_allowed(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.APPRENTICE_WEIGHT_ALLOWED_INDEX)


def get_todays_jockey_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_JOCKEY_STARTS_INDEX)


def get_todays_jockey_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_JOCKEY_WINS_INDEX)


def get_todays_jockey_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_JOCKEY_PLACES_INDEX)


def get_todays_jockey_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_JOCKEY_SHOWS_INDEX)


def get_todays_owner(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_OWNER_INDEX)


def get_owners_silks(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.OWNERS_SILKS_INDEX)


def get_mto_ae_indicator(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.MTO_AE_INDICATOR_INDEX)


def get_program_number(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.PROGRAM_NUMBER_INDEX)


def get_morning_line_odds(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.MORNING_LINE_ODDS_INDEX)


def get_horse_name(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_NAME_INDEX)


def get_horse_year_of_birth(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_YEAR_OF_BIRTH_INDEX)


def get_horse_foaling_month(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_FOALING_MONTH_INDEX)


def get_horse_sex(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_SEX_INDEX)


def get_horse_color(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_COLOR_INDEX)


def get_horse_weight(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_WEIGHT_INDEX)


def get_horse_sire(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_SIRE_INDEX)


def get_horse_sires_sire(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_SIRES_SIRE_INDEX)


def get_horse_dam(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_DAM_INDEX)


def get_horse_dams_sire(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_DAMS_SIRE_INDEX)


def get_horse_breeder(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_BREEDER_INDEX)


def get_horse_where(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_WHERE_INDEX)


def get_horse_program_post_position(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_PROGRAM_POST_POSITION_INDEX)


def get_todays_medication1(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_MEDICATION1_INDEX)


def get_todays_medication2(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TODAYS_MEDICATION2_INDEX)


def get_equipment_change(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.EQUIPMENT_CHANGE_INDEX)


def get_lifetime_starts_todays_distance(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_STARTS_TODAYS_DISTANCE_INDEX)


def get_lifetime_wins_todays_distance(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_WINS_TODAYS_DISTANCE_INDEX)


def get_lifetime_places_todays_distance(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_PLACES_TODAYS_DISTANCE_INDEX)


def get_lifetime_shows_todays_distance(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_SHOWS_TODAYS_DISTANCE_INDEX)


def get_lifetime_earnings_todays_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_EARNINGS_TODAYS_TRACK_INDEX)


def get_lifetime_starts_todays_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_STARTS_TODAYS_TRACK_INDEX)


def get_lifetime_wins_todays_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_WINS_TODAYS_TRACK_INDEX)


def get_lifetime_places_todays_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_PLACES_TODAYS_TRACK_INDEX)


def get_lifetime_shows_todays_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_SHOWS_TODAYS_TRACK_INDEX)


def get_lifetime_earnings_todays_distance(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_EARNINGS_TODAYS_DISTANCE_INDEX)


def get_lifetime_starts_turf(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_STARTS_TURF_INDEX)


def get_lifetime_wins_turf(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_WINS_TURF_INDEX)


def get_lifetime_places_turf(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_PLACES_TURF_INDEX)


def get_lifetime_shows_turf(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_SHOWS_TURF_INDEX)


def get_lifetime_earnings_turf(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_EARNINGS_TURF_INDEX)


def get_lifetime_starts_wet(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_STARTS_WET_INDEX)


def get_lifetime_wins_wet(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_WINS_WET_INDEX)


def get_lifetime_places_wet(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_PLACES_WET_INDEX)


def get_lifetime_shows_wet(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_SHOWS_WET_INDEX)


def get_lifetime_earnings_wet(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_EARNINGS_WET_INDEX)


def get_current_year(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.CURRENT_YEAR_INDEX)


def get_current_year_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.CURRENT_YEAR_STARTS_INDEX)


def get_current_year_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.CURRENT_YEAR_WINS_INDEX)


def get_current_year_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.CURRENT_YEAR_PLACES_INDEX)


def get_current_year_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.CURRENT_YEAR_SHOWS_INDEX)


def get_current_year_earnings(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.CURRENT_YEAR_EARNINGS_INDEX)


def get_previous_year(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.PREVIOUS_YEAR_INDEX)


def get_previous_year_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.PREVIOUS_YEAR_STARTS_INDEX)


def get_previous_year_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.PREVIOUS_YEAR_WINS_INDEX)


def get_previous_year_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.PREVIOUS_YEAR_PLACES_INDEX)


def get_previous_year_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.PREVIOUS_YEAR_SHOWS_INDEX)


def get_previous_year_earnings(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.PREVIOUS_YEAR_EARNINGS_INDEX)


def get_lifetime_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_STARTS_INDEX)


def get_lifetime_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_WINS_INDEX)


def get_lifetime_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_PLACES_INDEX)


def get_lifetime_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_SHOWS_INDEX)


def get_lifetime_earnings(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_EARNINGS_INDEX)


def get_workout_date(row: list[str], number: WorkoutNumber) -> str:
    return __try_get_str(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_DATE{number.value}_INDEX'
        )
    )


def get_workout_time(row: list[str], number: WorkoutNumber) -> str:
    return __try_get_str(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_TIME{number.value}_INDEX'
        )
    )


def get_workout_track(row: list[str], number: WorkoutNumber) -> str:
    return __try_get_str(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_TRACK{number.value}_INDEX'
        )
    )


def get_workout_distance(row: list[str], number: WorkoutNumber) -> int:
    return __try_get_int(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_DISTANCE{number.value}_INDEX'
        )
    )


def get_workout_track_condition(row: list[str], number: WorkoutNumber) -> str:
    return __try_get_str(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_TRACK_CONDITION{number.value}_INDEX'
        )
    )


def get_workout_description(row: list[str], number: WorkoutNumber) -> str:
    return __try_get_str(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_DESCRIPTION{number.value}_INDEX'
        )
    )


def get_workout_main_inner_track_indicator(row: list[str], number: WorkoutNumber) -> str:
    return __try_get_str(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_MAIN_INNER_TRACK_INDICATOR{number.value}_INDEX'
        )
    )


def get_workout_number_of_works(row: list[str], number: WorkoutNumber) -> int:
    return __try_get_int(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_NUMBER_OF_WORKS{number.value}_INDEX'
        )
    )


def get_workout_rank(row: list[str], number: WorkoutNumber) -> str:
    return __try_get_str(
        row,
        getattr(
            SingleFileIndex,
            f'WORKOUT_RANK{number.value}_INDEX'
        )
    )


def get_bris_run_style_designation(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.BRIS_RUN_STYLE_DESIGNATION_INDEX)


def get_quirin_speed_points(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.QUIRIN_SPEED_POINTS_INDEX)


def get_bris_pace_par_two_furlongs(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BRIS_PACE_PAR_TWO_FURLONGS_INDEX)


def get_bris_pace_par_four_furlongs(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BRIS_PACE_PAR_FOUR_FURLONGS_INDEX)


def get_bris_pace_par_six_furlongs(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BRIS_PACE_PAR_SIX_FURLONGS_INDEX)


def get_bris_speed_par(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BRIS_SPEED_PAR_INDEX)


def get_bris_late_pace_par(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BRIS_LATE_PACE_PAR_INDEX)


def get_trainer_jockey_combo_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_STARTS_INDEX)


def get_trainer_jockey_combo_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_WINS_INDEX)


def get_trainer_jockey_combo_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_PLACES_INDEX)


def get_trainer_jockey_combo_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_SHOWS_INDEX)


def get_trainer_jockey_combo_roi(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_ROI_INDEX)


def get_days_since_last_race(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.DAYS_SINCE_LAST_RACE_INDEX)


def get_complete_race_conditions1(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.COMPLETE_RACE_CONDITIONS1_INDEX)


def get_complete_race_conditions2(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.COMPLETE_RACE_CONDITIONS2_INDEX)


def get_complete_race_conditions3(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.COMPLETE_RACE_CONDITIONS3_INDEX)


def get_complete_race_conditions4(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.COMPLETE_RACE_CONDITIONS4_INDEX)


def get_complete_race_conditions5(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.COMPLETE_RACE_CONDITIONS5_INDEX)


def get_complete_race_conditions6(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.COMPLETE_RACE_CONDITIONS6_INDEX)


def get_complete_race_conditions(row: list[str]) -> str:
    ret = ''
    for i in range(1, 7):
        ret += __try_get_str(row, getattr(SingleFileIndex, f'COMPLETE_RACE_CONDITIONS{i}_INDEX'))
    return ret


def get_lifetime_starts_all_weather_surface(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_STARTS_ALL_WEATHER_SURFACE_INDEX)


def get_lifetime_wins_all_weather_surface(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_WINS_ALL_WEATHER_SURFACE_INDEX)


def get_lifetime_places_all_weather_surface(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_PLACES_ALL_WEATHER_SURFACE_INDEX)


def get_lifetime_shows_all_weather_surface(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_SHOWS_ALL_WEATHER_SURFACE_INDEX)


def get_lifetime_earnings_all_weather_surface(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LIFETIME_EARNINGS_ALL_WEATHER_SURFACE_INDEX)


def get_best_bris_speed_all_weather_surface(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_ALL_WEATHER_SURFACE_INDEX)


def get_low_claiming_price(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.LOW_CLAIMING_PRICE_INDEX)


def get_state_bred_flag(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.STATE_BRED_FLAG_INDEX)


def get_wager_types(row: list[str]) -> str:
    ret = ''
    for i in range(1, 10):
        ret += __try_get_str(row, getattr(SingleFileIndex, f'WAGER_TYPES{i}_INDEX'))
    return ret


def get_bris_prime_power_rating(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.BRIS_PRIME_POWER_RATING_INDEX)


def get_past_performance_date(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_DATE{number.value}_INDEX'))


def get_past_performance_days_since_previous_race(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_DAYS_SINCE_PREVIOUS_RACE{number.value}_INDEX'))


def get_past_performance_track_code(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_TRACK_CODE{number.value}_INDEX'))


def get_past_performance_bris_track_code(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_BRIS_TRACK_CODE{number.value}_INDEX'))


def get_past_performance_race_number(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_RACE_NUMBER{number.value}_INDEX'))


def get_past_performance_track_condition(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_TRACK_CONDITION{number.value}_INDEX'))


def get_past_performance_distance(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_DISTANCE{number.value}_INDEX'))


def get_past_performance_surface(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_SURFACE{number.value}_INDEX'))


def get_past_performance_special_chute_indicator(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_SPECIAL_CHUTE_INDICATOR{number.value}_INDEX'))


def get_past_performance_number_of_entrants(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_NUMBER_OF_ENTRANTS{number.value}_INDEX'))


def get_past_performance_post_position(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_POST_POSITION{number.value}_INDEX'))


def get_past_performance_equipment(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_EQUIPMENT{number.value}_INDEX'))


def get_past_performance_race_name(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_RACE_NAME{number.value}_INDEX'))


def get_past_performance_medication(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_MEDICATION{number.value}_INDEX'))


def get_past_performance_trip_comment(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_TRIP_COMMENT{number.value}_INDEX'))


def get_past_performance_winners_name(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_WINNERS_NAME{number.value}_INDEX'))


def get_past_performance_second_place_name(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_SECOND_PLACE_NAME{number.value}_INDEX'))


def get_past_performance_third_place_name(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_THIRD_PLACE_NAME{number.value}_INDEX'))


def get_past_performance_winners_weight_carried(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_WINNERS_WEIGHT_CARRIED{number.value}_INDEX'))


def get_past_performance_second_place_weight_carried(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_SECOND_PLACE_WEIGHT_CARRIED{number.value}_INDEX'))


def get_past_performance_third_place_weight_carried(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_THIRD_PLACE_WEIGHT_CARRIED{number.value}_INDEX'))


def get_past_performance_winners_margin(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_WINNERS_MARGIN{number.value}_INDEX'))


def get_past_performance_second_place_margin(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_SECOND_PLACE_MARGIN{number.value}_INDEX'))


def get_past_performance_third_place_margin(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_THIRD_PLACE_MARGIN{number.value}_INDEX'))


def get_past_performance_extra_comment(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_EXTRA_COMMENT{number.value}_INDEX'))


def get_past_performance_weight(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_WEIGHT{number.value}_INDEX'))


def get_past_performance_odds(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_ODDS{number.value}_INDEX'))


def get_past_performance_entry(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_ENTRY{number.value}_INDEX'))


def get_past_performance_race_classification(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_RACE_CLASSIFICATION{number.value}_INDEX'))


def get_past_performance_horse_claiming_price(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_HORSE_CLAIMING_PRICE{number.value}_INDEX'))


def get_past_performance_purse(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_PURSE{number.value}_INDEX'))


def get_past_performance_start_call_position(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_START_CALL_POSITION{number.value}_INDEX'))


def get_past_performance_first_call_position(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_FIRST_CALL_POSITION{number.value}_INDEX'))


def get_past_performance_second_call_position(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_SECOND_CALL_POSITION{number.value}_INDEX'))


def get_past_performance_gate_call_position(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_GATE_CALL_POSITION{number.value}_INDEX'))


def get_past_performance_stretch_position(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_STRETCH_POSITION{number.value}_INDEX'))


def get_past_performance_finish_position(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_FINISH_POSITION{number.value}_INDEX'))


def get_past_performance_start_call_beaten_lengths_leader_margin(row: list[str], number: PastPerformanceNumber) -> \
        float:
    return __try_get_float(
        row,
        getattr(
            SingleFileIndex,
            f'PAST_PERFORMANCE_START_CALL_BEATEN_LENGTHS_LEADER_MARGIN{number.value}_INDEX'
        )
    )


def get_past_performance_start_call_beaten_lengths(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_START_CALL_BEATEN_LENGTHS{number.value}_INDEX'))


def get_past_performance_first_call_beaten_lengths_leader_margin(row: list[str], number: PastPerformanceNumber) -> \
        float:
    return __try_get_float(
        row,
        getattr(
            SingleFileIndex,
            f'PAST_PERFORMANCE_FIRST_CALL_BEATEN_LENGTHS_LEADER_MARGIN{number.value}_INDEX'
        )
    )


def get_past_performance_first_call_beaten_lengths(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_FIRST_CALL_BEATEN_LENGTHS{number.value}_INDEX'))


def get_past_performance_second_call_beaten_lengths_leader_margin(row: list[str], number: PastPerformanceNumber) -> \
        float:
    return __try_get_float(
        row,
        getattr(
            SingleFileIndex,
            f'PAST_PERFORMANCE_SECOND_CALL_BEATEN_LENGTHS_LEADER_MARGIN{number.value}_INDEX'
        )
    )


def get_past_performance_second_call_beaten_lengths(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_SECOND_CALL_BEATEN_LENGTHS{number.value}_INDEX'))


def get_past_performance_first_call_bris_race_shape(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_FIRST_CALL_BRIS_RACE_SHAPE{number.value}_INDEX'))


def get_past_performance_stretch_beaten_lengths_leader_margin(row: list[str], number: PastPerformanceNumber) -> \
        float:
    return __try_get_float(
        row,
        getattr(
            SingleFileIndex,
            f'PAST_PERFORMANCE_STRETCH_BEATEN_LENGTHS_LEADER_MARGIN{number.value}_INDEX'
        )
    )


def get_past_performance_stretch_beaten_lengths(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_STRETCH_BEATEN_LENGTHS{number.value}_INDEX'))


def get_past_performance_finish_beaten_lengths_leader_margin(row: list[str], number: PastPerformanceNumber) -> \
        float:
    return __try_get_float(
        row,
        getattr(
            SingleFileIndex,
            f'PAST_PERFORMANCE_FINISH_BEATEN_LENGTHS_LEADER_MARGIN{number.value}_INDEX'
        )
    )


def get_past_performance_finish_beaten_lengths(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_FINISH_BEATEN_LENGTHS{number.value}_INDEX'))


def get_past_performance_second_call_bris_race_shape(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_SECOND_CALL_BRIS_RACE_SHAPE{number.value}_INDEX'))


def get_past_performance_bris_two_furlong_pace_fig(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_BRIS_TWO_FURLONG_PACE_FIG{number.value}_INDEX'))


def get_past_performance_bris_four_furlong_pace_fig(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_BRIS_FOUR_FURLONG_PACE_FIG{number.value}_INDEX'))


def get_past_performance_bris_six_furlong_pace_fig(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_BRIS_SIX_FURLONG_PACE_FIG{number.value}_INDEX'))


def get_past_performance_bris_eight_furlong_pace_fig(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_BRIS_EIGHT_FURLONG_PACE_FIG{number.value}_INDEX'))


def get_past_performance_bris_ten_furlong_pace_fig(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_BRIS_TEN_FURLONG_PACE_FIG{number.value}_INDEX'))


def get_past_performance_bris_late_pace_fig(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_BRIS_LATE_PACE_FIG{number.value}_INDEX'))


def get_past_performance_bris_speed_rating(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_BRIS_SPEED_RATING{number.value}_INDEX'))


def get_past_performance_speed_rating(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_SPEED_RATING{number.value}_INDEX'))


def get_past_performance_track_variant(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_TRACK_VARIANT{number.value}_INDEX'))


def get_past_performance_two_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_TWO_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_three_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_THREE_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_four_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_FOUR_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_five_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_FIVE_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_six_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_SIX_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_seven_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_SEVEN_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_eight_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_EIGHT_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_ten_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_TEN_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_twelve_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_TWELVE_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_fourteen_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_FOURTEEN_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_sixteen_furlong_fraction(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_SIXTEEN_FURLONG_FRACTION{number.value}_INDEX'))


def get_past_performance_1fr(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_1FR{number.value}_INDEX'))


def get_past_performance_2fr(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_2FR{number.value}_INDEX'))


def get_past_performance_3fr(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_3FR{number.value}_INDEX'))


def get_past_performance_final_time(row: list[str], number: PastPerformanceNumber) -> float:
    return __try_get_float(row,
                           getattr(SingleFileIndex, f'PAST_PERFORMANCE_FINAL_TIME{number.value}_INDEX'))


def get_past_performance_claimed_code(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_CLAIMED_CODE{number.value}_INDEX'))


def get_past_performance_trainer(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_TRAINER{number.value}_INDEX'))


def get_past_performance_jockey(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_JOCKEY{number.value}_INDEX'))


def get_past_performance_apprentice_weight_allowed(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_APPRENTICE_WEIGHT_ALLOWED{number.value}_INDEX'))


def get_past_performance_race_type(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_RACE_TYPE{number.value}_INDEX'))


def get_past_performance_age_and_sex_restrictions(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_AGE_AND_SEX_RESTRICTIONS{number.value}_INDEX')
    )


def get_past_performance_state_bred_flag(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_STATE_BRED_FLAG{number.value}_INDEX'))


def get_past_performance_restricted_qualifier_flag(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_RESTRICTED_QUALIFIER_FLAG{number.value}_INDEX')
    )


def get_past_performance_favorite_indicator(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_FAVORITE_INDICATOR{number.value}_INDEX'))


def get_past_performance_front_bandages_indicator(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_FRONT_BANDAGES_INDICATOR{number.value}_INDEX')
    )


def get_trainer_current_year_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_CURRENT_YEAR_STARTS_INDEX)


def get_trainer_current_year_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_CURRENT_YEAR_WINS_INDEX)


def get_trainer_current_year_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_CURRENT_YEAR_PLACES_INDEX)


def get_trainer_current_year_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_CURRENT_YEAR_SHOWS_INDEX)


def get_trainer_current_year_roi(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.TRAINER_CURRENT_YEAR_ROI_INDEX)


def get_trainer_previous_year_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_PREVIOUS_YEAR_STARTS_INDEX)


def get_trainer_previous_year_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_PREVIOUS_YEAR_WINS_INDEX)


def get_trainer_previous_year_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_PREVIOUS_YEAR_PLACES_INDEX)


def get_trainer_previous_year_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_PREVIOUS_YEAR_SHOWS_INDEX)


def get_trainer_previous_year_roi(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.TRAINER_PREVIOUS_YEAR_ROI_INDEX)


def get_jockey_current_year_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_CURRENT_YEAR_STARTS_INDEX)


def get_jockey_current_year_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_CURRENT_YEAR_WINS_INDEX)


def get_jockey_current_year_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_CURRENT_YEAR_PLACES_INDEX)


def get_jockey_current_year_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_CURRENT_YEAR_SHOWS_INDEX)


def get_jockey_current_year_roi(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.JOCKEY_CURRENT_YEAR_ROI_INDEX)


def get_jockey_previous_year_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_PREVIOUS_YEAR_STARTS_INDEX)


def get_jockey_previous_year_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_PREVIOUS_YEAR_WINS_INDEX)


def get_jockey_previous_year_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_PREVIOUS_YEAR_PLACES_INDEX)


def get_jockey_previous_year_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_PREVIOUS_YEAR_SHOWS_INDEX)


def get_jockey_previous_year_roi(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.JOCKEY_PREVIOUS_YEAR_ROI_INDEX)


def get_past_performance_class_speed_par(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(row,
                         getattr(SingleFileIndex, f'PAST_PERFORMANCE_CLASS_SPEED_PAR{number.value}_INDEX'))


def get_sire_stud_fee(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.SIRE_STUD_FEE_INDEX)


def get_best_bris_speed_fast_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_FAST_TRACK_INDEX)


def get_best_bris_speed_turf(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_TURF_INDEX)


def get_best_bris_speed_off_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_OFF_TRACK_INDEX)


def get_best_bris_speed_distance(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_DISTANCE_INDEX)


def get_past_performance_bar_shoe(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_BAR_SHOE{number.value}_INDEX')
    )


def get_past_performance_company_line_codes(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_COMPANY_LINE_CODES{number.value}_INDEX')
    )


def get_past_performance_low_claiming_price_of_race(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_LOW_CLAIMING_PRICE_OF_RACE{number.value}_INDEX')
    )


def get_past_performance_high_claiming_price_of_race(row: list[str], number: PastPerformanceNumber) -> int:
    return __try_get_int(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_HIGH_CLAIMING_PRICE_OF_RACE{number.value}_INDEX')
    )


def get_horse_auction_price(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_AUCTION_PRICE_INDEX)


def get_horse_auction_location(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.HORSE_AUCTION_LOCATION_INDEX)


def get_past_performance_start_code(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(row, getattr(SingleFileIndex, f'PAST_PERFORMANCE_START_CODE{number.value}_INDEX'))


def get_bris_dirt_pedigree_rating(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.BRIS_DIRT_PEDIGREE_RATING_INDEX)


def get_bris_mud_pedigree_rating(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.BRIS_MUD_PEDIGREE_RATING_INDEX)


def get_bris_turf_pedigree_rating(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.BRIS_TURF_PEDIGREE_RATING_INDEX)


def get_bris_distance_pedigree_rating(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.BRIS_DISTANCE_PEDIGREE_RATING_INDEX)


def get_best_bris_speed_life(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_LIFE_INDEX)


def get_best_bris_speed_most_recent_year(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_MOST_RECENT_YEAR_INDEX)


def get_best_bris_speed_second_most_recent_year(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_SECOND_MOST_RECENT_YEAR_INDEX)


def get_best_bris_speed_todays_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.BEST_BRIS_SPEED_TODAYS_TRACK_INDEX)


def get_horse_starts_fast_dirt_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_STARTS_FAST_DIRT_TRACK_INDEX)


def get_horse_wins_fast_dirt_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_WINS_FAST_DIRT_TRACK_INDEX)


def get_horse_places_fast_dirt_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_PLACES_FAST_DIRT_TRACK_INDEX)


def get_horse_shows_fast_dirt_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_SHOWS_FAST_DIRT_TRACK_INDEX)


def get_horse_earnings_fast_dirt_track(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.HORSE_EARNINGS_FAST_DIRT_TRACK_INDEX)


def get_trainer_key_stat_category(row: list[str], number: TrainerKeyStatNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'TRAINER_KEY_STAT{number.value}_CATEGORY_INDEX')
    )


def get_trainer_key_stat_number_of_starts(row: list[str], number: TrainerKeyStatNumber) -> int:
    return __try_get_int(
        row,
        getattr(SingleFileIndex, f'TRAINER_KEY_STAT{number.value}_NUMBER_OF_STARTS_INDEX')
    )


def get_trainer_key_stat_win_percentage(row: list[str], number: TrainerKeyStatNumber) -> float:
    return __try_get_float(
        row,
        getattr(SingleFileIndex, f'TRAINER_KEY_STAT{number.value}_WIN_PERCENTAGE_INDEX')
    )


def get_trainer_key_stat_itm_percentage(row: list[str], number: TrainerKeyStatNumber) -> float:
    return __try_get_float(
        row,
        getattr(SingleFileIndex, f'TRAINER_KEY_STAT{number.value}_ITM_PERCENTAGE_INDEX')
    )


def get_trainer_key_stat_roi(row: list[str], number: TrainerKeyStatNumber) -> float:
    return __try_get_float(
        row,
        getattr(SingleFileIndex, f'TRAINER_KEY_STAT{number.value}_ROI_INDEX')
    )


def get_jockey_at_distance_on_turf_label(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.JOCKEY_AT_DISTANCE_ON_TURF_LABEL_INDEX)


def get_jockey_at_distance_on_turf_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_AT_DISTANCE_ON_TURF_STARTS_INDEX)


def get_jockey_at_distance_on_turf_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_AT_DISTANCE_ON_TURF_WINS_INDEX)


def get_jockey_at_distance_on_turf_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_AT_DISTANCE_ON_TURF_PLACES_INDEX)


def get_jockey_at_distance_on_turf_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_AT_DISTANCE_ON_TURF_SHOWS_INDEX)


def get_jockey_at_distance_on_turf_roi(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.JOCKEY_AT_DISTANCE_ON_TURF_ROI_INDEX)


def get_jockey_at_distance_on_turf_earnings(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.JOCKEY_AT_DISTANCE_ON_TURF_EARNINGS_INDEX)


def get_post_times_by_region(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.POST_TIMES_BY_REGION_INDEX)


def get_past_performance_sealed_track_indicator(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_SEALED_TRACK_INDICATOR{number.value}_INDEX')
    )


def get_past_performance_all_weather_surface_flag(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_ALL_WEATHER_SURFACE_FLAG{number.value}_INDEX')
    )


def get_trainer_jockey_combo_meet_starts(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_MEET_STARTS_INDEX)


def get_trainer_jockey_combo_meet_wins(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_MEET_WINS_INDEX)


def get_trainer_jockey_combo_meet_places(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_MEET_PLACES_INDEX)


def get_trainer_jockey_combo_meet_shows(row: list[str]) -> int:
    return __try_get_int(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_MEET_SHOWS_INDEX)


def get_trainer_jockey_combo_meet_roi(row: list[str]) -> float:
    return __try_get_float(row, SingleFileIndex.TRAINER_JOCKEY_COMBO_MEET_ROI_INDEX)


def get_post_time_pacific_military(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.POST_TIME_PACIFIC_MILITARY_INDEX)


def get_past_performance_equibase_abbreviated_race_conditions(row: list[str], number: PastPerformanceNumber) -> str:
    return __try_get_str(
        row,
        getattr(SingleFileIndex, f'PAST_PERFORMANCE_EQUIBASE_ABBREVIATED_RACE_CONDITIONS{number.value}_INDEX')
    )


def get_todays_equibase_abbreviated_race_conditions(row: list[str]) -> str:
    return __try_get_str(row, SingleFileIndex.TODAYS_EQUIBASE_ABBREVIATED_RACE_CONDITIONS_INDEX)


__all__ = [
    "get_track",
    "get_date",
    "get_race_number",
    "get_post_position",
    "get_entry",
    "get_distance",
    "get_surface",
    "get_race_type",
    "get_age_sex_restrictions",
    "get_classification",
    "get_purse",
    "get_claiming_price",
    "get_claiming_price_of_horse",
    "get_track_record",
    "get_race_conditions",
    "get_todays_lasix_list",
    "get_todays_bute_list",
    "get_todays_coupled_list",
    "get_todays_mutuel_list",
    "get_simulcast_host_track_code",
    "get_simulcast_host_track_race_number",
    "get_breed_type",
    "get_todays_nasal_strip_change",
    "get_todays_all_weather_surface_flag",
    "get_todays_trainer",
    "get_todays_trainer_starts",
    "get_todays_trainer_wins",
    "get_todays_trainer_places",
    "get_todays_trainer_shows",
    "get_todays_jockey",
    "get_apprentice_weight_allowed",
    "get_todays_jockey_starts",
    "get_todays_jockey_wins",
    "get_todays_jockey_places",
    "get_todays_jockey_shows",
    "get_todays_owner",
    "get_owners_silks",
    "get_mto_ae_indicator",
    "get_program_number",
    "get_morning_line_odds",
    "get_horse_name",
    "get_horse_year_of_birth",
    "get_horse_foaling_month",
    "get_horse_sex",
    "get_horse_color",
    "get_horse_weight",
    "get_horse_sire",
    "get_horse_sires_sire",
    "get_horse_dam",
    "get_horse_dams_sire",
    "get_horse_breeder",
    "get_horse_where",
    "get_horse_program_post_position",
    "get_todays_medication1",
    "get_todays_medication2",
    "get_equipment_change",
    "get_lifetime_starts_todays_distance",
    "get_lifetime_wins_todays_distance",
    "get_lifetime_places_todays_distance",
    "get_lifetime_shows_todays_distance",
    "get_lifetime_earnings_todays_distance",
    "get_lifetime_starts_todays_track",
    "get_lifetime_wins_todays_track",
    "get_lifetime_places_todays_track",
    "get_lifetime_shows_todays_track",
    "get_lifetime_earnings_todays_track",
    "get_lifetime_starts_turf",
    "get_lifetime_wins_turf",
    "get_lifetime_places_turf",
    "get_lifetime_shows_turf",
    "get_lifetime_earnings_turf",
    "get_lifetime_starts_wet",
    "get_lifetime_wins_wet",
    "get_lifetime_places_wet",
    "get_lifetime_shows_wet",
    "get_lifetime_earnings_wet",
    "get_current_year",
    "get_current_year_starts",
    "get_current_year_wins",
    "get_current_year_places",
    "get_current_year_shows",
    "get_current_year_earnings",
    "get_previous_year",
    "get_previous_year_starts",
    "get_previous_year_wins",
    "get_previous_year_places",
    "get_previous_year_shows",
    "get_previous_year_earnings",
    "get_lifetime_starts",
    "get_lifetime_wins",
    "get_lifetime_places",
    "get_lifetime_shows",
    "get_lifetime_earnings",
    "get_bris_run_style_designation",
    "get_quirin_speed_points",
    "get_bris_pace_par_two_furlongs",
    "get_bris_pace_par_four_furlongs",
    "get_bris_pace_par_six_furlongs",
    "get_bris_speed_par",
    "get_bris_late_pace_par",
    "get_trainer_jockey_combo_starts",
    "get_trainer_jockey_combo_wins",
    "get_trainer_jockey_combo_places",
    "get_trainer_jockey_combo_shows",
    "get_trainer_jockey_combo_roi",
    "get_days_since_last_race",
    "get_complete_race_conditions1",
    "get_complete_race_conditions2",
    "get_complete_race_conditions3",
    "get_complete_race_conditions4",
    "get_complete_race_conditions5",
    "get_complete_race_conditions6",
    "get_complete_race_conditions",
    "get_lifetime_starts_all_weather_surface",
    "get_lifetime_wins_all_weather_surface",
    "get_lifetime_places_all_weather_surface",
    "get_lifetime_shows_all_weather_surface",
    "get_lifetime_earnings_all_weather_surface",
    "get_best_bris_speed_all_weather_surface",
    "get_low_claiming_price",
    "get_state_bred_flag",
    "get_wager_types",
    "get_bris_prime_power_rating",
    "get_past_performance_date",
    "get_past_performance_days_since_previous_race",
    "get_past_performance_track_code",
    "get_past_performance_bris_track_code",
    "get_past_performance_race_number",
    "get_past_performance_track_condition",
    "get_past_performance_distance",
    "get_past_performance_surface",
    "get_past_performance_special_chute_indicator",
    "get_past_performance_post_position",
    "get_past_performance_equipment",
    "get_past_performance_race_name",
    "get_past_performance_medication",
    "get_past_performance_trip_comment",
    "get_past_performance_winners_name",
    "get_past_performance_second_place_name",
    "get_past_performance_third_place_name",
    "get_past_performance_winners_weight_carried",
    "get_past_performance_second_place_weight_carried",
    "get_past_performance_third_place_weight_carried",
    "get_past_performance_winners_margin",
    "get_past_performance_second_place_margin",
    "get_past_performance_third_place_margin",
    "get_past_performance_extra_comment",
    "get_past_performance_weight",
    "get_past_performance_odds",
    "get_past_performance_entry",
    "get_past_performance_race_classification",
    "get_past_performance_horse_claiming_price",
    "get_past_performance_purse",
    "get_past_performance_start_call_position",
    "get_past_performance_first_call_position",
    "get_past_performance_second_call_position",
    "get_past_performance_gate_call_position",
    "get_past_performance_stretch_position",
    "get_past_performance_finish_position",
    "get_past_performance_start_call_beaten_lengths_leader_margin",
    "get_past_performance_start_call_beaten_lengths",
    "get_past_performance_first_call_beaten_lengths_leader_margin",
    "get_past_performance_first_call_beaten_lengths",
    "get_past_performance_second_call_beaten_lengths_leader_margin",
    "get_past_performance_second_call_beaten_lengths",
    "get_past_performance_first_call_bris_race_shape",
    "get_past_performance_stretch_beaten_lengths_leader_margin",
    "get_past_performance_stretch_beaten_lengths",
    "get_past_performance_finish_beaten_lengths_leader_margin",
    "get_past_performance_finish_beaten_lengths",
    "get_past_performance_second_call_bris_race_shape",
    "get_past_performance_bris_two_furlong_pace_fig",
    "get_past_performance_bris_four_furlong_pace_fig",
    "get_past_performance_bris_six_furlong_pace_fig",
    "get_past_performance_bris_eight_furlong_pace_fig",
    "get_past_performance_bris_ten_furlong_pace_fig",
    "get_past_performance_bris_late_pace_fig",
    "get_past_performance_bris_speed_rating",
    "get_past_performance_speed_rating",
    "get_past_performance_track_variant",
    "get_past_performance_two_furlong_fraction",
    "get_past_performance_three_furlong_fraction",
    "get_past_performance_four_furlong_fraction",
    "get_past_performance_five_furlong_fraction",
    "get_past_performance_six_furlong_fraction",
    "get_past_performance_seven_furlong_fraction",
    "get_past_performance_eight_furlong_fraction",
    "get_past_performance_ten_furlong_fraction",
    "get_past_performance_twelve_furlong_fraction",
    "get_past_performance_fourteen_furlong_fraction",
    "get_past_performance_sixteen_furlong_fraction",
    "get_past_performance_1fr",
    "get_past_performance_2fr",
    "get_past_performance_3fr",
    "get_past_performance_final_time",
    "get_past_performance_claimed_code",
    "get_past_performance_trainer",
    "get_past_performance_jockey",
    "get_past_performance_apprentice_weight_allowed",
    "get_past_performance_race_type",
    "get_past_performance_age_and_sex_restrictions",
    "get_past_performance_state_bred_flag",
    "get_past_performance_restricted_qualifier_flag",
    "get_past_performance_favorite_indicator",
    "get_past_performance_front_bandages_indicator",
    "get_trainer_current_year_starts",
    "get_trainer_current_year_wins",
    "get_trainer_current_year_places",
    "get_trainer_current_year_shows",
    "get_trainer_current_year_roi",
    "get_trainer_previous_year_starts",
    "get_trainer_previous_year_wins",
    "get_trainer_previous_year_places",
    "get_trainer_previous_year_shows",
    "get_trainer_previous_year_roi",
    "get_jockey_current_year_starts",
    "get_jockey_current_year_wins",
    "get_jockey_current_year_places",
    "get_jockey_current_year_shows",
    "get_jockey_current_year_roi",
    "get_jockey_previous_year_starts",
    "get_jockey_previous_year_wins",
    "get_jockey_previous_year_places",
    "get_jockey_previous_year_shows",
    "get_jockey_previous_year_roi",
    "get_past_performance_class_speed_par",
    "get_sire_stud_fee",
    "get_best_bris_speed_fast_track",
    "get_best_bris_speed_turf",
    "get_best_bris_speed_off_track",
    "get_best_bris_speed_distance",
    "get_past_performance_bar_shoe",
    "get_past_performance_company_line_codes",
    "get_past_performance_low_claiming_price_of_race",
    "get_past_performance_high_claiming_price_of_race",
    "get_horse_auction_price",
    "get_horse_auction_location",
    "get_past_performance_start_code",
    "get_bris_dirt_pedigree_rating",
    "get_bris_mud_pedigree_rating",
    "get_bris_turf_pedigree_rating",
    "get_bris_distance_pedigree_rating",
    "get_best_bris_speed_life",
    "get_best_bris_speed_most_recent_year",
    "get_best_bris_speed_second_most_recent_year",
    "get_best_bris_speed_todays_track",
    "get_horse_starts_fast_dirt_track",
    "get_horse_wins_fast_dirt_track",
    "get_horse_places_fast_dirt_track",
    "get_horse_shows_fast_dirt_track",
    "get_horse_earnings_fast_dirt_track",
    "get_trainer_key_stat_category",
    "get_trainer_key_stat_number_of_starts",
    "get_trainer_key_stat_win_percentage",
    "get_trainer_key_stat_itm_percentage",
    "get_trainer_key_stat_roi",
    "get_jockey_at_distance_on_turf_label",
    "get_jockey_at_distance_on_turf_starts",
    "get_jockey_at_distance_on_turf_wins",
    "get_jockey_at_distance_on_turf_places",
    "get_jockey_at_distance_on_turf_shows",
    "get_jockey_at_distance_on_turf_roi",
    "get_jockey_at_distance_on_turf_earnings",
    "get_post_times_by_region",
    "get_past_performance_sealed_track_indicator",
    "get_past_performance_all_weather_surface_flag",
    "get_trainer_jockey_combo_meet_starts",
    "get_trainer_jockey_combo_meet_wins",
    "get_trainer_jockey_combo_meet_places",
    "get_trainer_jockey_combo_meet_shows",
    "get_trainer_jockey_combo_meet_roi",
    "get_post_time_pacific_military",
    "get_todays_equibase_abbreviated_race_conditions",
]
