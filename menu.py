import random
from tkinter import StringVar, LEFT

import customtkinter as ck
from PIL import Image
from customtkinter import CTkImage

import api_util

global counter_round
global counter_life
global player_name
global var_round
global var_life

toggle_state = 0

""" GAME UTILILITIES """


def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()


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


def game_action(main_frame, action):
    global player_name
    if "restart" in action:
        start_game(main_frame, player_name)
    else:
        toggle(0)


def create_button(button_frame, l_shuffled):
    return ck.CTkButton(button_frame, text=l_shuffled)


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
    button_restart.configure(
        command=lambda: game_action(main_frame, "restart"))

    button_back_main_menu = create_button(action_frame, "Back to Main Menu")
    button_back_main_menu.configure(
        command=lambda: game_action(main_frame, "back_to_main_menu"))

    button_restart.grid(row=0, column=0)
    button_back_main_menu.grid(row=0, column=1)

    action_frame.pack(anchor="center")


def get_data_from_api():
    return_value = api_util.get_the_title_summary()

    return_value_first_incorrect = api_util.get_the_title_summary()

    return_value_second_incorrect = api_util.get_the_title_summary()

    return_value_third_incorrect = api_util.get_the_title_summary()

    image_link = return_value["thumbnail"]["source"]

    summary = return_value["extract"]

    title = return_value["title"]

    categories = api_util.get_the_title_categories(title)

    api_util.download_image(image_link, "image.jpg")

    incorrect_title = [return_value_first_incorrect["title"],
                       return_value_second_incorrect["title"],
                       return_value_third_incorrect["title"]]
    hints = []

    for word in categories.split("Category:")[1:]:
        hints.append(word.split("\'")[0])

    return title, summary, hints[:3], incorrect_title


def new_game(main_frame):
    clearFrame(main_frame)
    generate_header(main_frame)
    title, summary, hints, incorrect_title = get_data_from_api()
    generate_new_set_of_data(main_frame, summary, title,
                             incorrect_title,
                             hints)


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


def toggle(toggle_num):
    """ Call this function to switch between the different pages and load the right frames.
        Menu state = 0
        Play state = 1
        Highscore state = 2
        Tutorial state = 3
        Credits state = 4"""
    toggle_state = toggle_num
    if toggle_state == 0:
        main_frame_menu.place(relx=0.5, rely=0.5, anchor="center")
        main_frame_play.place_forget()
        highscore_title_label.place_forget()
        return

    elif toggle_state == 1:  # PLAY FUNCTION
        main_frame_menu.place_forget()
        main_frame_play.place(relx=0.5, rely=0.5, anchor="center")
        return

    elif toggle_state == 2:  # HIGHSCORE
        main_frame_menu.place_forget()
        main_frame_highscore.place(relx=0.5, rely=0.5, anchor="center")
        return

    elif toggle_state == 3:  # TUTORIAL
        main_frame_menu.place_forget()
        pass

    elif toggle_state == 4:  # CREDITS
        main_frame_menu.place_forget()
        pass


root = ck.CTk()
root.geometry("800x700")
root.title("Guess the title")

main_frame_menu = ck.CTkFrame(root, fg_color="transparent")

image = Image.open("guess.png")
tk_image = CTkImage(light_image=image, dark_image=image, size=(400, 300))

image_label = ck.CTkLabel(main_frame_menu, text="", image=tk_image)
image_label.grid(pady=20, row=0)

button_frame_menu = ck.CTkFrame(main_frame_menu, fg_color="transparent")

play_button = ck.CTkButton(button_frame_menu, text="PLAY", font=("Arial", 30),
                           command=lambda: toggle(1))
highscore_button = ck.CTkButton(button_frame_menu, text="HIGHSCORE",
                                font=("Arial", 30), command=lambda: toggle(2))
htp_button = ck.CTkButton(button_frame_menu, text="HOW TO PLAY",
                          font=("Arial", 30), command=lambda: toggle(3))
credits_button = ck.CTkButton(button_frame_menu, text="CREDITS",
                              font=("Arial", 30), command=lambda: toggle(4))
exit_button = ck.CTkButton(button_frame_menu, text="EXIT", font=("Arial", 30),
                           command=lambda: exit())

play_button.grid(row=0, pady=15)
highscore_button.grid(row=1, pady=15)
htp_button.grid(row=2, pady=15)
credits_button.grid(row=3, pady=15)
exit_button.grid(row=4, pady=15)

button_frame_menu.grid(row=1)

""" PLAY """
main_frame_play = ck.CTkFrame(root, fg_color="transparent")

start_game(main_frame_play, "Jerome")

""" HIGHSCORE """
main_frame_highscore = ck.CTkFrame(root, fg_color="transparent")

highscore_title_label = ck.CTkLabel(main_frame_highscore, text="Highscores",
                                    font=("Arial", 40))
highscore_title_label.pack(pady=20, anchor="center")
top_five_label = ck.CTkLabel(main_frame_highscore, text="")
toggle(0)

root.mainloop()
