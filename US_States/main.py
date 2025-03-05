from turtle import Screen
# from state_manager import StateManager
from state import State
import turtle
import pandas as pd

# Set up the screen
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.setup(width=725, height=491)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", 
        prompt="What's another state's name?").title()
            
    if answer_state == "Exit":
        states_to_learn = [state for state in all_states]
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv", index=False)
        break
    
    if answer_state in all_states:
        state = State(data[data.state == answer_state].state.item(), data[data.state == answer_state].x.item(), data[data.state == answer_state].y.item())
        guessed_states.append(answer_state)
        all_states.remove(answer_state)

screen.exitonclick()