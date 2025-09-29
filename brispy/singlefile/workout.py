#! python3


from dataclasses import dataclass

from brispy.abstract import Workout
from .utils import get_workout_date, get_workout_time, get_workout_track, get_workout_distance, \
    get_workout_track_condition, get_workout_description, get_workout_main_inner_track_indicator, \
    get_workout_number_of_works, get_workout_rank, WorkoutNumber


@dataclass
class SingleFileWorkout(Workout):
    date: str
    time: str
    track: str
    distance: int
    track_condition: str
    description: str
    main_inner_track_indicator: str
    number_of_works: int
    rank: str

    @staticmethod
    def create(row: list[str], number: WorkoutNumber) -> 'SingleFileWorkout':
        return SingleFileWorkout(
            get_workout_date(row, number),
            get_workout_time(row, number),
            get_workout_track(row, number),
            get_workout_distance(row, number),
            get_workout_track_condition(row, number),
            get_workout_description(row, number),
            get_workout_main_inner_track_indicator(row, number),
            get_workout_number_of_works(row, number),
            get_workout_rank(row, number),
        )
