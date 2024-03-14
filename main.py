import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
data = pandas.read_csv("50_states.csv")

points = 0
correct_answers = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{points}/50 Guess the State", prompt="Whats another states name?").title()

    if answer_state in data["state"].to_list():
        states_row = data[data.state == answer_state]
        x_position = int(states_row.x)
        y_position = int(states_row.y)
        turtle.goto(x_position, y_position)
        turtle.write(f"{answer_state}", align="center", font=("Courier", 6, "normal"))
        points += 1
        correct_answers.append(answer_state)
    if len(correct_answers) == 50:
        game_is_on = False
    if answer_state == "Exit":
        break

list_of_states = data["state"].to_list()
missed_states = [state for state in list_of_states if state not in correct_answers]


state_dict = {
    "state": missed_states
}

data_obj = pandas.DataFrame(state_dict)

data_obj.to_csv("MissedStates")
