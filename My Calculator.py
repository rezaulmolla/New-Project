print('Welcome to my calculator.\n')
print('Input your desired operation here:')

while True:
    try:
        n1 = float(input('Enter the first number: '))
        operator = input('Enter an operator (+, -, *, /): ')
        n2 = float(input('Enter the second number: '))
        
        if operator == '+':
            result = n1 + n2
            print(f'\nThe result of {n1} {operator} {n2} = {result}')
        elif operator == '-':
            result = n1 - n2
            print(f'\nThe result of {n1} {operator} {n2} = {result}')
        elif operator == '*':
            result = n1 * n2
            print(f'\nThe result of {n1} {operator} {n2} = {result}')
        elif operator == '/':
            if n2 == 0:
                print('\nSyntax Error: Cannot divide by zero.')
            else:
                result = n1 / n2
                print(f'\nThe result of {n1} {operator} {n2} = {result}')
        else:
            print('\nInvalid operator. Please choose one of: +, -, *, /')

    except ValueError:
        print('\nInput Error: Invalid input. Please enter only numeric values.')

    choice = input('\nDo you want to perform another operation? (yes to continue, no to exit): ').strip().lower()
    if choice != 'yes':
        print('Thank you for using my calculator.')
        break
