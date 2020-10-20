"""
Question1)Write a program to enter any three numbers  and display the largest number
"""

# Get user inputs
def user_input():
    global n_1
    n_1 = input('specify the value of the first number: ')

    global n_2
    n_2 = input('specify the value of the second number: ')

    global n_3
    n_3 = input('specify the value of the third number: ')

# check if the value is in integer form
def check():
    if n_1.isdigit() is False:
        print('\nPlease input an number and try again')
        user_input()

    if n_2.isdigit() is False:
        print('\nPlease input an number and try again')
        user_input()

    if n_3.isdigit() is False:
        print('\nPlease input an number and try again')
        user_input()

# find largest number
def main_math():
    if n_1 > n_2 and n_1 > n_3:
        print('\nThe greatest number is: ' , n_1)

    if n_2 > n_3 and n_2 > n_1:
        print('\nThe greatest number is: ' , n_2)

    if n_3 > n_1 and n_3 > n_2:
        print('\nThe greatest number is: ' , n_3)

# run the thing
def run():
    print('Hi this the the answer to the first question! Lets run it shall we!')
    user_input()
    check()
    main_math()
    rerun()

# rerun the thing creating an loop
def rerun():
    print('\nThat went great')
    g_input = input('Do you want to go again? press "y" for yes and "n" for no: ')

    if g_input.lower() == 'y' or g_input.lower() == 'yes':
        print('Fantastic lets go again')
        run()

    elif g_input.lower() == 'n' or g_input.lower() == 'no':
        print('Have a nice day!')
        quit()

    else:
        print('Please input a valid response')
        rerun()

# run the code
run()