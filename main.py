from tkinter import LEFT

from game_play_util.game_play_util import *
from frame_util.frame_util import *
from PIL import Image
import customtkinter as ck

player_name = 'Jerome'

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

"""Enter name"""

""" PLAY """
initialize_variables("Jerome")
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

