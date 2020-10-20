'''
Question2) Write a program to input percentage marks of a student and display his grades as per given specifications
'''

# get subjects
def subjects():
    global sub_1
    sub_1 = input('What is your first subject: ')

    global sub_2
    sub_2 = input('What is your second subject: ')

    global sub_3
    sub_3 = input('What is your third subject: ')

    global sub_4
    sub_4 = input('What is your fourth subject: ')

    global sub_5
    sub_5 = input('What is your fifth subject: ')

# get percentage of each subject
def g_percentage():
    print('\nplease give the marks you got in', sub_1)
    global sub1_marks
    sub1_marks = float(input('here: '))

    print('please give the marks you got in', sub_2)
    global sub2_marks
    sub2_marks = float(input('here: '))

    print('please give the marks you got in', sub_3)
    global sub3_marks
    sub3_marks = float(input('here: '))

    print('please give the marks you got in', sub_4)
    global sub4_marks
    sub4_marks = float(input('here: '))

    global sub5_marks
    print('please give the marks you got in', sub_5)
    sub5_marks = float(input('here: '))

# calculate the percentage
def calc_percent():
    sum = sub1_marks + sub2_marks + sub3_marks + sub4_marks + sub5_marks
    dev = sum / 500
    global percentage
    percentage = dev * 100
    print('\nyour percentage is ',percentage,'%')

# main math
def math():
    if percentage >= 90 and percentage <= 100:
        print('Congrats you got "A" grade')

    if percentage >= 70 and percentage <= 89:
        print('Good you got "B" grade')

    if percentage >= 0 and percentage <= 69:
        print('Its ok you got "C" grade')

# run the code
def run():
    print('Hi this is the answer to the second question, keep in mind the marks obtained are out of 100')
    subjects()
    g_percentage()
    calc_percent()
    math()
    rerun()

# rereun the code
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