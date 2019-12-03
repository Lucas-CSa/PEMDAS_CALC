def is_operand(var):
    return var in ('0123456789')

def execute(nbrs):
  if len(nbrs) < 2:
    return nbrs
  stack = []
  a = 0
  b = 0
  r = 0
  for i in nbrs:
    if i == "+":
      a = stack.pop()
      b = stack.pop()
      r = b + a
      stack.append(r)
    elif i == "-":
      a = stack.pop()
      b = stack.pop()
      r = b - a
      stack.append(r)
    elif i == "*":
      a = stack.pop()
      b = stack.pop()
      r = b * a
      stack.append(r)
    elif i == "/":
      a = stack.pop()
      b = stack.pop()
      r = b / a
      stack.append(r)
    elif i == "^":
      a = stack.pop()
      b = stack.pop()
      r = b ** a
      stack.append(r)
    else:
      stack.append(i)
  print(stack)
  print(stack.pop())

def analyze(line):
    line = line.replace(" ", "")
    line += "z"
    line = list(line)
    num = ""
    nbrs = []
    op = ""
    oprs = []
    print(line)
    print(nbrs)
    print(oprs)
    for i in range(len(line)):
      if(is_operand(line[i])):
        num += line[i]
        print(num)
      else:
        if num != "":
          nbrs.append(int(num))
          num = ""
        op = line[i]
        oprs.append(op)
        if len(oprs) > 1 and oprs[len(oprs) - 1] == "*":
          print("check order: *")
          if oprs[len(oprs) - 2] == "^" or oprs[len(oprs) - 2] == "/":
            print('Wrong Order')
            nbrs.append(oprs[len(oprs) - 2])
            del oprs[len(oprs) - 2]
        if len(oprs) > 1 and oprs[len(oprs) - 1] == "-" or oprs[len(oprs) - 1] == "+":
          print("Check the Order")
          if oprs[len(oprs) - 2] == "^" or oprs[len(oprs) - 2] == "/" or oprs[len(oprs) - 2] == "*":
            print('Wrong Order')
            nbrs.append(oprs[len(oprs) - 2])
            del oprs[len(oprs) - 2]
        if len(oprs) > 1 and oprs[len(oprs) - 1] == "/":
          print("check order: /")
          if oprs[len(oprs) - 2] == "^" or oprs[len(oprs) - 2] == "*":
            print('Wrong Order')
            nbrs.append(oprs[len(oprs) - 2])
            del oprs[len(oprs) - 2]
    oprs.pop()
    print(nbrs)
    print(oprs)
    oprs = oprs[::-1]
    for i in oprs:
      nbrs.append(i)
    print(nbrs)
    execute(nbrs)




expression = input('Qual expressão a ser calculada: ')
analyze(expression)