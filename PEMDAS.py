def is_operand(var):
    return var in ('0123456789')

def validate(expression):
    expression = expression.replace(" ", "")
    expression = list(expression)
    for element in expression:
        if element not in ('0123456789/*+-^()'):
            print("not here")
            return False
    return True

def operators(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1-num2
    if operation == '*':
        return num1*num2
    if operation == '/':
        return num1/num2
    if operation == '^':
        return num1 ** num2

def modArray(index, operations, numbers):
    newNum = operators(operations[index], numbers[index], numbers[index+1])
    del operations[index]
    del numbers[index+1]
    del numbers[index]
    numbers.insert(index, newNum)
    print(numbers)
def calculator(numbers, operations, j):
    for i in range(j):
        if "^" in operations:
            index = operations.index("^")
            modArray(index, operations, numbers)
        elif "*" in operations or "/" in operations:
            mult = j
            div = j
            if "*" in operations:
                mult = operations.index("*")
            if "/" in operations:
                div = operations.index("/")
            if mult < div:
                index = mult
                modArray(index, operations, numbers)
            else:
                index = operations.index("/")
                modArray(index, operations, numbers)
        elif "+" in operations:
            index = operations.index("+")
            modArray(index, operations, numbers)
        elif "-" in operations:
            index = operations.index("-")
            modArray(index, operations, numbers)
    return numbers
def analyze(numbers, expression):
    num = ""
    op = ""
    operations = []
    result = []

    expression = expression.replace(" ", "")
    expression += "z"
    expression = list(expression)
    for i in range(len(expression)):
        if(is_operand(expression[i])):
            num += expression[i]
        else:
            numbers.append(int(num))
            num = ""
            op = expression[i]
            operations.append(op)
    operations.pop()
    j = len(operations)
    return calculator(numbers, operations, j)

def calc(pairs, expression):
    for i in range(len(pairs)):
        openKey = pairs[i][0]
        closeKey = pairs[i][1]
        # print(openKey)
        # print(closeKey)
        innerOperation = expression[openKey+1:closeKey]
        innerRes = analyze([],innerOperation)
        expression = list(expression)
        del expression[openKey]
        expression.insert(openKey, str(innerRes[0]))
        # print(expression)
        cont = openKey+1
        while cont <= closeKey:
            del expression[cont]
            expression.insert(cont, " ")
            cont += 1
        expression = "".join(expression)
    return expression
def pareth(expression):
        iOpen = []
        # contOpen = 0
        iClose = []
        # contClose = 0
        pairs = []
        arr = list(expression)
        for i in range(len(arr)):
            if arr[i] == "(":
                iOpen.append(i)
                # contOpen+=1
            if arr[i] == ")":
                iClose.append(i)
                # contClose += 1
        a=0
        j=1

        while a < len(iOpen)-1:
            while j <len(iOpen):
                if iOpen[j] > iClose[a]:
                    pairs.append([iOpen[j-1],iClose[a]])
                    del iOpen[j-1]
                    del iClose[a]
                j+=1
            a += 1

        z =0
        iClose.reverse()
        while z < len(iOpen):
            pairs.append([iOpen[z],iClose[z]])
            del iOpen[z]
            del iClose[z]

        for j in range(len(pairs)):
            for i in range(len(pairs)-j-1):
                if (pairs[i][1] - pairs[i][0]) > (pairs[i+1][1] - pairs[i+1][0]):
                    
                    pairs[i], pairs[i+1] = pairs[i+1], pairs[i]

        return calc(pairs, expression)

expression = input("Digite a expressão a ser calculada: ")
if validate(expression):
    if ("(" in expression) & (")" in expression):
        expression = "("+ expression + ")"
        res = pareth(expression)
        print("\n\n\n O resultado da operação é : " + res)

    else:
        numbers = []
        analyze(numbers, expression)
        print(numbers[0])
else:
    print("error")

