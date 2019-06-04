# TimeService

Code challenge

```bash
git clone https://github.com/dr-jgsmith/TimeService.git

cd TimeService
pip install .
```

# Usage Example

```python
from TimeService.timeservice import *

timedata = TimeMachine('12:55 pm', 10).add_minutes()`
print(timedata)
```

Output results in 1:05 AM
