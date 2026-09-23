# Component Diagram

```text
+------------------------------------------------------+
|                 Heart Rate Project                  |
+------------------------------------------------------+
|                                                      |
| heart_rate_calculator.py  -> main controller        |
| calculator.py             -> BPM calculation        |
| validator.py              -> input validation       |
| classifier.py             -> BPM classification     |
| display.py                -> result presentation    |
| history.py                -> JSON storage           |
| config.py                 -> project constants      |
|                                                      |
+-------------------------------+----------------------+
                                |
                                v
                       data/history.json
```

Each module has one main responsibility, making the project easier to understand and maintain.
