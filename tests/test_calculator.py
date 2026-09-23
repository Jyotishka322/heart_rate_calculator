import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from calculator import calculate_heart_rate


def test_60_beats_in_60_seconds():
    assert calculate_heart_rate(60, 60) == 60


def test_30_beats_in_30_seconds():
    assert calculate_heart_rate(30, 30) == 60


def test_75_beats_in_60_seconds():
    assert calculate_heart_rate(75, 60) == 75


def test_fractional_result():
    assert round(calculate_heart_rate(50, 45), 2) == 66.67
