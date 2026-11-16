#! python3


from unittest import TestCase

from brispy import abstract


class TestAbstractFactories(TestCase):
    """Each abstract factory refuses to run, and subclasses initialise."""

    def test_factories_raise(self):
        calls = [
            lambda: abstract.DataFile.create('x'),
            lambda: abstract.Trainer.create([]),
            lambda: abstract.Jockey.create([]),
            lambda: abstract.Owner.create([]),
            lambda: abstract.Horse.create([]),
            lambda: abstract.Workout.create([], abstract.SpecialEnum),
            lambda: abstract.PastPerformance.create([], abstract.SpecialEnum),
        ]
        for call in calls:
            with self.subTest(call=call):
                with self.assertRaises(NotImplementedError):
                    call()

    def test_subclasses_initialise(self):
        bases = [
            abstract.DataFile, abstract.Trainer, abstract.Jockey, abstract.Owner,
            abstract.Horse, abstract.Workout, abstract.PastPerformance,
        ]
        for base in bases:
            concrete = type('Concrete', (base,), {'create': staticmethod(lambda *a: None)})
            with self.subTest(base=base.__name__):
                self.assertIsInstance(concrete(), base)
