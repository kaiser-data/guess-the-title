import json
import sys
import os
from pathlib import Path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

JSON_FILE_PATH = Path(__file__).parent.parent / "data" / "high_score.json"


def reading_highscores():
    """
    Reads the high scores from a JSON file.

    Returns:
        dict: A dictionary containing high scores, where keys are player names
              and values are their corresponding scores.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data", JSON_FILE_PATH)

    with open(file_path, "r") as fileobj:
        highscores = json.load(fileobj)
        return highscores


def saving_highscores(data):
    """
    Saves high scores to a JSON file.

    Parameter:
        data (dict): A dictionary containing high scores, where keys are player names
                     and values are their corresponding scores.

    Returns:
        None: The data is saved to the high score file.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data", JSON_FILE_PATH)

    with open(file_path, "w") as fileobj:
        json.dump(data, fileobj)


def get_scores():
    """
    Retrieves and prints the top 5 high scores.

    Returns:
        list: A list of tuples containing player names and their scores, sorted in
              descending order of scores.
    """
    all_scores = reading_highscores()
    sorted_scores = sorted(all_scores.items(), key=lambda x: x[1],
                           reverse=True)

    for name, score in sorted_scores[:5]:
        print(f"{name}: {score}")

    return sorted_scores


def set_score(name, score):
    """
    Updates or adds a new high score for a player.

    Parameters:
        name (str): The player's name.
        score (int): The score to be set for the player.

    Returns:
        None: The high score data is saved after the score is updated or added.
    """
    data = reading_highscores()
    is_account_present_greater_than_score = False
    is_account_new = True

    for data_name, data_score in data.items():
        if name == data_name and score > data_score:
            data[name] = score
            is_account_present_greater_than_score = True
        if name == data_name:
            is_account_new = False

    if is_account_new:
        data[name] = score
        saving_highscores(data)

    if is_account_present_greater_than_score:
        saving_highscores(data)
