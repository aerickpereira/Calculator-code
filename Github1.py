while True:
    number_1 = input('Enter a number: ')
    number_2 = input('Enter another number: ')
    operator = input('Enter the operator (+-/*): ')
    print('peanut candyyyyyyyyyyyyyyyyyYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY!')

    valid_numbers = None

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or both numbers entered are invalid.')
        continue

    print('Performing your calculation, check the result below:')

    if operator == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)

    elif operator == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)

    elif operator == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)

    elif operator == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)

    exit_program = input('Do you want peanut candy? Yeah or no? ').lower().startswith('y')

    allowed_operators = '+-/*'

    if operator not in allowed_operators:
        print('Invalid operator.')
        continue

    if len(operator) > 1:
        print('Enter only one operator.')
        continue

    if exit_program is True:
        break

print('We love peanut candy, right?')