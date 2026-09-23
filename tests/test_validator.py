import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validator import get_valid_measurement
from classifier import classify_heart_rate


def test_classification_low():
    assert classify_heart_rate(59) == "Below 60 BPM"


def test_classification_normal():
    assert classify_heart_rate(60) == "60-100 BPM"
    assert classify_heart_rate(100) == "60-100 BPM"


def test_classification_high():
    assert classify_heart_rate(101) == "Above 100 BPM"
