'''Write a python which will keep adding a stream of numbers
inputted by the user. The adding stop as soom as user presses q key on the keyboard'''

sum = 0
while(True):
    userInput = input("Enter the item price or press q to quit: \n")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")

    else:
        print(f"Your Bill total is {sum}. Thanks for shopping with us!")
        break
