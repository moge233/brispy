#! python3


from abstract import Horse, PastPerformance
from .jockey import SingleFileJockey
from .owner import SingleFileOwner
from .trainer import SingleFileTrainer
from .record import SingleFileRecord, SingleFileRecordWithYear
from .workout import SingleFileWorkout
from .utils import get_horse_name, get_horse_year_of_birth, get_horse_foaling_month, get_horse_sex, \
    get_horse_color, get_horse_weight, get_horse_sire, get_horse_sires_sire, get_horse_dam, get_horse_dams_sire, \
    get_horse_breeder, get_horse_where, get_horse_program_post_position, get_todays_medication1, get_mto_ae_indicator, \
    get_program_number, get_morning_line_odds, get_lifetime_starts_todays_distance, get_lifetime_wins_todays_distance, \
    get_lifetime_places_todays_distance, get_lifetime_shows_todays_distance, get_lifetime_earnings_todays_distance, \
    get_lifetime_starts_todays_track, get_lifetime_wins_todays_track, get_lifetime_places_todays_track, \
    get_lifetime_shows_todays_track, get_lifetime_earnings_todays_track, \
    get_lifetime_starts_turf, get_lifetime_wins_turf, get_lifetime_places_turf, \
    get_lifetime_shows_turf, get_lifetime_earnings_turf, \
    get_lifetime_starts_wet, get_lifetime_wins_wet, get_lifetime_places_wet, \
    get_lifetime_shows_wet, get_lifetime_earnings_wet, \
    get_current_year, get_current_year_starts, get_current_year_wins, get_current_year_places, \
    get_current_year_shows, get_current_year_earnings, \
    get_previous_year, get_previous_year_starts, get_previous_year_wins, get_previous_year_places, \
    get_previous_year_shows, get_previous_year_earnings, \
    get_lifetime_starts, get_lifetime_wins, get_lifetime_places, \
    get_lifetime_shows, get_lifetime_earnings, \
    get_equipment_change, get_bris_run_style_designation, get_quirin_speed_points, \
    get_lifetime_starts_all_weather_surface, get_lifetime_wins_all_weather_surface, \
    get_lifetime_places_all_weather_surface, get_lifetime_shows_all_weather_surface, \
    get_lifetime_earnings_all_weather_surface, get_best_bris_speed_all_weather_surface, \
    get_bris_prime_power_rating, get_past_performance_date, get_past_performance_days_since_previous_race, \
    get_past_performance_track_code, get_past_performance_bris_track_code, get_past_performance_race_number, \
    get_past_performance_track_condition, get_past_performance_distance, get_past_performance_surface, \
    get_past_performance_special_chute_indicator, get_past_performance_number_of_entrants, \
    get_past_performance_post_position, get_past_performance_equipment, get_past_performance_race_name, \
    get_past_performance_medication, get_past_performance_trip_comment, get_past_performance_winners_name, \
    get_past_performance_second_place_name, get_past_performance_third_place_name, \
    get_past_performance_winners_weight_carried, get_past_performance_second_place_weight_carried, \
    get_past_performance_third_place_weight_carried, get_past_performance_winners_margin, \
    get_past_performance_second_place_margin, get_past_performance_third_place_margin, \
    get_past_performance_extra_comment, get_past_performance_weight, get_past_performance_odds, \
    get_past_performance_entry, get_past_performance_race_classification, get_past_performance_horse_claiming_price, \
    get_past_performance_purse, get_past_performance_start_call_position, get_past_performance_first_call_position, \
    get_past_performance_second_call_position, get_past_performance_gate_call_position, \
    get_past_performance_stretch_position, get_past_performance_finish_position, \
    get_past_performance_start_call_beaten_lengths_leader_margin, get_past_performance_start_call_beaten_lengths, \
    get_past_performance_first_call_beaten_lengths_leader_margin, get_past_performance_first_call_beaten_lengths, \
    get_past_performance_second_call_beaten_lengths_leader_margin, get_past_performance_second_call_beaten_lengths, \
    get_past_performance_first_call_bris_race_shape, \
    get_past_performance_stretch_beaten_lengths_leader_margin, get_past_performance_stretch_beaten_lengths, \
    get_past_performance_finish_beaten_lengths_leader_margin, get_past_performance_finish_beaten_lengths, \
    get_past_performance_second_call_bris_race_shape, get_past_performance_bris_two_furlong_pace_fig, \
    get_past_performance_bris_four_furlong_pace_fig, get_past_performance_bris_six_furlong_pace_fig, \
    get_past_performance_bris_eight_furlong_pace_fig, get_past_performance_bris_ten_furlong_pace_fig, \
    get_past_performance_bris_late_pace_fig, get_past_performance_bris_speed_rating, \
    get_past_performance_speed_rating, get_past_performance_track_variant, \
    get_past_performance_two_furlong_fraction, get_past_performance_three_furlong_fraction, \
    get_past_performance_four_furlong_fraction, get_past_performance_five_furlong_fraction, \
    get_past_performance_six_furlong_fraction, get_past_performance_seven_furlong_fraction, \
    get_past_performance_eight_furlong_fraction, get_past_performance_ten_furlong_fraction, \
    get_past_performance_twelve_furlong_fraction, get_past_performance_fourteen_furlong_fraction, \
    get_past_performance_sixteen_furlong_fraction, get_past_performance_1fr, get_past_performance_2fr, \
    get_past_performance_3fr, get_past_performance_final_time, get_past_performance_claimed_code, \
    get_past_performance_trainer, get_past_performance_jockey, get_past_performance_apprentice_weight_allowed, \
    get_past_performance_race_type, get_past_performance_age_and_sex_restrictions, \
    get_past_performance_state_bred_flag, get_past_performance_restricted_qualifier_flag, \
    get_past_performance_favorite_indicator, get_past_performance_front_bandages_indicator, \
    get_past_performance_class_speed_par, get_sire_stud_fee, get_best_bris_speed_fast_track, get_best_bris_speed_turf, \
    get_best_bris_speed_off_track, get_best_bris_speed_distance, get_past_performance_bar_shoe, \
    get_past_performance_company_line_codes, get_past_performance_low_claiming_price_of_race, \
    get_past_performance_high_claiming_price_of_race, get_horse_auction_price, get_horse_auction_location, \
    get_past_performance_start_code, \
    get_bris_dirt_pedigree_rating, get_bris_mud_pedigree_rating, get_bris_turf_pedigree_rating, \
    get_bris_distance_pedigree_rating, get_best_bris_speed_life, get_best_bris_speed_most_recent_year, \
    get_best_bris_speed_second_most_recent_year, get_best_bris_speed_todays_track, get_horse_starts_fast_dirt_track, \
    get_horse_wins_fast_dirt_track, get_horse_places_fast_dirt_track, get_horse_shows_fast_dirt_track, \
    get_horse_earnings_fast_dirt_track, \
    WorkoutNumber, PastPerformanceNumber


class SingleFilePastPerformance(PastPerformance):
    def __init__(self, date: str, days_since_previous_race: int, track_code: str, bris_track_code: str,
                 race_number: int, track_condition: str, distance: int, surface: str, special_chute_indicator: str,
                 number_of_entrants: int, post_position: int, equipment: str, race_name: str, medication: str,
                 trip_comment: str, winners_name: str, second_place_name: str, third_place_name: str,
                 winners_weight_carried: int, second_place_weight_carried: int, third_place_weight_carried: int,
                 winners_margin: float, second_place_margin: float, third_place_margin: float, extra_comment: str,
                 weight: int, odds: float, entry: str, race_classification: str, horse_claiming_price: int, purse: int,
                 start_call_position: str, first_call_position: str, second_call_position: str, gate_call_position: str,
                 stretch_position: str, finish_position: str, start_call_beaten_lengths_leader_margin: float,
                 start_call_beaten_lengths: float, first_call_beaten_lengths_leader_margin: float,
                 first_call_beaten_lengths: float, second_call_beaten_lengths_leader_margin: float,
                 second_call_beaten_lengths: float, first_call_bris_race_shape: int,
                 stretch_beaten_lengths_leader_margin: float, stretch_beaten_lengths: float,
                 finish_beaten_lengths_leader_margin: float, finish_beaten_lengths: float,
                 second_call_bris_race_shape: int, bris_two_furlong_pace_fig: int, bris_four_furlong_pace_fig: int,
                 bris_six_furlong_pace_fig: int, bris_eight_furlong_pace_fig: int, bris_ten_furlong_pace_fig: int,
                 bris_late_pace_fig: int, bris_speed_rating: int, speed_rating: int, track_variant: int,
                 two_furlong_fraction: float, three_furlong_fraction: float, four_furlong_fraction: float,
                 five_furlong_fraction: float, six_furlong_fraction: float, seven_furlong_fraction: float,
                 eight_furlong_fraction: float, ten_furlong_fraction: float, twelve_furlong_fraction: float,
                 fourteen_furlong_fraction: float, sixteen_furlong_fraction: float, fr1: float, fr2: float, fr3: float,
                 final_time: float, claimed_code: str, trainer: str, jockey: str, apprentice_weight_allowed: int,
                 race_type: str, age_and_sex_restrictions: str, state_bred_flag: str, restricted_qualifier_flag: str,
                 favorite_indicator: str, front_bandages_indicator: str, class_speed_par: int, bar_shoe: str,
                 company_line_codes: str, low_claiming_price_of_race: int, high_claiming_price_of_race: int,
                 start_code: str):
        super().__init__()
        self.date: str = date
        self.days_since_previous_race: int = days_since_previous_race
        self.track_code: str = track_code
        self.bris_track_code: str = bris_track_code
        self.race_number: int = race_number
        self.track_condition: str = track_condition
        self.distance: int = distance
        self.surface: str = surface
        self.special_chute_indicator: str = special_chute_indicator
        self.number_of_entrants: int = number_of_entrants
        self.post_position: int = post_position
        self.equipment: str = equipment
        self.race_name: str = race_name
        self.medication: str = medication
        self.trip_comment: str = trip_comment
        self.winners_name: str = winners_name
        self.second_place_name: str = second_place_name
        self.third_place_name: str = third_place_name
        self.winners_weight_carried: int = winners_weight_carried
        self.second_place_weight_carried: int = second_place_weight_carried
        self.third_place_weight_carried: int = third_place_weight_carried
        self.winners_margin: float = winners_margin
        self.second_place_margin: float = second_place_margin
        self.third_place_margin: float = third_place_margin
        self.extra_comment: str = extra_comment
        self.weight: int = weight
        self.odds: float = odds
        self.entry: str = entry
        self.race_classification: str = race_classification
        self.horse_claiming_price: int = horse_claiming_price
        self.purse: int = purse
        self.start_call_position: str = start_call_position
        self.first_call_position: str = first_call_position
        self.second_call_position: str = second_call_position
        self.gate_call_position: str = gate_call_position
        self.stretch_position: str = stretch_position
        self.finish_position: str = finish_position
        self.start_call_beaten_lengths_leader_margin: float = start_call_beaten_lengths_leader_margin
        self.start_call_beaten_lengths: float = start_call_beaten_lengths
        self.first_call_beaten_lengths_leader_margin: float = first_call_beaten_lengths_leader_margin
        self.first_call_beaten_lengths: float = first_call_beaten_lengths
        self.second_call_beaten_lengths_leader_margin: float = second_call_beaten_lengths_leader_margin
        self.second_call_beaten_lengths: float = second_call_beaten_lengths
        self.first_call_bris_race_shape: int = first_call_bris_race_shape
        self.stretch_beaten_lengths_leader_margin: float = stretch_beaten_lengths_leader_margin
        self.stretch_beaten_lengths: float = stretch_beaten_lengths
        self.finish_beaten_lengths_leader_margin: float = finish_beaten_lengths_leader_margin
        self.finish_beaten_lengths: float = finish_beaten_lengths
        self.second_call_bris_race_shape: int = second_call_bris_race_shape
        self.bris_two_furlong_pace_fig: int = bris_two_furlong_pace_fig
        self.bris_four_furlong_pace_fig: int = bris_four_furlong_pace_fig
        self.bris_six_furlong_pace_fig: int = bris_six_furlong_pace_fig
        self.bris_eight_furlong_pace_fig: int = bris_eight_furlong_pace_fig
        self.bris_ten_furlong_pace_fig: int = bris_ten_furlong_pace_fig
        self.bris_late_pace_fig: int = bris_late_pace_fig
        self.bris_speed_rating: int = bris_speed_rating
        self.speed_rating: int = speed_rating
        self.track_variant: int = track_variant
        self.two_furlong_fraction: float = two_furlong_fraction
        self.three_furlong_fraction: float = three_furlong_fraction
        self.four_furlong_fraction: float = four_furlong_fraction
        self.five_furlong_fraction: float = five_furlong_fraction
        self.six_furlong_fraction: float = six_furlong_fraction
        self.seven_furlong_fraction: float = seven_furlong_fraction
        self.eight_furlong_fraction: float = eight_furlong_fraction
        self.ten_furlong_fraction: float = ten_furlong_fraction
        self.twelve_furlong_fraction: float = twelve_furlong_fraction
        self.fourteen_furlong_fraction: float = fourteen_furlong_fraction
        self.sixteen_furlong_fraction: float = sixteen_furlong_fraction
        self.fr1: float = fr1
        self.fr2: float = fr2
        self.fr3: float = fr3
        self.final_time: float = final_time
        self.claimed_code: str = claimed_code
        self.trainer: str = trainer
        self.jockey: str = jockey
        self.apprentice_weight_allowed: int = apprentice_weight_allowed
        self.race_type: str = race_type
        self.age_and_sex_restrictions: str = age_and_sex_restrictions
        self.state_bred_flag: str = state_bred_flag
        self.restricted_qualifier_flag: str = restricted_qualifier_flag
        self.favorite_indicator: str = favorite_indicator
        self.front_bandages_indicator: str = front_bandages_indicator
        self.class_speed_par: int = class_speed_par
        self.bar_shoe: str = bar_shoe
        self.company_line_codes: str = company_line_codes
        self.low_claiming_price_of_race: int = low_claiming_price_of_race
        self.high_claiming_price_of_race: int = high_claiming_price_of_race
        self.start_code: str = start_code

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFilePastPerformance({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFilePastPerformance({ret[:-2]})'

    @staticmethod
    def create(row: list[str], number: PastPerformanceNumber) -> 'SingleFilePastPerformance':
        return SingleFilePastPerformance(
            get_past_performance_date(row, number),
            get_past_performance_days_since_previous_race(row, number),
            get_past_performance_track_code(row, number),
            get_past_performance_bris_track_code(row, number),
            get_past_performance_race_number(row, number),
            get_past_performance_track_condition(row, number),
            get_past_performance_distance(row, number),
            get_past_performance_surface(row, number),
            get_past_performance_special_chute_indicator(row, number),
            get_past_performance_number_of_entrants(row, number),
            get_past_performance_post_position(row, number),
            get_past_performance_equipment(row, number),
            get_past_performance_race_name(row, number),
            get_past_performance_medication(row, number),
            get_past_performance_trip_comment(row, number),
            get_past_performance_winners_name(row, number),
            get_past_performance_second_place_name(row, number),
            get_past_performance_third_place_name(row, number),
            get_past_performance_winners_weight_carried(row, number),
            get_past_performance_second_place_weight_carried(row, number),
            get_past_performance_third_place_weight_carried(row, number),
            get_past_performance_winners_margin(row, number),
            get_past_performance_second_place_margin(row, number),
            get_past_performance_third_place_margin(row, number),
            get_past_performance_extra_comment(row, number),
            get_past_performance_weight(row, number),
            get_past_performance_odds(row, number),
            get_past_performance_entry(row, number),
            get_past_performance_race_classification(row, number),
            get_past_performance_horse_claiming_price(row, number),
            get_past_performance_purse(row, number),
            get_past_performance_start_call_position(row, number),
            get_past_performance_first_call_position(row, number),
            get_past_performance_second_call_position(row, number),
            get_past_performance_gate_call_position(row, number),
            get_past_performance_stretch_position(row, number),
            get_past_performance_finish_position(row, number),
            get_past_performance_start_call_beaten_lengths_leader_margin(row, number),
            get_past_performance_start_call_beaten_lengths(row, number),
            get_past_performance_first_call_beaten_lengths_leader_margin(row, number),
            get_past_performance_first_call_beaten_lengths(row, number),
            get_past_performance_second_call_beaten_lengths_leader_margin(row, number),
            get_past_performance_second_call_beaten_lengths(row, number),
            get_past_performance_first_call_bris_race_shape(row, number),
            get_past_performance_stretch_beaten_lengths_leader_margin(row, number),
            get_past_performance_stretch_beaten_lengths(row, number),
            get_past_performance_finish_beaten_lengths_leader_margin(row, number),
            get_past_performance_finish_beaten_lengths(row, number),
            get_past_performance_second_call_bris_race_shape(row, number),
            get_past_performance_bris_two_furlong_pace_fig(row, number),
            get_past_performance_bris_four_furlong_pace_fig(row, number),
            get_past_performance_bris_six_furlong_pace_fig(row, number),
            get_past_performance_bris_eight_furlong_pace_fig(row, number),
            get_past_performance_bris_ten_furlong_pace_fig(row, number),
            get_past_performance_bris_late_pace_fig(row, number),
            get_past_performance_bris_speed_rating(row, number),
            get_past_performance_speed_rating(row, number),
            get_past_performance_track_variant(row, number),
            get_past_performance_two_furlong_fraction(row, number),
            get_past_performance_three_furlong_fraction(row, number),
            get_past_performance_four_furlong_fraction(row, number),
            get_past_performance_five_furlong_fraction(row, number),
            get_past_performance_six_furlong_fraction(row, number),
            get_past_performance_seven_furlong_fraction(row, number),
            get_past_performance_eight_furlong_fraction(row, number),
            get_past_performance_ten_furlong_fraction(row, number),
            get_past_performance_twelve_furlong_fraction(row, number),
            get_past_performance_fourteen_furlong_fraction(row, number),
            get_past_performance_sixteen_furlong_fraction(row, number),
            get_past_performance_1fr(row, number),
            get_past_performance_2fr(row, number),
            get_past_performance_3fr(row, number),
            get_past_performance_final_time(row, number),
            get_past_performance_claimed_code(row, number),
            get_past_performance_trainer(row, number),
            get_past_performance_jockey(row, number),
            get_past_performance_apprentice_weight_allowed(row, number),
            get_past_performance_race_type(row, number),
            get_past_performance_age_and_sex_restrictions(row, number),
            get_past_performance_state_bred_flag(row, number),
            get_past_performance_restricted_qualifier_flag(row, number),
            get_past_performance_favorite_indicator(row, number),
            get_past_performance_front_bandages_indicator(row, number),
            get_past_performance_class_speed_par(row, number),
            get_past_performance_bar_shoe(row, number),
            get_past_performance_company_line_codes(row, number),
            get_past_performance_low_claiming_price_of_race(row, number),
            get_past_performance_high_claiming_price_of_race(row, number),
            get_past_performance_start_code(row, number),
        )


class SingleFileHorseStats:
    def __init__(self, medication: int,
                 lifetime_record_todays_distance: SingleFileRecord,
                 lifetime_record_todays_track: SingleFileRecord,
                 lifetime_record_turf: SingleFileRecord,
                 lifetime_wet_record: SingleFileRecord,
                 current_year_record: SingleFileRecordWithYear,
                 previous_year_record: SingleFileRecordWithYear,
                 lifetime_record: SingleFileRecord):
        self.medication: int = medication
        self.lifetime_record_todays_distance: SingleFileRecord = lifetime_record_todays_distance
        self.lifetime_record_todays_track: SingleFileRecord = lifetime_record_todays_track
        self.lifetime_record_turf: SingleFileRecord = lifetime_record_turf
        self.lifetime_wet_record: SingleFileRecord = lifetime_wet_record
        self.current_year_record: SingleFileRecordWithYear = current_year_record
        self.previous_year_record: SingleFileRecordWithYear = previous_year_record
        self.lifetime_record: SingleFileRecord = lifetime_record

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileHorseStats({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileHorseStats({ret[:-2]})'

    @staticmethod
    def create(row: list[str]) -> 'SingleFileHorseStats':
        return SingleFileHorseStats(
            get_todays_medication1(row),
            SingleFileRecord(
                get_lifetime_starts_todays_distance(row),
                get_lifetime_wins_todays_distance(row),
                get_lifetime_places_todays_distance(row),
                get_lifetime_shows_todays_distance(row),
                get_lifetime_earnings_todays_distance(row)
            ),
            SingleFileRecord(
                get_lifetime_starts_todays_track(row),
                get_lifetime_wins_todays_track(row),
                get_lifetime_places_todays_track(row),
                get_lifetime_shows_todays_track(row),
                get_lifetime_earnings_todays_track(row)
            ),
            SingleFileRecord(
                get_lifetime_starts_turf(row),
                get_lifetime_wins_turf(row),
                get_lifetime_places_turf(row),
                get_lifetime_shows_turf(row),
                get_lifetime_earnings_turf(row)
            ),
            SingleFileRecord(
                get_lifetime_starts_wet(row),
                get_lifetime_wins_wet(row),
                get_lifetime_places_wet(row),
                get_lifetime_shows_wet(row),
                get_lifetime_earnings_wet(row)
            ),
            SingleFileRecordWithYear(
                get_current_year(row),
                get_current_year_starts(row),
                get_current_year_wins(row),
                get_current_year_places(row),
                get_current_year_shows(row),
                get_current_year_earnings(row)
            ),
            SingleFileRecordWithYear(
                get_previous_year(row),
                get_previous_year_starts(row),
                get_previous_year_wins(row),
                get_previous_year_places(row),
                get_previous_year_shows(row),
                get_previous_year_earnings(row)
            ),
            SingleFileRecord(
                get_lifetime_starts(row),
                get_lifetime_wins(row),
                get_lifetime_places(row),
                get_lifetime_shows(row),
                get_lifetime_earnings(row)
            ),
        )


class SingleFileHorse(Horse):
    def __init__(self, name: str, year_of_birth: int, foaling_month: int, sex: str, color: str, weight: int,
                 sire: str, sires_sire: str, dam: str, dams_sire: str, breeder: str, where: str, post_position: int,
                 trainer: SingleFileTrainer, jockey: SingleFileJockey, owner: SingleFileOwner, mto_ae_indicator: str,
                 program_number: str, morning_line_odds: float, stats: SingleFileHorseStats, equipment_change: int,
                 workouts: list[SingleFileWorkout], bris_run_style_designation: str, quirin_speed_points: int,
                 lifetime_starts_all_weather_surface: int, lifetime_wins_all_weather_surface: int,
                 lifetime_places_all_weather_surface: int, lifetime_shows_all_weather_surface: int,
                 lifetime_earnings_all_weather_surface: int, best_bris_speed_all_weather_surface: int,
                 bris_prime_power_rating: float, past_performances: list[SingleFilePastPerformance],
                 sire_stud_fee: int, best_bris_speed_fast_track: int, best_bris_speed_turf: int,
                 best_bris_speed_off_track: int, best_bris_speed_distance: int, auction_price: int,
                 auction_location: str,
                 dirt_pedigree_rating: str, mud_pedigree_rating: str, turf_pedigree_rating: str,
                 distance_pedigree_rating: str, best_bris_speed_life: int, best_bris_speed_most_recent_year: int,
                 best_bris_speed_second_most_recent_year: int, best_bris_speed_todays_track: int,
                 starts_fast_dirt_track: int, wins_fast_dirt_track: int, places_fast_dirt_track: int,
                 shows_fast_dirt_track: int, earnings_fast_dirt_track: int):
        self.name: str = name
        self.year_of_birth: int = year_of_birth
        self.foaling_month: int = foaling_month
        self.sex: str = sex
        self.color: str = color
        self.weight: int = weight
        self.sire: str = sire
        self.sires_sire: str = sires_sire
        self.dam: str = dam
        self.dams_sire: str = dams_sire
        self.breeder: str = breeder
        self.where: str = where
        self.post_position: int = post_position
        self.trainer: SingleFileTrainer = trainer
        self.jockey: SingleFileJockey = jockey
        self.owner: SingleFileOwner = owner
        self.mto_ae_indicator: str = mto_ae_indicator
        self.program_number: str = program_number
        self.morning_line_odds: float = morning_line_odds
        self.stats: SingleFileHorseStats = stats
        self.equipment_change: int = equipment_change
        self.workouts: list[SingleFileWorkout] = workouts
        self.bris_run_style_designation: str = bris_run_style_designation
        self.quirin_speed_points: int = quirin_speed_points
        self.lifetime_starts_all_weather_surface: int = lifetime_starts_all_weather_surface
        self.lifetime_wins_all_weather_surface: int = lifetime_wins_all_weather_surface
        self.lifetime_places_all_weather_surface: int = lifetime_places_all_weather_surface
        self.lifetime_shows_all_weather_surface: int = lifetime_shows_all_weather_surface
        self.lifetime_earnings_all_weather_surface: int = lifetime_earnings_all_weather_surface
        self.best_bris_speed_all_weather_surface: int = best_bris_speed_all_weather_surface
        self.bris_prime_power_rating: float = bris_prime_power_rating
        self.past_performances: list[SingleFilePastPerformance] = past_performances
        self.sire_stud_fee: int = sire_stud_fee
        self.best_bris_speed_fast_track: int = best_bris_speed_fast_track
        self.best_bris_speed_turf: int = best_bris_speed_turf
        self.best_bris_speed_off_track: int = best_bris_speed_off_track
        self.best_bris_speed_distance: int = best_bris_speed_distance
        self.auction_price: int = auction_price
        self.auction_location: str = auction_location
        self.dirt_pedigree_rating: str = dirt_pedigree_rating
        self.mud_pedigree_rating: str = mud_pedigree_rating
        self.turf_pedigree_rating: str = turf_pedigree_rating
        self.distance_pedigree_rating: str = distance_pedigree_rating
        self.best_bris_speed_life: int = best_bris_speed_life
        self.best_bris_speed_most_recent_year: int = best_bris_speed_most_recent_year
        self.best_bris_speed_second_most_recent_year: int = best_bris_speed_second_most_recent_year
        self.best_bris_speed_todays_track: int = best_bris_speed_todays_track
        self.starts_fast_dirt_track: int = starts_fast_dirt_track
        self.wins_fast_dirt_track: int = wins_fast_dirt_track
        self.places_fast_dirt_track: int = places_fast_dirt_track
        self.shows_fast_dirt_track: int = shows_fast_dirt_track
        self.earnings_fast_dirt_track: int = earnings_fast_dirt_track

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileHorse({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileHorse({ret[:-2]})'

    @staticmethod
    def create(row: list[str]) -> 'SingleFileHorse':
        return SingleFileHorse(
            get_horse_name(row),
            get_horse_year_of_birth(row),
            get_horse_foaling_month(row),
            get_horse_sex(row),
            get_horse_color(row),
            get_horse_weight(row),
            get_horse_sire(row),
            get_horse_sires_sire(row),
            get_horse_dam(row),
            get_horse_dams_sire(row),
            get_horse_breeder(row),
            get_horse_where(row),
            get_horse_program_post_position(row),
            SingleFileTrainer.create(row),
            SingleFileJockey.create(row),
            SingleFileOwner.create(row),
            get_mto_ae_indicator(row),
            get_program_number(row),
            get_morning_line_odds(row),
            SingleFileHorseStats.create(row),
            get_equipment_change(row),
            [
                SingleFileWorkout.create(row, workout_number) for workout_number in WorkoutNumber
            ],
            get_bris_run_style_designation(row),
            get_quirin_speed_points(row),
            get_lifetime_starts_all_weather_surface(row),
            get_lifetime_wins_all_weather_surface(row),
            get_lifetime_places_all_weather_surface(row),
            get_lifetime_shows_all_weather_surface(row),
            get_lifetime_earnings_all_weather_surface(row),
            get_best_bris_speed_all_weather_surface(row),
            get_bris_prime_power_rating(row),
            [
                SingleFilePastPerformance.create(row, past_performance_number) for
                past_performance_number in PastPerformanceNumber
            ],
            get_sire_stud_fee(row),
            get_best_bris_speed_fast_track(row),
            get_best_bris_speed_turf(row),
            get_best_bris_speed_off_track(row),
            get_best_bris_speed_distance(row),
            get_horse_auction_price(row),
            get_horse_auction_location(row),
            get_bris_dirt_pedigree_rating(row),
            get_bris_mud_pedigree_rating(row),
            get_bris_turf_pedigree_rating(row),
            get_bris_distance_pedigree_rating(row),
            get_best_bris_speed_life(row),
            get_best_bris_speed_most_recent_year(row),
            get_best_bris_speed_second_most_recent_year(row),
            get_best_bris_speed_todays_track(row),
            get_horse_starts_fast_dirt_track(row),
            get_horse_wins_fast_dirt_track(row),
            get_horse_places_fast_dirt_track(row),
            get_horse_shows_fast_dirt_track(row),
            get_horse_earnings_fast_dirt_track(row),
        )
