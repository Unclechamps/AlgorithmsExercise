def userInput():
    how_tall = int(input("How many lines will this tree have? "))
    return how_tall

how_tall = userInput()

def pyramid(how_tall):
    for i in range(0, how_tall + 1):
        print((" " * (how_tall-i)) + ("*" * (2 * i + 1)))

pyramid(how_tall)
