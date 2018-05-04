#working under the assumption that I had to ask for an input
element = int(input("How many elements do you want to enter? "))

def userInput():
    list_of_elements = []
    for num in range(1, element+1):
        list_of_elements.append(int(input("Please enter an element: ")))
    return list_of_elements

elements_array = userInput()

def find_element(elements_array):
    largest_element = 0
    for i in range(0, len(elements_array)):
        if elements_array[i] > largest_element:
            largest_element = elements_array[i]

    print(f"The largest element is {largest_element}.")

find_element(elements_array)
