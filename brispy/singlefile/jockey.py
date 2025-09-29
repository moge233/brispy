#! python3


from dataclasses import dataclass

from brispy.abstract import Jockey
from .utils import get_apprentice_weight_allowed, get_todays_jockey, get_todays_jockey_starts, get_todays_jockey_wins, \
    get_todays_jockey_places, get_todays_jockey_shows, get_jockey_current_year_starts, get_jockey_current_year_wins, \
    get_jockey_current_year_places, get_jockey_current_year_shows, get_jockey_current_year_roi, \
    get_jockey_previous_year_starts, get_jockey_previous_year_wins, get_jockey_previous_year_places, \
    get_jockey_previous_year_shows, get_jockey_previous_year_roi, get_jockey_at_distance_on_turf_label, \
    get_jockey_at_distance_on_turf_starts, get_jockey_at_distance_on_turf_wins, get_jockey_at_distance_on_turf_places, \
    get_jockey_at_distance_on_turf_shows, get_jockey_at_distance_on_turf_roi, get_jockey_at_distance_on_turf_earnings


@dataclass
class SingleFileJockey(Jockey):
    name: str
    apprentice_weight_allowed: int
    starts: int
    wins: int
    place: int
    shows: int
    current_year_starts: int
    current_year_wins: int
    current_year_places: int
    current_year_shows: int
    current_year_roi: float
    preivous_year_starts: int
    previous_year_wins: int
    previous_year_places: int
    previous_year_shows: int
    previous_year_roi: float
    at_distance_on_turf_label: str
    at_distance_on_turf_starts: int
    at_distance_on_turf_wins: int
    at_distance_on_turf_places: int
    at_distance_on_turf_shows: int
    at_distance_on_turf_roi: float
    at_distance_on_turf_earnings: int

    @staticmethod
    def create(row: list[str]) -> 'SingleFileJockey':
        return SingleFileJockey(
            get_todays_jockey(row),
            get_apprentice_weight_allowed(row),
            get_todays_jockey_starts(row),
            get_todays_jockey_wins(row),
            get_todays_jockey_places(row),
            get_todays_jockey_shows(row),
            get_jockey_current_year_starts(row),
            get_jockey_current_year_wins(row),
            get_jockey_current_year_places(row),
            get_jockey_current_year_shows(row),
            get_jockey_current_year_roi(row),
            get_jockey_previous_year_starts(row),
            get_jockey_previous_year_wins(row),
            get_jockey_previous_year_places(row),
            get_jockey_previous_year_shows(row),
            get_jockey_previous_year_roi(row),
            get_jockey_at_distance_on_turf_label(row),
            get_jockey_at_distance_on_turf_starts(row),
            get_jockey_at_distance_on_turf_wins(row),
            get_jockey_at_distance_on_turf_places(row),
            get_jockey_at_distance_on_turf_shows(row),
            get_jockey_at_distance_on_turf_roi(row),
            get_jockey_at_distance_on_turf_earnings(row)
        )
