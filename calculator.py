result = None
operand = None
operator = None
wait_for_number = True
#input first digit
while True:
    user_input = input('>>> ')
    try:
        user_input = float(user_input)
        result = user_input
        wait_for_number = False
        operand = 0
        break
    except ValueError:
        print(f"'{user_input}' is not a number. Try again.")
        
while True:
    #input math sign
    user_input = input('>>> ')
    while True:
        if user_input in ('+','-','*','/'):
            operator = user_input
            wait_for_number = True
        elif user_input == '=':
            

    if wait_for_number:
        try:
            operand = float(user_input)
            wait_for_number = False
        except ValueError:
            print(f"'{user_input}' is not a number. Try again.")

    elif user_input != '=':
        if
            if operator == '+':
                try:
                    result = result + operand
                except TypeError:
                    continue
                    
            elif operator == '-':
                try:
                    result = result - operand
                except TypeError:
                    continue
            elif operator == '*':
                try:
                    result = result * operand
                except TypeError:
                    continue
            else:
                try:
                    result = result / operand
                except ZeroDivisionError:
                    print("Cannot divide by 0")
                except TypeError:
                    continue
        else:
            print(f"'{user_input}' is not '+' or '-' or '/' or '*'. Try again")
    elif user_input == '=':
        try:
            result = float(result)
        except TypeError:
            result = operand
        print(result)
        break
