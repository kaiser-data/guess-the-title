from tkinter import LEFT

from game_play_util.game_play_util import *
from frame_util.frame_util import *
from PIL import Image
import customtkinter as ck

"""
This script initializes the main game window for the "Guess the Title" game using the `customtkinter` library.

The script creates a GUI with multiple frames for different parts of the game:
- Menu: Displays the main menu where the player can choose options.
- Enter Name: A frame for entering the player's name.
- Play: The gameplay screen where the player interacts with the game.
- Highscore: Displays the high scores.
- How To Play: Provides instructions for playing the game.
- Credits: Displays game credits.
"""
root = ck.CTk()

frames = {
    "menu": ck.CTkFrame(root, fg_color="transparent"),
    "enter_name": ck.CTkLabel(root, fg_color="transparent"),
    "play": ck.CTkFrame(root, fg_color="transparent"),
    "highscore": ck.CTkFrame(root, fg_color="transparent"),
    "htp": ck.CTkFrame(root, fg_color="transparent"),
    "credits": ck.CTkFrame(root, fg_color="transparent")
}

root.geometry("1000x1100+400+50")
root.title("Guess the title")

image = Image.open("guess.png")
create_menu_frame(image, frames)

""" PLAY """
initialize_variables()
new_game(frames["play"], frames)

""" HIGHSCORE """
high_score_board(frames)

"""HOW TO PLAY"""
how_to_play(frames)

"""Menu"""
toggle_frames("menu", frames)

"""Credits"""
credits_func(frames)

root.mainloop()
