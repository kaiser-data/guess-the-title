from tkinter import LEFT, CENTER
from tkinter import StringVar

import customtkinter as ck
from PIL import Image
from customtkinter import CTkImage
import random

global counter_round
global counter_life
global player_name
global var_round
global var_life

from api_util import get_the_title_summary, download_image, \
    get_the_title_categories


def answer_from_user(player_choice, correct_title, main_frame):
    global counter_round, counter_life, var_round, var_life
    if player_choice == correct_title:
        counter_round += 1
        var_round.set(f"Round: {counter_round}")
        var_life.set(f"Life: {counter_life}")
        new_game(main_frame)
    else:
        counter_life -= 1
        var_life.set(f"Life: {counter_life}")
        new_game(main_frame)


def generate_header(main_frame):
    global counter_round, counter_life, player_name

    label_frame = ck.CTkFrame(main_frame, width=400, height=10)

    player_label = ck.CTkLabel(label_frame,
                               text=f"Player name: {player_name}",
                               fg_color="transparent")
    player_label.pack(padx=100, side=LEFT)
    round_label = ck.CTkLabel(label_frame,
                              textvariable=var_round,
                              fg_color="transparent", anchor="center")
    round_label.pack(padx=100, side=LEFT)
    score_label = ck.CTkLabel(label_frame,
                              textvariable=var_life,
                              fg_color="transparent")
    score_label.pack(padx=100, side=LEFT)

    label_frame.pack(anchor="center")

    image_logo = Image.open("guess.png")
    tk_image = CTkImage(light_image=image_logo, dark_image=image_logo,
                        size=(100, 100))
    image_label = ck.CTkLabel(main_frame, text="", image=tk_image)
    image_label.pack(pady=10, anchor="center")


def generate_new_set_of_data(main_frame, summary, title,
                             incorrect_title,
                             hints):
    image = Image.open("image.jpg")
    tk_image = CTkImage(light_image=image, dark_image=image, size=(300, 300))

    image_label = ck.CTkLabel(main_frame, text="", image=tk_image)
    image_label.pack(pady=10, anchor="center")

    label_summary = ck.CTkLabel(main_frame, text=f"{summary}",
                                fg_color="transparent", width=300)
    label_summary._label.config(wrap=800)
    label_summary.pack(pady=10, anchor="center")

    incorrect_title.append(title)

    l_shuffled = random.sample(incorrect_title, len(incorrect_title))

    button_frame = ck.CTkFrame(main_frame, width=450, height=350)

    button1 = create_button(button_frame, l_shuffled[0])
    button1.configure(
        command=lambda: answer_from_user(l_shuffled[0], title, main_frame))

    button2 = create_button(button_frame, l_shuffled[1])
    button2.configure(
        command=lambda: answer_from_user(l_shuffled[1], title, main_frame))

    button3 = create_button(button_frame, l_shuffled[2])
    button3.configure(
        command=lambda: answer_from_user(l_shuffled[2], title, main_frame))

    button4 = create_button(button_frame, l_shuffled[3])
    button4.configure(
        command=lambda: answer_from_user(l_shuffled[3], title, main_frame))

    button1.grid(row=0, column=0, padx=20, pady=20)
    button2.grid(row=0, column=1, padx=20, pady=20)
    button3.grid(row=1, column=0, padx=20, pady=20)
    button4.grid(row=1, column=1, padx=20, pady=20)

    button_frame.pack(anchor="center")

    label_hint = ck.CTkLabel(main_frame, text=f"Hint? {hints}",
                             fg_color="transparent", width=100)
    label_hint.pack(pady=20, anchor="center")

    action_frame = ck.CTkFrame(main_frame, width=200, height=200)

    button_restart = create_button(action_frame, "Restart")
    button_restart.configure(command=lambda: game_action("restart"))

    button_back_main_menu = create_button(action_frame, "Back to Main Menu")
    button_back_main_menu.configure(
        command=lambda: game_action("back_to_main_menu"))

    button_restart.grid(row=0, column=0)
    button_back_main_menu.grid(row=0, column=1)

    action_frame.pack(anchor="center")


def game_action(action):
    print(action)


def create_button(button_frame, l_shuffled):
    return ck.CTkButton(button_frame, text=l_shuffled)


def get_data_from_api():
    return_value = get_the_title_summary()

    return_value_first_incorrect = get_the_title_summary()["title"]

    return_value_second_incorrect = get_the_title_summary()["title"]

    return_value_third_incorrect = get_the_title_summary()["title"]

    image_link = return_value["thumbnail"]["source"]

    summary = return_value["extract"]

    title = return_value["title"]

    categories = get_the_title_categories(title)

    download_image(image_link, "image.jpg")

    incorrect_title = [return_value_first_incorrect,
                       return_value_second_incorrect,
                       return_value_third_incorrect]
    hints = []

    for word in categories.split("Category:")[1:]:
        hints.append(word.split("\'")[0])

    return title, summary, hints[:3], incorrect_title


def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()


def start_game(main_frame, player):
    global counter_round, counter_life, player_name, var_life, var_round

    player_name = player
    counter_life = 3
    counter_round = 0
    var_life = StringVar()
    var_life.set(f"Life: 3")
    var_round = StringVar()
    var_round.set(f"Round: 0")

    var_round.set(f"Round: {counter_round}")
    var_life.set(f"Life: {counter_life}")

    new_game(main_frame)




def new_game(main_frame):
    clearFrame(main_frame)
    generate_header(main_frame)
    title, summary, hints, incorrect_title = get_data_from_api()
    generate_new_set_of_data(main_frame, summary, title,
                             incorrect_title,
                             hints)


def main():
    root = ck.CTk()
    root.geometry("850x850")
    root.title("Guess the Title")

    global counter_round, counter_life, player_name, var_life, var_round

    player_name = "Jerome"
    counter_life = 3
    counter_round = 0
    var_life = StringVar()
    var_life.set(f"Life: 3")
    var_round = StringVar()
    var_round.set(f"Round: 0")

    var_round.set(f"Round: {counter_round}")
    var_life.set(f"Life: {counter_life}")

    main_frame = ck.CTkFrame(root, fg_color="transparent")

    new_game(main_frame)

    main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()


if __name__ == '__main__':
    main()
