from tkinter import *
import random

window = Tk()
window.geometry("1000x800")
window.title("Rock, Paper, Scissors")
window.config(background="white")

cs = 0
ps = 0
options = ["Rock","Paper","Scissors"]


def computer_wins():
    global cs 
    cs += 1
    Computer_score.config(text="Score: {}".format(cs),font=("times",16,"bold"))
    winner_title.config(text="Computer won",fg="red",font=("times",18),bg="white")
    player_score.config(text="Score: {}".format(ps),font=("times",16,"bold"))

def player_wins():
    global ps
    ps += 1
    Computer_score.config(text="Score: {}".format(cs),font=("times",16,"bold"))
    winner_title.config(text="You won",fg="green",font=("times",18),bg="white")
    player_score.config(text="Score: {}".format(ps),font=("times",16,"bold"))

def tie():
    global cs,ps
    Computer_score.config(text="Score: {}".format(cs),font=("times",16,"bold"))
    player_score.config(text="Score: {}".format(ps),font=("times",16,"bold"))
    winner_title.config(text="It's a tie",fg="yellow",font=("times",18),bg="white")

def player_choice(player_input):
    print(player_input)
    global options
    computer_input = random.choice(options)
    computer_selection.config(text="Selection: {}".format(computer_input))
    player_selection.config(text="Selection: {}".format(player_input))

    if player_input == computer_input:
        tie()
    elif player_input == "Rock" and computer_input == "Paper":
        computer_wins()



title = Label(text="Rock, Paper, Scissors",fg="grey",font=("times",25))
title.pack(pady=50)

winner_title = Label(text="Let's start the game!",fg="green",font=("times",18),bg="white")
winner_title.pack(pady=5)

options1 = Label(text="Your options: ",fg="black",font=("times",18))
options1.place(x=50,y=250)

rock = Button(text="Rock",height=2,width=10,font=("times",16),command=lambda: player_choice("Rock"))
rock.place(x=200,y=325)

paper = Button(text="Paper",height=2,width=10,font=("times",16),command=lambda: player_choice("Paper"))
paper.place(x=425,y=325)

scissors = Button(text="Scissors",height=2,width=10,font=("times",16),command=lambda: player_choice("Scissors"))
scissors.place(x=650,y=325)

score_details = Label(text="Score: ",fg="black",font=("times",18),background="white")
score_details.place(x=50,y=425)

Computer = Label(text="Computer",font=("times",20,"bold"),background="white")
Computer.place(x=150,y=500)

player = Label(text="Player",font=("times",20,"bold"),background="white")
player.place(x=550,y=500)

computer_selection = Label(text="Selection: ",font=("times",16,"bold"),background="white")
computer_selection.place(x=150,y=550)

player_selection = Label(text="Selection: ",font=("times",16,"bold"),background="white")
player_selection.place(x=550,y=550)

Computer_score = Label(text="Score: ",font=("times",16,"bold"),background="white")
Computer_score.place(x=150,y=600)

player_score = Label(text="Score: ",font=("times",16,"bold"),background="white")
player_score.place(x=550,y=600)









window.mainloop()






