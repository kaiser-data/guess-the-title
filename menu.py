import customtkinter as ck
from PIL import Image
from customtkinter import CTkImage
from game_util import start_game

toggle_state = 0


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
