from turtle import Turtle, Screen
import pandas
#
screen = Screen()
turtle=Turtle()
screen.setup(725,491)
screen.title("US States Guessing Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


guessed_states=[]

while len(guessed_states)<50:
    state_name=screen.textinput(f"{len(guessed_states)}/50 states","Enter the State ")
    if state_name=="exit":
        missing_states=[state for state in states if state not in guessed_states]

        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("Lean these States.csv")
        break

    if state_name in states:
        guessed_states.append(state_name)
        t = Turtle()
        t.hideturtle()
        t.penup()
        get_state=data[data.state==state_name]
        t.goto(x= int(get_state.x),y= int(get_state.y))
        t.write(state_name)


screen.exitonclick()