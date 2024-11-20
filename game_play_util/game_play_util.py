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

global player_name
global var_round
global var_life
global var_score
global counter_round, counter_life, counter_score


def initialize_variables():
    global counter_round, counter_life, counter_score, player_name, var_life, var_round, var_score

    if not player_name:
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
    options = [title, ]
    time.sleep(1)
    for i in range(3):
        return_value = get_the_title_summary()
        options.append(return_value["title"])
    random.shuffle(options)
    return options


def get_data_from_api():
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
    return title, summary, hints, options


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


def new_game(main_frame, frames):
    clearFrame(main_frame)
    generate_header(main_frame, player_name, var_round, var_life, var_score)
    title, summary, hints, options = get_data_from_api()
    generate_new_set_of_data(main_frame, frames, summary, title,
                             options,
                             hints)


def create_button(button_frame, l_shuffled):
    return ck.CTkButton(button_frame, text=l_shuffled)


def generate_new_set_of_data(main_frame, frames, summary, title,
                             options,
                             hints):
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
    initialize_variables()
    new_game(frames["play"], frames)


def answer_from_user(player_choice, correct_title, main_frame, frames,
                     image_label):
    global counter_round, counter_life, counter_score, var_round, var_life, var_score
    counter_round += 1
    var_round.set(f"Round: {counter_round}")
    if player_choice == correct_title:
        counter_score += 100
        var_score.set(f"Score: {counter_score}")
        replacement_image = CTkImage(light_image=Image.open("correct.png"),
                                     size=(400, 400))
        image_label.configure(image=replacement_image)
        main_frame.after(1000, lambda: new_game(main_frame, frames))

    elif counter_life == 0:
        set_score(player_name, counter_score)
        replacement_image = CTkImage(light_image=Image.open("game_over.png"),
                                     size=(400, 400))
        image_label.configure(image=replacement_image)
        clearFrame(frames["highscore"])
        high_score_board(frames)
        main_frame.after(1000, lambda: toggle_frames("highscore", frames))
    else:
        counter_life -= 1
        var_life.set(f"Lives: {counter_life}")
        replacement_image = CTkImage(light_image=Image.open("wrong.png"),
                                     size=(400, 400))
        image_label.configure(image=replacement_image)

        main_frame.after(1000, lambda: new_game(main_frame, frames))

    time.sleep(0.5)


def generate_options(title):
    options = [title, ]
    time.sleep(1)
    for i in range(3):
        return_value = get_the_title_summary()
        options.append(return_value["title"])
    random.shuffle(options)
    return options


def get_data_from_api():
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
    return title, summary, hints, options


def get_name():
    return input("Enter your name: ")


def game_status_info(round, lives, score, name):
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


if __name__ == "__main__":
    pass
