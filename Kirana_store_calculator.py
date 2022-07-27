'''
Write a python program which will keep adding a stream of
product price entered by user. The adding stops as soon as
user entered q or any other key other than digit.
'''

total = 0
while(True):
    inp = input("Enter the price or press q to Quit \n")
    if inp.isnumeric():
        total = total + int(inp)
        print(f"Total order price till now is : {total}")
    elif inp == 'q':
        print("Thanks for visiting Abhinav's Sweets Shop!!!")
        print(f"Your total price is : {total}")
        break
    else:
        print("Invalid input")
        break