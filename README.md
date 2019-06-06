# TimeService

Code challenge

```bash
git clone https://github.com/dr-jgsmith/TimeService.git

cd TimeService
pip install .
```

# Usage Example

```python
from TimeService.timeservice import TimeMachine

timedata = TimeMachine('12:55 pm', 10).add_minutes()
print(timedata)
```

Or

```python
from TimeService.timeservice import TimeMachine

timedata = TimeMachine('12:55 pm', 10)
new_time = timedata.add_minutes()
print(new_time)
```

Output results in 1:05 AM

# Tests
Tests were created with the pytest module.

```bash
pip install pytest
cd tests
```

Run pytest in your terminal from within the tests directory.

```bash
$ home/usr/local/TimeService/tests/>pytest
```

