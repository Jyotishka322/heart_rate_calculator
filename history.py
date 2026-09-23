"""Simple JSON history storage module."""

import json
from pathlib import Path

HISTORY_FILE = Path("data/history.json")


def save_result(name, beats, time, heart_rate, category):
    """Save one calculation to a JSON file."""
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    records = []

    if HISTORY_FILE.exists():
        try:
            records = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            records = []

    records.append({
        "name": name,
        "beats": beats,
        "time_seconds": time,
        "heart_rate_bpm": round(heart_rate, 2),
        "category": category
    })

    HISTORY_FILE.write_text(
        json.dumps(records, indent=4),
        encoding="utf-8"
    )


def get_history():
    """Return all saved calculations."""
    if not HISTORY_FILE.exists():
        return []

    try:
        return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
