#! python3


from abc import ABC, abstractmethod
from enum import Enum


class DataFile(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def create(path: str) -> 'DataFile':
        raise NotImplementedError


class Trainer(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def create(row: list[str]) -> 'Trainer':
        raise NotImplementedError


class Jockey(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def create(row: list[str]) -> 'Jockey':
        raise NotImplementedError


class Owner(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def create(row: list[str]) -> 'Owner':
        raise NotImplementedError


class Horse(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def create(row: list[str]) -> 'Horse':
        raise NotImplementedError


class SpecialEnum(Enum):
    pass


class Workout(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def create(row: list[str], number: SpecialEnum) -> 'Workout':
        raise NotImplementedError


class PastPerformance(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def create(row: list[str], number: SpecialEnum) -> 'PastPerformance':
        raise NotImplementedError
