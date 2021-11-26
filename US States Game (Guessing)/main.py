import turtle
import pandas


FONT = ('Arial', 30, 'normal')

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
print(all_states)
answers = []
guessing = True

while guessing:
    answer_state = screen.textinput(title=f'{len(answers)}/50 States guessed', prompt="What the next State's name?").title()
    if answer_state == "Exit":
        # states_to = []
        # for state in all_states:
        #     if state not in answers:
        #         states_to.append(state)
        # print(states_to)
        states_to = [state for state in all_states if not state in answers]
        break
    if answer_state in df.values:
        answers.append(answer_state)
        coor_x = df[df["state"] == answer_state]["x"].values[0]
        coor_y = df[df["state"] == answer_state]["y"].values[0]
        states_to = all_states.remove(answer_state)
        # print(states_to)

        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_text.goto(int(coor_x), int(coor_y))
        state_text.write(f"{answer_state}")

        score = turtle.Turtle()
        score.hideturtle()
        score.penup()
        score.goto(0, 190)
        score.write(f"{len(set(answers))}", FONT)
        
    else:
        pass

df2 = pandas.DataFrame(states_to)
df2.to_csv('states_to.csv', index=False)