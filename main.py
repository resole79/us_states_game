from turtle import Turtle
from turtle import Screen
from PIL import Image
import pandas

# Declare variable and CONSTANT
# If you want different country uncomment this and comment us image and file
# IMAGE = "./image/Italia_per_region.gif"
# FILE = "./csv/italy_region.csv"

IMAGE = "./image/blank_states_img.gif"
FILE = "./csv/50_states.csv"

FONT = ("Courier", 12, "bold")
ALIGN = "center"
correct_answer = []

# Use Pil package
open_image = Image.open(IMAGE)
width, height = open_image.size
screen = Screen()
screen.bgpic(IMAGE)
screen.setup(width, height)
screen.title("Guess the state")

# read cvs file
us_states = pandas.read_csv(FILE)
# convert colon "state" in list
us_states_list = us_states.state.to_list()
# Length of "us_states_list" and "correct_answer"
us_states_len = len(us_states_list)
correct_answer_len = len(correct_answer)

us_state_missing = []
# cycle while condition to exit "correct_answer_len" equal to or grater then "us_states_len"
while correct_answer_len < us_states_len:
    choice_user = screen.textinput(f"{len(correct_answer)}/{us_states_len} - Guess",
                                   "What's another name?").title()
    # state user choice in cvs file
    us_state_user_choice = us_states[us_states.state == choice_user]

    # write exit to finish program and write missing state file
    if choice_user == "Exit":
        for state in us_states_list:
            if state not in correct_answer:
                us_state_missing.append(state)
        list_to_write = pandas.DataFrame(us_state_missing)
        list_to_write.to_csv("you_missing.csv")
        break
    # if to check the state in inside csv file
    if not us_state_user_choice.empty:
        correct_answer.append(choice_user)
        state = us_state_user_choice.state.item()
        x_pos = int(us_state_user_choice.x)
        y_pos = int(us_state_user_choice.y)
        usa_map = Turtle()
        usa_map.hideturtle()
        usa_map.penup()
        usa_map.goto(x_pos, y_pos)
        usa_map.write(state, align=ALIGN, font=FONT)
