#! python3


from unittest import TestCase

from brispy.singlefile import SingleFileRow
from brispy.singlefile.index import SingleFileIndex
from .rowbuilder import FIELD_COUNT, build_row


class TestEveryReader(TestCase):
    """Every field reader runs on a full row of parseable values."""

    def test_full_row(self):
        row = SingleFileRow.create(build_row('7'))
        self.assertEqual(row.race.track, '7')
        self.assertEqual(row.race.number, 7)
        self.assertEqual(row.horse.morning_line_odds, 7.0)
        self.assertEqual(row.race.conditions, '7')
        self.assertEqual(row.race.complete_race_conditions, '7' * 6)
        self.assertEqual(row.race.wager_types, '7' * 9)
        self.assertEqual(len(row.horse.past_performances), 10)
        self.assertEqual(len(row.horse.workouts), 12)
        self.assertEqual(row.horse.past_performances[9].final_time, 7.0)

    def test_short_row_falls_back(self):
        # Current behaviour: a field that is missing or unparseable reads as
        # '' / 0 / 0.0. A later change makes this strict.
        row = SingleFileRow.create([])
        self.assertEqual(row.race.track, '')
        self.assertEqual(row.race.number, 0)
        self.assertEqual(row.horse.morning_line_odds, 0.0)

    def test_unparseable_numbers_fall_back(self):
        row = SingleFileRow.create(build_row('x'))
        self.assertEqual(row.race.number, 0)
        self.assertEqual(row.horse.morning_line_odds, 0.0)


class TestIndexMatchesBrisnetSpec(TestCase):
    """Spot checks against Brisnet's single-file data structure (1-based field numbers)."""

    SPEC_FIELDS = {
        'TRACK': 1, 'DATE': 2, 'RACE_NUMBER': 3, 'POST_POSITION': 4, 'ENTRY': 5,
        'DISTANCE': 6, 'SURFACE': 7, 'RACE_TYPE': 9, 'AGE_SEX_RESTRICTIONS': 10,
        'CLASSIFICATION': 11, 'PURSE': 12, 'CLAIMING_PRICE': 13, 'PROGRAM_NUMBER': 43,
        'MORNING_LINE_ODDS': 44, 'HORSE_NAME': 45, 'BRIS_PRIME_POWER_RATING': 251,
        'LOW_CLAIMING_PRICE': 238, 'STATE_BRED_FLAG': 239,
        'PAST_PERFORMANCE_DATE1': 256, 'PAST_PERFORMANCE_TRACK_CODE1': 276,
        'PAST_PERFORMANCE_BRIS_TRACK_CODE1': 286, 'PAST_PERFORMANCE_RACE_NUMBER1': 296,
        'PAST_PERFORMANCE_DISTANCE1': 316, 'PAST_PERFORMANCE_SURFACE1': 326,
        'PAST_PERFORMANCE_FINISH_POSITION1': 616, 'PAST_PERFORMANCE_FINISH_BEATEN_LENGTHS1': 746,
        'PAST_PERFORMANCE_TRACK_VARIANT1': 866, 'PAST_PERFORMANCE_TWO_FURLONG_FRACTION1': 876,
        'PAST_PERFORMANCE_FINAL_TIME1': 1036, 'PAST_PERFORMANCE_RACE_TYPE1': 1086,
        'PAST_PERFORMANCE_AGE_AND_SEX_RESTRICTIONS1': 1096,
        'PAST_PERFORMANCE_STATE_BRED_FLAG1': 1106, 'POST_TIME_PACIFIC_MILITARY': 1418,
        'TODAYS_EQUIBASE_ABBREVIATED_RACE_CONDITIONS': 1429,
    }

    def test_spec_fields(self):
        for name, field in self.SPEC_FIELDS.items():
            with self.subTest(name=name):
                self.assertEqual(SingleFileIndex[f'{name}_INDEX'].value, field - 1)

    def test_every_index_fits_a_row(self):
        self.assertLess(max(member.value for member in SingleFileIndex), FIELD_COUNT)


class TestStandaloneReaders(TestCase):
    """Public readers that no row class calls."""

    def test_standalone_readers(self):
        from brispy.singlefile import utils

        row = build_row('7')
        self.assertEqual(utils.get_todays_medication2(row), 7)
        self.assertEqual(utils.get_days_since_last_race(row), 7)
        self.assertEqual(utils.get_post_times_by_region(row), '7')
        for number in range(1, 7):
            reader = getattr(utils, f'get_complete_race_conditions{number}')
            with self.subTest(number=number):
                self.assertEqual(reader(row), '7')
