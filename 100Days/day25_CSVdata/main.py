import pandas
import turtle
import csv

data = pandas.read_csv("100Days\day25_CSVdata/50_states.csv")

screen  = turtle.Screen()
screen.title("U.S States")
image = "100Days\day25_CSVdata/blank_states_img.gif"    # load in the map as an image (gif only)
screen.addshape(image)              # load that shape in as the screen
turtle.shape(image)

correct_count = 50
correct_guesses = []
states_to_learn = []

game_on = True

while game_on:
    state_answer = screen.textinput(title="Guess a state", prompt=f"{correct_count} to go, enter the name of a state:").title()
    if state_answer == 'Exit':
        break
    else:
        for state in data.state:        # look at the state column
            if state_answer == state:   # compare the input to names in that column
                correct_guesses.append(state)   # add it to the dictionary if it is
                correct_count -= 1              # count down the score
                """Create a turtle instance to display the correctly
                guessed state name."""
                t = turtle.Turtle()
                t.hideturtle()   
                t.penup()
                """Retrieve the row of data for the correct input state's name."""
                state_data = data[data.state == state_answer]
                """Take the 'x' and 'y' from that row to input as the 'goto' for the name text."""
                t.goto(int(state_data.x), int(state_data.y))
                t.write(state_data.state.item())        # 'item' looks into the data, and takes the FIRST element (state name in this case)
                                                        # can just code 't.write(state_answer)'
                """Continue whilst there are still countries left to guess."""
                if correct_count > 0:                   
                    continue
                else:
                    break

states_to_learn = [state for state in data.state if state not in correct_guesses]

"""Create a new variable from the list of states to learn."""
new_data = pandas.DataFrame(states_to_learn)
"""Send that data list to a new .csv."""
new_data.to_csv("100Days\day25_CSVdata/States to learn.csv")
for state in states_to_learn:
    print(state)

turtle.mainloop()       # keeps the main loop running, won't close