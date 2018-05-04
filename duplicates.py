#working under the assumption that I had to ask for an input
total_names = int(input("How many names do you want to enter? "))

def userInput():
    list_of_names = []
    for num in range(1, total_names+1):
        list_of_names.append(input("Please enter a name: "))
    return list_of_names

list_of_names = userInput()

def find_duplicate(list_of_names):
    unique_names = []
    for name in list_of_names:
        if name not in unique_names:
            unique_names.append(name)
    print (unique_names)

find_duplicate(list_of_names)
