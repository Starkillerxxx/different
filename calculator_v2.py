result = None
operand = None
operator = None
wait_for_number = True

print("Це простий калькулятор, який поочередно приймає операнди та оператори. Вміє додовати, віднімати, множити та ділити. Результат виводить по знаку '=' дорівнює.")
while True:

#Input
    #First input must be digit
    while result == None:
        user_input = input('>>> ')
        try:
            result = float(user_input)
            wait_for_number = False
            break
        except:
            print("Enter digit")
    
    #All other inputs

    user_input = input('>>> ')
   
    if wait_for_number == True:
        try:
            operand = float(user_input)
            wait_for_number = False
        except:
            print("Enter digit")
            continue
    else:
        if user_input == '=': #RESULT
            print(result)
            break
        elif user_input in ('+','-','/','*'):
            operator = user_input
            wait_for_number = True
        else:
            print("Enter +, -, * or /")
            continue

    
    if operand == None:
        continue
    if wait_for_number == True:
        continue

#Calculation
    if operator == '+':
        result += operand
        operator = None
        operand = None
    elif operator == '-':
        result -= operand
        operator = None
        operand = None
    elif operator == '*':
        result *= operand
        operator = None
        operand = None
    else:
        try:
            result /= operand
            operator = None
            operand = None
        except ZeroDivisionError:
            print("You can't divide by \"0\". Try again.")
            wait_for_number = True

input("Презапустіть для нового розрахунку")