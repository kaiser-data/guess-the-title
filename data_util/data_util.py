import json
import sys
import os
from pathlib import Path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

JSON_FILE_PATH = Path(__file__).parent.parent / "data" / "high_score.json"


def reading_highscores():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data", JSON_FILE_PATH)

    with open(file_path, "r") as fileobj:
        highscores = json.load(fileobj)
        return highscores


def saving_highscores(data):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data", JSON_FILE_PATH)

    with open(file_path, "w") as fileobj:
        json.dump(data, fileobj)


def get_scores():
    all_scores = reading_highscores()
    sorted_scores = sorted(all_scores.items(), key=lambda x: x[1],
                           reverse=True)

    for name, score in sorted_scores[:5]:
        print(f"{name}: {score}")

    return sorted_scores


def set_score(name, score):
    data = reading_highscores()
    for data_name, data_score in data.items():
        if score > data_score:
            data[name] = score
    saving_highscores(data)
