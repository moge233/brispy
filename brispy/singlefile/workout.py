#! python3


from brispy.abstract import Workout
from .utils import get_workout_date, get_workout_time, get_workout_track, get_workout_distance, \
    get_workout_track_condition, get_workout_description, get_workout_main_inner_track_indicator, \
    get_workout_number_of_works, get_workout_rank, WorkoutNumber


class SingleFileWorkout(Workout):

    def __init__(self, date: str, time: str, track: str, distance: int, track_condition: str, description: str,
                 main_inner_track_indicator: str, number_of_works: int, rank: str):
        super().__init__()
        self.date: str = date
        self.time: str = time
        self.track: str = track
        self.distance: int = distance
        self.track_condition: str = track_condition
        self.description: str = description
        self.main_inner_track_indicator: str = main_inner_track_indicator
        self.number_of_works: int = number_of_works
        self.rank: str = rank

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileWorkout({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'SingleFileWorkout({ret[:-2]})'

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
