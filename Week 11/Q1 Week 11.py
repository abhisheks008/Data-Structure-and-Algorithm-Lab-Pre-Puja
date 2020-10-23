def applyOp(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
    
string = []
string = input().split(" ")
f1 = string.count("(")
f2 = string.count(")")
s1 = string.count("{")
s2 = string.count("}")
t1 = string.count("[")
t2 = string.count("]")
n = len(string)
if (f1!=f2 or s1 != s2 or t1 != t2):
    print ("ERROR")
else :
    
    for i in range (0,n):
        if (string[i] == '(' and string[i+4]==')'):
            x = applyOp (int(string[i+1]),int(string[i+3]),string[i+2])
            string [i] = str(x)
            del string [i+1:i+5]
            break
            
    for i in range (0,n):
        if (string[i] == '{' and string[i+4]=='}'):
            x = applyOp (int(string[i+1]),int(string[i+3]),string[i+2])
            string [i] = str(x)
            del string [i+1:i+5]
            break
    for i in range (0,n):
        if (string[i] == '[' and string[i+4]==']'):
            x = applyOp (int(string[i+1]),int(string[i+3]),string[i+2])
            print (x)
            string [i] = str(x)
            del string [i+1:i+5]
            break 
