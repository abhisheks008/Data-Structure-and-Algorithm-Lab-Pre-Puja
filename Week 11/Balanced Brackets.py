def is_matched(expression):
    s = []
    for e in expression: 
        if (e == '{'):
            s.append('}')
        elif (e == '['):
            s.append(']')
        elif (e == '('):
            s.append(')')
        else:
            if (s == [] or e != s[-1]):
                return False
            s.pop();
    return (s ==[])

t = int(input())
for a0 in range(0,t):
    expression = input()
    if (is_matched(expression) == True):
        print ("YES")
    else:
        print ("NO")
