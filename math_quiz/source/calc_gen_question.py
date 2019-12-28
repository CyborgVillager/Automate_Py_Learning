from random import randint

def calculate_Answer(left_hand_side, right_hand_side, operator):
    if (operator == '-'):
        return left_hand_side - right_hand_side
    if (operator == '+'):
        return left_hand_side + right_hand_side
    if (operator == '*'):
        return left_hand_side * right_hand_side
    if (operator == '/'):
        return left_hand_side / right_hand_side
    raise Exception('Unknown Operator, please try again!')


def generate_Question():
    left_hand_side = randint(0, 10)
    right_hand_side = randint(0, 10)
    operator_Choose = '/*-+'
    operator_Index = randint(0, len(operator_Choose) - 1)  # prevents going out of bounds
    operator = operator_Choose[operator_Index]

    while (right_hand_side == 0 and operator == '/'):
        right_hand_side == randint(0, 10)

    return left_hand_side, right_hand_side, operator


"""
for index in range(100):
    results = generate_Question()
    if(results[1] == 0):
      print(results)
"""
