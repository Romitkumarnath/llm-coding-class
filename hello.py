import random

greetings = [
    "Hello there, wonderful world!",
    "Greetings, fellow earthling!",
    "Hey, you wonderful human!",
    "Top of the morning to you!",
    "Welcome to this magnificent day!",
    "Hey there, sunshine!",
    "Salutations from your friendly program!",
    "Well hello, fancy meeting you here!",
    "G'day mate!",
    "Howdy, partner!",
    "Welcome aboard the code express!",
    "Welcome aboard the code express again !"
    ]

def get_random_greeting():
    return random.choice(greetings)

if __name__ == "__main__":
    print(get_random_greeting())
