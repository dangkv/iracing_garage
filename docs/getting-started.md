# Getting Started

### Requirements
*  Python 3

### Steps
 1. Install
 2. Authenticate

 ---

#### How to Install

```bash
pip install iracing-garage
```

(Optional: consider installing in a virtual environment)

#### How to Authenticate
```python
from iracing_garage import iRacingGarage


username = "<UR_USERNAME>"
password = "<UR_PASSWORD>"

iRacing = iRacingGarage(username, password)

```
