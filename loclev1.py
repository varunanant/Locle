#!/usr/bin/env python3
from geopy.geocoders import Nominatim
import random
import tkinter as tk
from PIL import ImageTk, Image
import os
import sys

window = tk.Tk()
window['bg'] = "#006994"
window.title("Locle!")
def runGame():
    welcome_msg = tk.Label(text="Welcome To Locle! The goal is to guess a city within 100 miles of a latitude line! To take a guess, enter the name of a city in the white box!\n\n\n", bg="#006994", font=("Helvetica", 15))
    goal_line = random.randint(-55,60)
    # Dist_form = 0.01449
    if goal_line < 0:
        goal_txt = str(0-goal_line)+" S"
    else:
        goal_txt = str(goal_line)+" N"
    guess_msg = tk.Label(text="Latitude: "+str(goal_txt), bg="#006994")
    guess_box = tk.Entry(width=30)
    geolocator = Nominatim(user_agent="Locle")
    output_console = tk.Text(bg="#8BAE72")
    output_console.config(state=tk.DISABLED)
    global guess_cnt
    guess_cnt = 0
    def submitAnswer():
        pos = "-1.0"
        global guess
        guess = geolocator.geocode(guess_box.get())
        output_console.config(state=tk.NORMAL)
        guess_latitude = guess.latitude
        if guess.latitude < 0:
            guess_latitude = str(0-guess.latitude)+" S"
        else:
            guess_latitude = str(guess.latitude)+" N"

        global dist_away
        dist_away = round(abs((goal_line - guess.latitude)/0.0149), 1)
        global guess_cnt
        guess_cnt += 1

    def playAgain():
        os.execv(sys.executable, [sys.executable, __file__] + sys.argv)

    def exitGame():
        window.destroy()
    
    play_again_button = tk.Button(text="Play Again!", command=lambda : playAgain())
    exit_button = tk.Button(text="Exit", command=lambda : exitGame())

    def displayText():
        output_console.insert('-1.0', str(guess)+' is '+str(dist_away)+' miles away.\n')
        if dist_away <= 100:
            output_console.insert('-1.0', 'Congratulations! You guessed a correct city in '+str(guess_cnt)+" tries!")
            play_again_button.pack()
            submit_button["state"] = tk.DISABLED
            output_console.insert('-1.0', '---------------------------------------------------------------------------\n')
        elif guess_cnt < 6:
            output_console.insert('-1.0', 'Your guess was too far away. Try again.\n')
            output_console.insert('-1.0', '---------------------------------------------------------------------------\n')
        else:
            output_console.insert('-1.0', '---------------------------------------------------------------------------\n')
            output_console.insert('-1.0', 'You were unable to solve the Locle. Click the "play again" button to play again or the "exit" button to exit\n')
            play_again_button.pack()

    def doBoth():
        submitAnswer()
        displayText()


    
    submit_button = tk.Button(command=lambda : doBoth(), text="Enter my Guess!")
    submit_button["state"] = tk.NORMAL

    welcome_msg.pack()
    guess_msg.pack()
    guess_box.pack()
    submit_button.pack()
    output_console.pack()
    exit_button.pack()

runGame()
window.mainloop()