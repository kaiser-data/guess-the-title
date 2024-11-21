import sys
import os
import time
from tkinter import StringVar
import random

from customtkinter import CTkInputDialog

from data_util.data_util import set_score

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_util.api_util import *
from frame_util.frame_util import *

player_name = "name"
global var_round
global var_life
global var_score
global counter_round, counter_life, counter_score


def initialize_variables():
    """
    Initializes game variables such as player name, round, life, and score.
    Prompts the user for their name if it hasn't been set yet.
    Also initializes the `StringVar` objects for round, life, and score display.

    Returns:
        None
    """
    global counter_round, counter_life, counter_score, player_name, var_life, var_round, var_score

    if player_name == "name":
        dialog = CTkInputDialog(text="Please enter your name: ",
                                title="Player Name")

        player_name = dialog.get_input()

    counter_life = 3
    counter_round = 1
    counter_score = 0
    var_life = StringVar()
    var_life.set(f"Lives: 3")
    var_round = StringVar()
    var_round.set(f"Round: 1")
    var_score = StringVar()
    var_score.set(f"Score: 0")

    var_round.set(f"Round: {counter_round}")
    var_life.set(f"Life: {counter_life}")
    var_score.set(f"Score: {counter_score}")


def generate_options(title):
    """
    Generates multiple answer options for the game, shuffling the correct answer
    with other randomly fetched titles from the API.

    Parameters:
        title (str): The correct answer to be included in the options list.

    Returns:
        list: A shuffled list of options, including the correct answer and three random titles.
    """
    options = [title, ]
    time.sleep(1)
    for i in range(3):
        return_value = get_the_title_summary()
        options.append(return_value["title"])
    random.shuffle(options)
    return options


def get_data_from_api():
    """
    Fetches data related to a title from an Wikipedia API, including its summary,
    categories, and an image link, and prepares it for the game.

    Returns:
        tuple: A tuple containing the title, a truncated summary,
               hints (categories), and shuffled options for the game.
    """
    title, summary, image_link = get_title_and_summary_imagelink()
    summary = remove_title_from_summary(title, summary)

    categories = get_the_title_categories(title)

    download_image(image_link, "image.jpg")

    # creates options
    options = generate_options(title)

    hints = []
    for word in categories.split("Category:")[1:]:
        hints.append(word.split("\'")[0])

    hints = f"\nCategories: {'; '.join(str(index + 1) + ". " + hints[index] for index in range(3))}"
    return title, summary[:150], hints, options


def remove_title_from_summary(title, summary):
    """
    Removes the title from the summary text by replacing all occurrences of the title
    (in various cases) with a placeholder.

    Parameters:
        title (str): The title to be removed from the summary.
        summary (str): The summary text to process.

    Returns:
        str: The summary text with the title replaced by '?'.
    """
    title_words = title.split()
    title = remove_special_characters(title)
    title_words = set(title.split() + title_words)
    summary_r_title = summary
    for word in title_words:
        summary_r_title = summary_r_title.replace(word, "?")
        summary_r_title = summary_r_title.replace(word.lower(), "?")
        summary_r_title = summary_r_title.replace(word.upper(), "?")
        summary_r_title = summary_r_title.replace(
            word[0].upper() + word[1:].lower(), "?")

    summary_r_title = summary_r_title[:2] + "".join(
        summary_r_title[index] for index in range(2, len(summary_r_title))
        if "?" not in summary_r_title[index - 2:index] or summary_r_title[
            index] != "?")
    return summary_r_title


def new_game(main_frame, frames):
    """
    Starts a new game by clearing the main frame, displaying the new game data,
    and initiating the game cycle.

    Parameters:
        main_frame (CTkFrame): The frame in which the game content is displayed.
        frames (dict): A dictionary containing the different frames of the game.

    Returns:
        None
    """
    while True:
        try:
            clearFrame(main_frame)
            generate_header(main_frame, player_name, var_round, var_life,
                            var_score)
            title, summary, hints, options = get_data_from_api()
            generate_new_set_of_data(main_frame, frames, summary, title,
                                     options,
                                     hints)
        except Exception as e:
            pass
        else:
            break;


def create_button(button_frame, l_shuffled):
    """
    Creates and returns a custom button widget in the provided frame.

    Parameters:
        button_frame (CTkFrame): The frame in which the button will be placed.
        l_shuffled (str): The text to be displayed on the button.

    Returns:
        CTkButton: The created button widget with the specified text.
    """
    return ck.CTkButton(button_frame, text=l_shuffled)


def generate_new_set_of_data(main_frame, frames, summary, title,
                             options,
                             hints):
    """
    Generates a new set of data for the game, including options, hints,
    a summary of the title, and an image. It also creates the game buttons.

    Parameters:
        main_frame (CTkFrame): The frame in which to display the new game content.
        frames (dict): A dictionary containing the different frames of the game.
        summary (str): A truncated summary of the title to be displayed.
        title (str): The correct answer.
        options (list): A list of shuffled options (including the correct answer).
        hints (str): A string of category hints related to the title.
    """
    l_shuffled = options

    image = Image.open("image.jpg")
    tk_image = CTkImage(light_image=image, dark_image=image, size=(400, 400))

    image_label = ck.CTkLabel(main_frame, text="", image=tk_image)
    image_label.pack(pady=10, anchor="center")

    label_summary = ck.CTkLabel(main_frame, text=f"{summary}",
                                font=("Arial", 16),
                                fg_color="transparent", width=300)
    label_summary._label.config(wrap=800)
    label_summary.pack(pady=10, anchor="center")

    button_frame = ck.CTkFrame(main_frame, width=750, height=550)

    button1 = create_button(button_frame, l_shuffled[0])
    button1.configure(font=("Arial", 16),
                      command=lambda: answer_from_user(l_shuffled[0], title,
                                                       main_frame, frames,
                                                       image_label))

    button2 = create_button(button_frame, l_shuffled[1])
    button2.configure(font=("Arial", 16),
                      command=lambda: answer_from_user(l_shuffled[1], title,
                                                       main_frame, frames,
                                                       image_label))

    button3 = create_button(button_frame, l_shuffled[2])
    button3.configure(font=("Arial", 16),
                      command=lambda: answer_from_user(l_shuffled[2], title,
                                                       main_frame, frames,
                                                       image_label))

    button4 = create_button(button_frame, l_shuffled[3])
    button4.configure(font=("Arial", 16),
                      command=lambda: answer_from_user(l_shuffled[3], title,
                                                       main_frame, frames,
                                                       image_label))

    button1.grid(row=0, column=0, padx=20, pady=20)
    button2.grid(row=0, column=1, padx=20, pady=20)
    button3.grid(row=1, column=0, padx=20, pady=20)
    button4.grid(row=1, column=1, padx=20, pady=20)

    button_frame.pack(anchor="center")

    label_hint = ck.CTkLabel(main_frame, text=f"Hint? {hints}",
                             fg_color="transparent", width=100)
    label_hint.pack(pady=20, anchor="center")

    action_frame = ck.CTkFrame(main_frame, width=200, height=200)
    action_frame.pack(fill="x", pady=20, padx=50)

    button_restart = create_button(action_frame, "Restart the Game")
    button_restart.configure(
        command=lambda: restart_game(frames))

    button_back_main_menu = create_button(action_frame, "Back to Main Menu")
    button_back_main_menu.configure(
        command=lambda: toggle_frames("menu", frames))

    button_restart.pack(pady=10, side="left")
    button_back_main_menu.pack(pady=10, side="right")

    action_frame.pack(anchor="center")


def restart_game(frames):
    """
    Restarts the game by reinitializing variables and starting a new game.

    Parameters:
        frames (dict): A dictionary containing the different frames of the game.
    """
    initialize_variables()
    new_game(frames["play"], frames)


def answer_from_user(player_choice, correct_title, main_frame, frames,
                     image_label):
    """
    Handles the player's answer to a quiz question.
    It updates the round, score, and life based on the player's choice.
    Displays an image indicating whether the answer was correct or incorrect,
    and proceeds to the next round or ends the game.

    Parameters:
        player_choice (str): The answer selected by the player.
        correct_title (str): The correct answer for the current quiz question.
        main_frame (tkinter.Frame): The main frame of the game where UI elements are updated.
        frames (dict): Dictionary of frames used in the game for switching views.
        image_label (tkinter.Label): The label that displays the feedback image ("correct" or "wrong").

    Updates:
        counter_round (int): Increments the round count.
        counter_life (int): Decreases the life count if the answer is wrong.
        counter_score (int): Increases the score by 100 if the answer is correct.
        var_round (StringVar): Updates the displayed round number.
        var_life (StringVar): Updates the displayed number of lives.
        var_score (StringVar): Updates the displayed score.
    """
    global counter_round, counter_life, player_name, counter_score, var_round, var_life, var_score
    counter_round += 1
    var_round.set(f"Round: {counter_round}")
    if player_choice == correct_title:
        counter_score += 100
        var_score.set(f"Score: {counter_score}")
        replacement_image = CTkImage(light_image=Image.open("correct.png"),
                                     size=(400, 400))
        image_label.configure(image=replacement_image)
        main_frame.after(1000, lambda: new_game(main_frame, frames))

    elif counter_life == 1:
        replacement_image = CTkImage(light_image=Image.open("game_over.png"),
                                     size=(400, 400))
        image_label.configure(image=replacement_image)
        main_frame.after(1000,
                         lambda: end_game(counter_score, frames, image_label,
                                          main_frame, player_name))
    else:
        counter_life -= 1
        var_life.set(f"Lives: {counter_life}")
        replacement_image = CTkImage(light_image=Image.open("wrong.png"),
                                     size=(400, 400))
        image_label.configure(image=replacement_image)

        main_frame.after(1000, lambda: new_game(main_frame, frames))

    time.sleep(0.5)


def end_game(counter_score, frames, image_label, main_frame, player_name):
    """
    Ends the current game, updates the score, and displays the highscore board.

    Parameters:
        counter_score (int): The player's final score at the end of the game.
        frames (dict): Dictionary of frames used in the game for switching views.
        image_label (tkinter.Label): The label displaying the current game image (e.g., "game over").
        main_frame (tkinter.Frame): The main frame of the game where UI elements are updated.
        player_name (str): The name of the player.

    Updates:
        Sets the player's final score using `set_score`.
        Displays the "game over" image on `image_label`.
        Clears and regenerates the highscore board frame using `clearFrame` and `high_score_board`.
        Switches to the "highscore" frame to display the leaderboard.
        Initializes game variables to their default values (e.g., round, score, lives).
        Starts a new game with `new_game`.
    """
    set_score(player_name, counter_score)  # set new score

    replacement_image = CTkImage(light_image=Image.open("game_over.png"),
                                 size=(400, 400))
    image_label.configure(image=replacement_image)  # update the image

    time.sleep(1)

    clearFrame(
        frames["highscore"])  # clear the highscore frames with elements

    high_score_board(frames)  # generate the highscore frame element

    main_frame.after(1000, lambda: toggle_frames("highscore",
                                                 frames))  # Display the highscore

    initialize_variables()  # set to init values scores, round and etc

    new_game(main_frame, frames)  # generate new game


def generate_options(title):
    """
    Generates a list of multiple-choice options for the user based on the given title.

    Parameter:
        title (str): The correct answer that will be included in the list of options.

    Returns:
        list: A shuffled list of 4 options, including the correct title and 3 other random titles.
    """
    options = [title, ]
    time.sleep(1)
    for i in range(3):
        return_value = get_the_title_summary()
        options.append(return_value["title"])
    random.shuffle(options)
    return options


def get_data_from_api():
    """
    Retrieves data from an external API and processes it for use in the game.

    The function performs the following steps:
    - Retrieves the title, summary, and image link for a random item via `get_title_and_summary_imagelink`.
    - Fetches the categories for the title.
    - Downloads the associated image.
    - Generates multiple-choice options by calling `generate_options`.
    - Extracts and formats the categories as hints.
    - Returns the title, a shortened version of the summary, the formatted hints, and the options.

    Returns:
        tuple: A tuple containing:
            - title (str): The correct answer (title).
            - summary (str): The shortened summary (up to 150 characters).
            - hints (str): A formatted string of category hints (if available).
            - options (list): A shuffled list of four options, including the correct title and three random ones.
    """
    title, summary, image_link = get_title_and_summary_imagelink()
    summary = remove_title_from_summary(title, summary)

    categories = get_the_title_categories(title)

    download_image(image_link, "image.jpg")

    # creates options
    options = generate_options(title)

    hints = []
    for word in categories.split("Category:")[1:]:
        hints.append(word.split("\'")[0])

    if len(hints) > 0:
        hints = f"\nCategories: {'; '.join(str(index + 1) + ". " + hints[index] for index in range(3))}"

    return title, summary[:150], hints, options


def get_name():
    return input("Enter your name: ")


def game_status_info(round, lives, score, name):
    """
    Creates a string summarizing the current game status.

    Parameters:
        round (int): The current round number in the game.
        lives (int): The number of lives remaining for the player.
        score (int): The player's current score.
        name (str): The name of the player.

    Returns:
        str: A string containing the formatted game status information.
    """
    game_status_info = (f"\nPlayer: {name}\n"
                        f"That's round no. {round}.\n"
                        f"You have {lives} lives left.\n"
                        f"Your actual score is {score}\n")
    return game_status_info


def remove_title_from_summary(title, summary):
    title = remove_special_characters(title)
    title_words = title.split()
    summary_r_title = summary
    for word in title_words:
        summary_r_title = summary_r_title.replace(word, "?")
        summary_r_title = summary_r_title.replace(word.lower(), "?")
        summary_r_title = summary_r_title.replace(word.upper(), "?")
        summary_r_title = summary_r_title.replace(
            word[0].upper() + word[1:].lower(), "?")

    summary_r_title = summary_r_title[:2] + "".join(
        summary_r_title[index] for index in range(2, len(summary_r_title))
        if "?" not in summary_r_title[index - 2:index] or summary_r_title[
            index] != "?")
    return summary_r_title


def remove_special_characters(text):
    return ''.join(char for char in text if char.isalnum() or char.isspace())


def get_title_and_summary_imagelink():
    return_value = get_the_title_summary()
    title = return_value["title"]
    summary = return_value["extract"]
    image_link = return_value["thumbnail"]["source"]
    return title, summary, image_link
