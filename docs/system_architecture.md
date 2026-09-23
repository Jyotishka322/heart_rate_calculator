# System Architecture

```text
                    +----------------+
                    |      User      |
                    +-------+--------+
                            |
                            v
              +---------------------------+
              | heart_rate_calculator.py  |
              |       Main Program        |
              +-------------+-------------+
                            |
        +-------------------+-------------------+
        |                   |                   |
        v                   v                   v
+---------------+   +---------------+   +---------------+
|  validator.py |   | calculator.py |   | classifier.py |
| Input checks  |   | BPM formula   |   | BPM category  |
+---------------+   +---------------+   +---------------+
                            |
                            v
                    +---------------+
                    |  display.py   |
                    | Result output |
                    +-------+-------+
                            |
                            v
                    +---------------+
                    |  history.py   |
                    | JSON storage  |
                    +-------+-------+
                            |
                            v
                    +---------------+
                    | history.json  |
                    +---------------+
```
