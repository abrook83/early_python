def disemvowel(string):
    vowels = ['a','e','i','o','u']
    for v in vowels:
        if v in string:
            print(True)
    return string

string = "This website is for losers LOL!"
disemvowel