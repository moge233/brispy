# brispy
A wrapper for Brisnet single-file past-performance data files (`.DRF`).

```python
from brispy.singlefile import SingleFile

card = SingleFile.create("CDX1115.DRF")
for row in card.rows:
    print(row.race.number, row.horse.program_number, row.horse.name)
```

## Development

```shell
python -m pip install -e ".[test]"
python -m coverage run -m unittest discover -s brispy -p "test_*.py" -t .
python -m coverage report
```

CI runs the same commands and requires 100% line and branch coverage.
