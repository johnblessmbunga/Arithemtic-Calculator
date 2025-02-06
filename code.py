import os


#functions
def plus_minus(symbol_array):
    #simplflies series of + and - to either or
    countpm = 0
    countms = 0
    for i in range(len(symbol_array) - 1, -1, -1):
        #check if current instance is + or -
        if symbol_array[i] == '+' or symbol_array[i] == '-':
            countpm += 1
            if symbol_array[i] == '-':
                countms += 1
        #deals with assigmnet
        if countpm == 1 and symbol_array[i] not in ['+', '-']:
            #only one in series
            countpm = 0
            countms = 0
        elif countpm > 1:
            #series detected
            if i == 0 and symbol_array[0] in ['+', '-']:
                #reached start
                a = 0
            elif symbol_array[i] not in ['+', '-']:
                #series ended
                a = 1
            else:
                a = -1
            if a != -1:
                for j in range(countpm + i - 1 + a, i + a, -1):
                    #remove redundant symbols
                    symbol_array.pop(j)
                countpm = 0
                if countms % 2 == 0:
                    symbol_array[i + a] = '+'
                else:
                    symbol_array[i + a] = '-'
                countms = 0
    return symbol_array


def transform_numbers(user_input):
    #users input will be changed form a string to list of
    #numbers and symbols

    #seperating elements based on symbols
    user_input = user_input.replace(" ", "")
    user_input = user_input.replace("+-", "-")
    user_input = user_input.replace("+", " + ")
    user_input = user_input.replace("-", " - ")
    user_input = user_input.replace("/", " / ")
    user_input = user_input.replace("*", " * ")
    user_input = user_input.replace("x", " * ")
    user_input = user_input.replace("(", "( ")
    user_input = user_input.replace(")", " )")
    user_input = user_input.replace("  ", " ")
    symbols = user_input.split(" ")
    #ensures no empty spaces in list
    symbols = list(filter(None, symbols))
    output = []
    #change number strings to intergers or floats
       for i in range(len(symbols)):
        is_float = 1
        try:
            float(symbols[i])
        except ValueError:
            is_float=0
        #add the transform number or string to output
        if is_float == 1:
            output.append(float(symbols[i]))
        else:
            output.append(symbols[i])
    output = plus_minus(output)
    return output


def one_operation(symbol_array, point, symbol):
    # performs one operation(+,-,/,*) with two numbers
    #take numbers
    int1 = symbol_array[point - 1]
    int2 = float('inf')
    out_of_bound = 0
    if point + 1 >= len(symbol_array):
        #if no further element
        out_of_bound = 1
    elif symbol_array[point + 1] in ['-', '+']:
        #if second number has sign
        if point + 2 < len(symbol_array):
            if symbol_array[point + 1] == '-':
                if isinstance(symbol_array[point + 2], int) or isinstance(symbol_array[point + 2], float):
                    symbol_array[point + 1] = -symbol_array[point + 2]
            else:
                symbol_array[point + 1] = symbol_array[point + 2]
            symbol_array.pop(point + 2)

    if out_of_bound == 0:
        int2 = symbol_array[point + 1]
    answer = 0
    #perform one operation based on symbol
    if out_of_bound == 1:
        answer = 'nan'
        print('Invalid Operation Detected')
    elif isinstance(int1, str) or isinstance(int2, str):
        #if one number is a symbol or string
        answer = 'nan'
        print('Invalid Operation Detected')
    elif symbol == '+':
        answer = int1 + int2
    elif symbol == '-':
        answer = int1 - int2
    elif symbol == 'x' or symbol == '*':
        answer = int1 * int2
    elif symbol == '/':
        if int2 == 0:
            print('Divide by zero detected')
            answer = 'nan'
        else:
            answer = int1 / int2
    symbol_array[point] = answer
    #remove adjacent elements
    if out_of_bound == 0:
        symbol_array.pop(point + 1)
    symbol_array.pop(point - 1)
    return symbol_array


def one_line_operations(symbol_array):
    #performs operations from right to left while considering bimdas(not brackets)
    # if first number is negative or positive change first number attribute and remove sign
    if len(symbol_array) >= 2:
        if symbol_array[0] in ['-', '+']:
            if isinstance(symbol_array[1], int) or isinstance(symbol_array[1], float):
                if symbol_array[0] == '-':
                    symbol_array[0] = -symbol_array[1]
                else:
                    symbol_array[0] = symbol_array[1]
                symbol_array.pop(1)
    #mutiplication and division done first
    n1 = symbol_array.count('*')
    n2 = symbol_array.count('/')
    m1 = n1 + n2
    #only runs if multiplication or division detected
    for i in range(m1):
        p1 = float('inf')
        p2 = float('inf')
        #check if any multiplication or division left and and their location
        if '*' in symbol_array:
            p1 = symbol_array.index('*')
        if '/' in symbol_array:
            p2 = symbol_array.index('/')
        #perform operation closer to right side
        if p1 < p2:
            symbol_array = one_operation(symbol_array, p1, '*')
            n1 = n1 - 1
        elif p2 < p1:
            symbol_array = one_operation(symbol_array, p2, '/')
            n2 = n2 - 1
    #now for addition and substraction
    n1 = symbol_array.count('+')
    n2 = symbol_array.count('-')
    m1 = n1 + n2
    #only runs if addition or subtraction detected
    for ii in range(m1):
        p1 = float('inf')
        p2 = float('inf')
        #check if any addition or subtraction left and their location
        if '+' in symbol_array:
            p1 = symbol_array.index('+')
        if '-' in symbol_array:
            p2 = symbol_array.index('-')
        #perform operation closer to right side
        if p1 < p2:
            symbol_array = one_operation(symbol_array, p1, '+')
            n1 -= 1
        elif p2 < p1:
            symbol_array = one_operation(symbol_array, p2, '-')
            n2 -= 1
    return symbol_array


def bimdas(symbol_array):
    #performs operations based on brackets
    #find number of bracket elements
    n = symbol_array.count('(')
    nn = symbol_array.count(')')
    if nn != n:
        #unclosed bracket
        print('Unclosed bracket detected')
    elif n == 0:
        #no brackets
        symbol_array = one_line_operations(symbol_array)
    else:
        #perform all bracket elements
        for i in range(n):
            #detect back brace
            back_brace = symbol_array.index(')')
            front_brace = float('inf')
            for j in range(back_brace, - 1, -1):
                #detect corresponding front brace
                if symbol_array[j] == '(':
                    front_brace = j
                    break
            if front_brace != float('inf'):
                #front bracket detected and compute inside bracket
                answer = one_line_operations(symbol_array[front_brace + 1:back_brace])
                for k in range(back_brace, front_brace, -1):
                    #remove redundant elements
                    symbol_array.pop(k)
                if len(answer) >= 1:
                    #put answer as long as not empty
                    symbol_array[front_brace] = answer[0]
            else:
                #no closed bracket
                print('Bracket Error Detected')
        #all brackets removed
        symbol_array = one_line_operations(symbol_array)
    return symbol_array


#code
#instructions
os.system('cls')
print('Calculator that performs the following operations:',
      '\naddition subtraction, multiplication and division.',
      '\nUse the following symbols: +-/*x()')
#user input
input_equation = input('Input equation:')
#transform user input
os.system('cls')
equation = transform_numbers(input_equation)
equation_display = ''
for z in equation:
    equation_display = equation_display + str(z)
#perform operation
final_answer = bimdas(equation)
#print answer or error
if len(final_answer) == 1:
    if isinstance(final_answer[0], int) or isinstance(final_answer[0], float):
        #computed number
        print(equation_display, ' = ', final_answer[0])

    else:
        #some error occurred
        print('Failed Computation')
else:
    #string produced
    print('Failed Computation')
