# brispy
A wrapper for Brisnet single-file past-performance data files (`.DRF`).

```python
from brispy.singlefile import SingleFile

card = SingleFile.create("CDX1115.DRF")
for row in card.rows:
    print(row.race.number, row.horse.program_number, row.horse.name)
```

Fields are read strictly. A blank field is `None`. A field that can't be read
as its type, or a row too short to hold it, raises `brispy.singlefile.FieldError`.
The error names the field (with its 1-based Brisnet field number), the value,
and, from `SingleFile.create`, the file and row.

## Development

```shell
python -m pip install -e ".[test]"
python -m coverage run -m unittest discover -s brispy -p "test_*.py" -t .
python -m coverage report
```

CI runs the same commands and requires 100% line and branch coverage.
