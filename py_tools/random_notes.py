import random

notes = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
]

amount = 25


def get_readable_text():
    print("here are your new notes")
    for i in range(amount):
        if (i % 5) == 0:
            print("-----")

        rand_id = random.randrange(0, len(notes))
        note = notes[rand_id]
        print(note)

    print("-----")


get_readable_text()
