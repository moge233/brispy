#! python3
"""Build Brisnet single-file rows field by field for tests."""

from brispy.singlefile.index import SingleFileIndex

FIELD_COUNT = 1435
"""Fields per row in the Brisnet single-file format."""


def build_row(value: str = '', **fields: str) -> list[str]:
    """A full-width row with every field set to ``value``.

    Args:
        value: Text for every field not named in ``fields``.
        fields: Field values keyed by ``SingleFileIndex`` member name
            without the ``_INDEX`` suffix, e.g. ``HORSE_NAME='Example'``.

    Returns:
        The row.
    """
    row = [value] * FIELD_COUNT
    for name, text in fields.items():
        row[SingleFileIndex[f'{name}_INDEX'].value] = text
    return row
