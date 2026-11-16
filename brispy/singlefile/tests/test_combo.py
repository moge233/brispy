#! python3


from unittest import TestCase

from brispy.singlefile import SingleFileTrainerJockeyCombo
from .rowbuilder import build_row


class TestTrainerJockeyComboRoi(TestCase):
    """Field 223 (T/J combo $2 ROI, 365 days) holds decimals such as -0.60."""

    def test_lifetime_roi_keeps_its_decimals(self):
        row = build_row('0', TRAINER_JOCKEY_COMBO_ROI='-0.60')
        self.assertEqual(SingleFileTrainerJockeyCombo.create(row).lifetime_roi, -0.60)

    def test_meet_roi_keeps_its_decimals(self):
        row = build_row('0', TRAINER_JOCKEY_COMBO_MEET_ROI='1.25')
        self.assertEqual(SingleFileTrainerJockeyCombo.create(row).meet_roi, 1.25)
