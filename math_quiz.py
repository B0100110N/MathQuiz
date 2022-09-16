score = 0


def greet_player():
    print("\n\nHello! Welcome to Ben's Simple Math Quiz.")


def get_name():
    print('What is your name?\n')
    return str(input('Name: ').strip())


def respond_name():
    print('\nHello, ' + name + '! Are you ready to begin?')


def is_player_ready():
    if is_ready_first.lower() == 'yes':
        print("""\nOkay, let's begin! You will be solving 5 problems, all of which are graded, so\
 be sure to keep an eye out for your total score at the end!\n\n """)
        print('Here is the first problem:\n')
        print('2 * 3 = ?\n')
    elif is_ready_first.lower() == 'no':
        print('Okay, ' + name + '. I will be here when you decide to come back!')


def first_problem():
    if int(first_answer) < 6:
        print('\nSorry, ' + name + ' that number is too low. Try again!')
    elif int(first_answer) > 6:
        print('\nSorry, ' + name + ' that is too high. Try again!')
    elif int(first_answer) == 6:
        print('\nThat is correct, ' + name + '!' + ' Your math skills are subliminal!\n')
        print('Are you ready for the second problem?')


def moving_on_second():
    if is_ready_second.lower() == 'yes':
        print('\nOkay. Here is the second problem, ' + name + ':\n')
        print('-1 * -1 = ?\n')
    elif is_ready_second.lower() == 'no':
        print('\nOkay. Take your time, ' + name + ". I'm ready when you are!\n")


def second_problem():
    if int(second_answer) < 1:
        print("\nThat answer was too low. Be sure to double check your work!")
    elif int(second_answer) > 1:
        print('\nSorry, that is too high. Remember: a negative * a negative results in a positive number.')
    elif int(second_answer) == 1:
        print('\nSpot on, ' + name + '! Are you a mathematician? The third problem awaits... are you ready?')


def moving_on_third():
    if is_ready_third.lower() == 'yes':
        print('\nOkay. Here is the third problem, ' + name + ':\n')
        print('100 / 25 = ?\n')
    elif is_ready_third.lower() == 'no':
        print('\nOkay. Take your time, ' + name + ". I'm ready when you are!\n")


def third_problem():
    if int(third_answer) < 4:
        print("\nNot quite. That answer is too low. Don't give up though, you got this! !")
    elif int(third_answer) > 4:
        print('\nOops, that answer is too high. No worries! I believe in you!')
    elif int(third_answer) == 4:
        print('\nWow! Keep up the great work!! Are you ready for the fourth problem?')


def moving_on_fourth():
    if is_ready_fourth.lower() == 'yes':
        print('\nOkay. Here is the fourth problem, ' + name + ':\n')
        print('-15 - -22 = ?\n')
    elif is_ready_fourth.lower() == 'no':
        print('\nOkay. Take your time, ' + name + ". I'm ready when you are!\n")


def fourth_problem():
    if int(fourth_answer) < 7:
        print('\nToo Low!')
    elif int(fourth_answer) > 7:
        print('\nSorry, that is too high. Try again!')
    elif int(fourth_answer) == 7:
        print('\nNice, ' + name + '! Are you ready to solve the last problem?')


def moving_on_fifth():
    if is_ready_fifth.lower() == 'yes':
        print('\nOkay. Here is the fifth and final problem, ' + name + ':\n')
        print('100000 / -1 * -1 = ?\n')
    elif is_ready_fifth.lower() == 'no':
        print('\nOkay. Take your time, ' + name + ". I'm ready when you are!\n")


def fifth_problem():
    if int(fifth_answer) < 100000:
        print('\nToo Low! Remember a negative * a negative results in a positive number!')
    elif int(fifth_answer) > 100000:
        print("\nSorry, that is too high. Try again! Did I mention you got this? Don't give up now " + name + '.')
    elif int(fifth_answer) == 100000:
        print('\nCorrect')


greet_player()
name: str = get_name()
respond_name()

is_ready_first = input()
is_player_ready()
first_answer = input('Answer: ')
score += 1
first_problem()

is_ready_second = input()
moving_on_second()
second_answer = input('Answer: ')
score += 1
second_problem()

is_ready_third = input()
moving_on_third()
third_answer = input('Answer: ')
score += 1
third_problem()

is_ready_fourth = input()
moving_on_fourth()
fourth_answer = input('Answer: ')
score += 1
fourth_problem()

is_ready_fifth = input()
moving_on_fifth()
fifth_answer = input('Answer: ')
score += 1
fifth_problem()

total_questions = 5

marks = int(score/total_questions) * 100
if marks > 70:
    print('Your final score is: ' + str(marks) + '%')
    print("WOW! You're really good at this, " + name + '!')
    print('Thanks for playing')
