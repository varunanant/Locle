from geopy.geocoders import Nominatim
import random
from tkinter import *
from tkinter import ttk as tk
from PIL import ImageTk, Image
import os
import sys

window = Tk()
window["bg"] = "#4DB4D7"
style = tk.Style()
style.configure("TButton", background="#44BD90")
window.title("Locle!")
def runGame():
    welcome_msg = tk.Label(text="Welcome To Locle! The goal is to guess a city within 100 miles of a latitude line! To take a guess, enter the name of a city in the white box!\n\n\n", font=("Helvetica", 15), background="#4DB4D7")
    goal_line = random.randint(-55,60)
    # Dist_form = 0.01449
    if goal_line < 0:
        goal_txt = str(0-goal_line)+" S"
    else:
        goal_txt = str(goal_line)+" N"
    guess_msg = tk.Label(text="Latitude: "+str(goal_txt), background="#4DB4D7")
    guess_box = tk.Entry(width=30)
    geolocator = Nominatim(user_agent="Locle")
    output_console = Text(background="#44BD90")
    output_console.config(state=DISABLED)
    instructions = tk.Label(text="Latitude lines are the lines that go horizontally across the entrire planet.The are measured in degrees North or South, north being above the equator, and south being below. Latitude 0 North or South is the equator. \nKeep in mind that one latitude degree is about 70 miles. Good Luck! :)", background="#4DB4D7")
    global guess_cnt
    guess_cnt = 0
    def submitAnswer():
        pos = "-1.0"
        global guess
        guess = geolocator.geocode(guess_box.get())
        output_console.config(state=NORMAL)
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
    
    play_again_button = tk.Button(text="Play Again!", command=playAgain)
    exit_button = tk.Button(text="Exit", command=exitGame)

    def displayText():
        output_console.insert('-1.0', str(guess)+' is '+str(dist_away)+' miles away.\n')
        if dist_away <= 100:
            output_console.insert('-1.0', 'Congratulations! You guessed a correct city in '+str(guess_cnt)+" tries! ")
            output_console.config(state=DISABLED)
            guess_box["state"] = DISABLED
            play_again_button.pack()
            submit_button["state"] = DISABLED
            output_console.insert('-1.0', '---------------------------------------------------------------------------\n')
        elif guess_cnt < 6:
            output_console.insert('-1.0', 'Your guess was too far away. Try again.\n')
            output_console.insert('-1.0', '---------------------------------------------------------------------------\n')
            output_console.config(state=DISABLED)
        else:
            output_console.insert('-1.0', '---------------------------------------------------------------------------\n')
            output_console.insert('-1.0', 'You were unable to solve the Locle. Click the "play again" button to play again or the "exit" button to exit\n')
            submit_button["state"] = DISABLED
            guess_box["state"] = DISABLED
            output_console.config(state=DISABLED)
            play_again_button.pack()

    def doBoth():
        submitAnswer()
        displayText()
    
    submit_button = tk.Button(command=doBoth, text="Enter my Guess!")
    submit_button["state"] = NORMAL

    welcome_msg.pack()
    guess_msg.pack()
    guess_box.pack()
    submit_button.pack()
    output_console.pack()
    exit_button.pack()
    instructions.pack()

runGame()
window.mainloop()