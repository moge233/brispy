#! python3


from dataclasses import dataclass

from .bris import SingleFileBrisPars
from .combo import SingleFileTrainerJockeyCombo
from .horse import SingleFileHorse
from .jockey import SingleFileJockey
from .owner import SingleFileOwner
from .race import SingleFileRace
from .trainer import SingleFileTrainer


@dataclass
class SingleFileRow:
    race: SingleFileRace                                #
    horse: SingleFileHorse                              #
    trainer: SingleFileTrainer                          #
    jockey: SingleFileJockey                            #
    owner: SingleFileOwner                              #
    bris_pars: SingleFileBrisPars                       #
    trainer_jockey_combo: SingleFileTrainerJockeyCombo  #

    @staticmethod
    def create(row: list[str]) -> 'SingleFileRow':
        return SingleFileRow(
            race=SingleFileRace.create(row),
            horse=SingleFileHorse.create(row),
            trainer=SingleFileTrainer.create(row),
            jockey=SingleFileJockey.create(row),
            owner=SingleFileOwner.create(row),
            bris_pars=SingleFileBrisPars.create(row),
            trainer_jockey_combo=SingleFileTrainerJockeyCombo.create(row)
        )
