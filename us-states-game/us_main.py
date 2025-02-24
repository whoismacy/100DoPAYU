import pandas
import turtle
from turtle import Screen

screen = Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

# Creating the turtle
amy = turtle.Turtle()
amy.penup()
amy.color("black")
amy.hideturtle()

# Reading From CSV
states_data = pandas.read_csv("50_states.csv")
states = states_data.state.tolist()
x_coords = states_data.x.tolist()
y_coords = states_data.y.tolist()
full_coords = tuple(zip(x_coords, y_coords))
states_coords = dict()

for i in range(len(states)):
    states_coords[states[i]] = full_coords[i]

#Count & Game is on.
correct_count = 0
game_is_on = True

# guessed states
guessed_states = []

# Getting Input from the User
while game_is_on:
    answer_state = turtle.textinput(title=f"{correct_count}/50", prompt="What's another State's name ?")
    answer_state = answer_state.title()

    if correct_count == 50:
        game_is_on = False

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        if answer_state not in guessed_states:
            correct_count += 1
            amy.goto(states_coords[answer_state])
            amy.write(arg=answer_state, font=("Courier", 8, "normal"), align="center")
            guessed_states.append(answer_state)


# Ensure game is continuously running
# turtle.mainloop()

