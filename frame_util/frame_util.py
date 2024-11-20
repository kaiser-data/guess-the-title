import customtkinter as ck
from customtkinter import CTkImage
from PIL import Image

from data_util.data_util import get_scores

player_name = 'Jerome'
toggle_state = 0

var_round = None
var_life = None
var_score = None


def toggle_frames(frame_name, frames):
    """ Call this function to switch between the different pages and load the right frames."""
    if frame_name in frames:
        for frame in frames:
            frames[frame].place_forget()
        frames[frame_name].place(relx=0.5, rely=0.5, anchor="center")


def create_menu_frame(image, frames):
    tk_image = CTkImage(light_image=image, dark_image=image, size=(400, 300))

    image_label = ck.CTkLabel(frames["menu"], text="", image=tk_image)
    image_label.grid(pady=20, row=0)

    button_frame_menu = ck.CTkFrame(frames["menu"], fg_color="transparent")

    play_button = ck.CTkButton(button_frame_menu, text="PLAY",
                               font=("Arial", 50, "bold"),
                               command=lambda: toggle_frames("play", frames))
    highscore_button = ck.CTkButton(button_frame_menu, text="HIGHSCORE",
                                    font=("Arial", 30),
                                    command=lambda: toggle_frames("highscore",
                                                                  frames))
    htp_button = ck.CTkButton(button_frame_menu, text="HOW TO PLAY",
                              font=("Arial", 30),
                              command=lambda: toggle_frames("htp", frames))
    credits_button = ck.CTkButton(button_frame_menu, text="CREDITS",
                                  font=("Arial", 30),
                                  command=lambda: toggle_frames(
                                      credits_button, frames))
    exit_button = ck.CTkButton(button_frame_menu, text="EXIT",
                               font=("Arial", 30),
                               command=lambda: exit())

    play_button.grid(row=0, pady=15)
    highscore_button.grid(row=1, pady=15)
    htp_button.grid(row=2, pady=15)
    credits_button.grid(row=3, pady=15)
    exit_button.grid(row=4, pady=15)

    button_frame_menu.grid(row=1)


def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()


def generate_header(main_frame, player_name, var_round, var_life, var_score):
    label_frame = ck.CTkFrame(main_frame, width=400, height=10,
                              fg_color="#2E8B57", )
    label_frame.pack(fill="x", side="top", pady=5)

    player_label = ck.CTkLabel(label_frame, font=("Arial", 16),
                               text=f"Player: {player_name}",
                               fg_color="transparent")
    player_label.pack(padx=50, side="left")
    round_label = ck.CTkLabel(label_frame, font=("Arial", 16),
                              textvariable=var_round,
                              fg_color="transparent", anchor="center")
    round_label.pack(padx=50, side="left")

    life_label = ck.CTkLabel(label_frame, font=("Arial", 16),
                             textvariable=var_life,
                             fg_color="transparent")
    life_label.pack(padx=50, side="left")

    score_label = ck.CTkLabel(label_frame, font=("Arial", 16),
                              textvariable=var_score,
                              fg_color="transparent")
    score_label.pack(padx=50, side="left")

    label_frame.pack(anchor="center")

    image_logo = Image.open("guess.png")
    tk_image = CTkImage(light_image=image_logo, dark_image=image_logo,
                        size=(40, 40))
    image_label = ck.CTkLabel(label_frame, text="", image=tk_image)
    image_label.pack(side="right", padx=0, pady=0)


def high_score_board(frames):
    top_five = get_scores()
    htp_frame = ck.CTkFrame(frames["highscore"], width=750, height=550)
    htp_title_label = ck.CTkLabel(htp_frame, text="Scoreboard",
                                  font=("Arial", 30, "bold"))
    htp_title_label.pack(pady=10, anchor="center")

    htp_title_label = ck.CTkLabel(htp_frame, text="Name : Score",
                                  font=("Arial", 10, "bold"))
    htp_title_label.pack(pady=10, anchor="center")

    for count, val in enumerate(top_five, start=1):
        htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                               text=f"{count}. {val[0]} : {val[1]}",
                                               font=("Arial", 20))
        htp_start_the_game_label.pack(pady=10)

    action_frame = ck.CTkFrame(htp_frame, width=100, height=100)
    action_frame.pack(fill="x", pady=20, padx=50)
    button_back_main_menu = create_button(action_frame, "Back to Main Menu")
    button_back_main_menu.configure(
        command=lambda: toggle_frames("menu", frames))
    button_back_main_menu.pack(pady=10, side="bottom")
    action_frame.pack(anchor="center")

    htp_frame.pack()


def how_to_play(frames):
    htp_frame = ck.CTkFrame(frames["htp"], width=750, height=550)
    htp_title_label = ck.CTkLabel(htp_frame, text="How to Play",
                                  font=("Arial", 30, "bold"))
    htp_title_label.pack(pady=10, anchor="center")
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="1. Start the Game",
                                           font=("Arial", 20))
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="Select Play from the menu and enter your name to begin.",
                                           font=("Arial", 20))
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="2. Objective",
                                           font=("Arial", 20))
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="Answer questions correctly to earn points."
                                                " You start with 3 lives and a score of 0.",
                                           font=("Arial", 20), wraplength=500)
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="3. Gameplay",
                                           font=("Arial", 20))
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="A random image and a short summary will appear."
                                                " Choose the correct answer from the 4 options provided."
                                                " Correct Answer: Gain 100 points."
                                                " Incorrect Answer: Lose 1 life.",
                                           font=("Arial", 20), wraplength=500)
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="4. Game Over",
                                           font=("Arial", 20))
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="The game ends when you lose all lives."
                                                " Your score is compared with the top 5 on the leaderboard.",
                                           font=("Arial", 20), wraplength=500)
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="5. Scoreboard",
                                           font=("Arial", 20))
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="If your score is high enough, it will be added to the top 5."
                                                " View your ranking and try again to beat your best score!",
                                           font=("Arial", 20), wraplength=550)
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="6. Return to Menu",
                                           font=("Arial", 20))
    htp_start_the_game_label.pack(pady=10)
    htp_start_the_game_label = ck.CTkLabel(htp_frame,
                                           text="After the game ends, you’ll return to the menu to play again,"
                                                " view the leaderboard, or exit.",
                                           font=("Arial", 20), wraplength=550)
    htp_start_the_game_label.pack(pady=10)
    action_frame = ck.CTkFrame(htp_frame, width=100, height=100)
    action_frame.pack(fill="x", pady=20, padx=50)
    button_back_main_menu = create_button(action_frame, "Back to Main Menu")
    button_back_main_menu.configure(
        command=lambda: toggle_frames("menu", frames))
    button_back_main_menu.pack(pady=10, side="bottom")
    action_frame.pack(anchor="center")

    htp_frame.pack()


def create_button(button_frame, l_shuffled):
    return ck.CTkButton(button_frame, text=l_shuffled)
