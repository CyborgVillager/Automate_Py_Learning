from calc_gen_question import *
from text_color import *


# from calc_gen_question import generate_Question

def question_accurate(givenanswer, correct_Answer, tolerance=0.01):
    difference = abs(float(givenanswer) - float(correct_Answer))
    return difference <= tolerance


user_question_choice = int(input('How many questions would you like to complete today? '))
question_number = int(user_question_choice)
total_questions = question_number
user_current_question = 1
correct = 0

for i in range(total_questions):
    question = generate_Question()
    correct_answer = calculate_Answer(question[0], question[1], question[2])
    print('--- Question #' + str(user_current_question) + ' ---')
    print('    {0} {2} {1}'.format(question[0], question[1], question[2]))
    print('---     ---     ---')
    user_input = input('Enter Answer: ')
    user_current_question += 1
    if (question_accurate(correct_answer, user_input)):
        print(color.YELLOW + color.BOLD + 'Correct!' + color.END)
        correct += 1
    else:
        print('Sorry thats' + color.RED + ' incorrect' + color.END +'. The correct answer is: ' +
              color.YELLOW + color.BOLD + str(correct_answer) + color.END)

print('You\'ve got {0} correct out of {1}. Or {2}% correct!'.format(correct, total_questions,
                                                                    correct / total_questions * 100))
