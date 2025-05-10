# Home

##  Welcome to **iracing\_garage**! 🏎️

This is a simple and free Python wrapper around the [iRacing API](https://forums.iracing.com/discussion/15068/general-availability-of-data-api/p1), created for the awesome iRacing community. Whether you're building a tool, analyzing your races, or just love data — this is your pit crew in code form. 😎

[Github Repository](https://github.com/dangkv/iracing_garage){ .md-button }

---

## 🚀 Getting Started

### 1. Install the package 📦

```bash
pip install iracing-garage
```

(Optional: consider installing in a virtual environment)

---

### 2. Authentication 🛡️

You'll need to log in with your iRacing email and password (this uses the same method the iRacing web portal does).

```python
from iracing_garage import iRacingGarage

email = 'maxv@gmail.com'
password = 'hotwheels'

iracing = iRacingGarage(email, password)
```

> 🔒 *This iRacing Garage does not store your credentials. It's all handled securely at runtime.*

---

## 🔍 What Can You Do?


After logging in, you can access a bunch of data in JSON format from the iRacing API.
Here are some examples:

### Get Cars 🚗

```python hl_lines="1"
cars = iracing.car.get()
print(cars)
```

### Get Tracks 🏁

```python hl_lines="1"
tracks = iracing.track.get()
print(tracks)
```

### Get Driver Stats 📊

```python hl_lines="2"
cust_id = 123456
driver_data = iracing.stats.summary(cust_id)
print(driver_data)
```

### Get Race Results 🏆

```python hl_lines="3"
subsession_id = 654321
simsession_number = 0
results = iracing.results.get(subsession_id, simsession_number)
print(results)
```
#### Check out the [Data Endpoints](https://dangkv.github.io/iracing_garage/data-endpoints/) page for more data points!!

---

## 📬 Contact

* Maintainer: [dangkv](https://github.com/dangkv) + [hmkamel](https://github.com/hmkamel)

---

## 🏁 Final Lap

Enjoy the ride. 🏎️💨

[Getting Started](getting-started.md){ .md-button }

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
