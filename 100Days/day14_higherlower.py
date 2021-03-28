import random
from day14_higherlowerart import logo, clear, vs
from day14_gamedata import data

def take_data():
    """ access a random choice list item """
    return random.choice(data)

def disp_data(entry):
    """ return an information string of each random selection """
    name = entry['name']
    desc = entry['description']
    country = entry['country']
    return f"{name}, a {desc} from {country}"

def compare_answer(user_in, a_followers, b_followers):
    """ determines the winners from the followers count, compares the input guess to the correct answer """
    if a_followers > b_followers:       # if 'a' has the most followers...
        return user_in == 'a'             # returns a True if the guess matches this....
    else:
        return user_in == 'b'

def run_game():
    """ runs the game... """
    print(logo)
    go_again = True
    score = 0
    entry_a = take_data()
    entry_b = take_data()
    while go_again:
        entry_a = entry_b
        entry_b = take_data()

        while entry_a == entry_b:
            entry_b = take_data()

        print(f"Compare 'A': {disp_data(entry_a)}")
        print(random.choice(vs))
        print(f"'B': {disp_data(entry_b)}...")
        
        user_in = input("Which has the most followers? 'A' or 'B'?:\n").lower()
        a_followers = entry_a['follower_count']
        b_followers = entry_b['follower_count']
        correct = compare_answer(user_in, a_followers, b_followers)

        print(clear)
        print(logo)
        if correct:
            score += 1
            print(f"Yup, {score} points so far...\nThis time,")
        else:
            go_again = False
            print("Ahhhhhh, better luck next time :(")

run_game()

# # take 2 random entries from the list of data
# for entry in range(2):
#     choice = random.choice(data)        # access a random dictionary within the list of data
#     info_str = f"{choice['name']}, {choice['description']} from {choice['country']}"       # f-string from info from that dictionary
#     comparison.append(info_str)             # and add it to the list
#     followers[choice['name']] = choice['follower_count']        # loads the name and followers into the dictionary
#     winner = max(followers.values())        # determine the biggest value from the dictionary of two entries

# # display both with vs. logo
# print(f"\n'A': {comparison[0]},\n{random.choice(vs)}\n'B': {comparison[1]}")
# print(followers)
# print(winner)

# # ask for answer from player
# if input("Which has the most followers? 'A' or 'B'?:\n").title() == 'A':
#     pass

# # compare answer with actual

# # determine winner

# # take second entry as first entry to continue play

# # ask to play again