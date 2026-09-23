# Heart Rate Calculator using Python

## 1. Project Overview

The Heart Rate Calculator is a simple Python command-line project. It calculates a person's heart rate in Beats Per Minute (BPM) from the number of heartbeats counted and the time taken to count them.

The original project formula is:

**BPM = (Number of Beats / Time in Seconds) × 60**

The project has been extended with input validation, heart-rate classification, JSON history storage, testing, documentation and modular Python files.

## 2. Features

- Takes the user's name.
- Takes the number of heartbeats counted.
- Takes the measurement time in seconds.
- Calculates BPM using the original formula.
- Displays the complete calculation.
- Gives a simple BPM range message.
- Handles invalid input.
- Saves calculation history in JSON.
- Includes automated tests.
- Uses multiple Python modules.

## 3. Technologies Used

- Python 3.x
- Command Line / Terminal
- JSON
- Git and GitHub
- pytest for optional automated testing

## 4. Project Structure

```text
Heart_Rate_Calculator_Complete/
│
├── heart_rate_calculator.py
├── calculator.py
├── validator.py
├── classifier.py
├── display.py
├── history.py
├── config.py
├── requirements.txt
├── README.md
├── statement.md
│
├── data/
│   └── history.json
│
├── tests/
│   ├── test_calculator.py
│   └── test_validator.py
│
└── docs/
    ├── system_architecture.md
    ├── workflow.md
    ├── use_case.md
    ├── sequence.md
    ├── component.md
    └── storage_design.md
```

## 5. How to Run

Open a terminal in the project folder and run:

```bash
python heart_rate_calculator.py
```

Enter:
1. Your name
2. Number of heartbeats counted
3. Time in seconds

## 6. Example

```text
enter your name: xyz
hello xyz!
enter the number of heartbeats counted : 60
enter the time in seconds: 60

YOUR RESULT
name: xyz
heartbeats counted: 60
time: 60 seconds
heart rate: 60.0 BPM
```

## 7. Formula

```text
BPM = (Number of Beats / Time in Seconds) × 60
```

Example:

```text
BPM = (60 / 60) × 60
BPM = 60 BPM
```

## 8. Testing

If pytest is installed:

```bash
pytest
```

The tests check:
- BPM calculation
- Decimal results
- Low/normal/high classification

## 9. GitHub

```bash
git init
git add .
git commit -m "Complete heart rate calculator project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## 10. Limitations

- It depends on the accuracy of user input.
- It does not use a heart-rate sensor.
- It is not a medical diagnostic tool.
- The BPM range message is a simple educational classification.

## 11. Future Enhancements

- Add a graphical user interface.
- Connect a heart-rate sensor.
- Add charts.
- Add CSV export.
- Add more detailed user history.
