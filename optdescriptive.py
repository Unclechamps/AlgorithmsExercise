number_in_alpha = input("Enter number to convert to words: ")

words = ""

nums_single = {'0': ' ' , '1' : 'One', '2' : 'Two', '3' : 'Three', '4' : 'Four', '5' : 'Five', '6' : 'Six', '7' : 'Seven', '8' : 'Eight', '9' : 'Nine'}
nums_teenagers = {'10' : 'Ten', '11': 'Eleven', '12' : 'Twelve', '13' : 'Thirteen', '14' : 'Fourteen', '15' : 'Fifteen', '16' : 'Sixteen', '17' : 'Seventeen', '18' : 'Eighteen', '19' : 'Nineteen'}
nums_tens = {'2' : 'Twenty', '3' : 'Thirty', '4' : 'Fourty' , '5' : 'Fifty', '6' : 'Sixty', '7' : 'Seventy', '8' : 'Eighty', '9' : 'Ninety'}

def ones(number_in_alpha):
    for num in nums_single:
        if number_in_alpha == num:
            words = nums_single[num]
            return (words)

def teenagers(number_in_alpha):
    for num in nums_teenagers:
        if number_in_alpha == num:
            words = nums_teenagers[num]
            return (words)

def tens(number_in_alpha):
    first_number = number_in_alpha[0]
    second_number = number_in_alpha[1]
    for num in nums_tens:
        if first_number == num:
            words = nums_tens[num] + " " + nums_single[second_number]
            return (words)

number = int(number_in_alpha)

if number > 0 and number < 10:
    words = ones(number_in_alpha)
elif number >= 10 and number <= 19:
    words = teenagers(number_in_alpha)
elif number >= 20 and number <= 99:
    words = tens(number_in_alpha)
elif number_in_alpha == '100':
    words = 'One Hundred'

print(words)





    # for i in nums_single:
    #         #
    #     for i in nums_teenagers:
    #         if number_in_alpha == i:
    #             words = nums_teenagers[i]
    #         print(word)
    #
    #     for i in nums_tens:
    #         if str(number_in_alpha[0]) == i:
    #             words = nums_tens[i] + nums_single[str(number_in_alpha)[1]]
    #         print(word)
