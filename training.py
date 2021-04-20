import random

GREETING_INPUTS = ("привет", "прив", "хай", "ку")
GREETING_RESPONSES = ["Приветствую!", "Доброго времени суток!", "Рад встрече!"]

def greet(text):
    for i in range(len(text)):
        for word in text[i]:
            if word in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)