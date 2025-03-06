import math
import re
    
def poisson(x,μ):
    possibility = []
    # if isinstance(x, list):
    #     total = 0
    #     for i in range(int(x[0]),int( x[1]) + 1):
    #         a = (math.e ** (-μ) * μ ** i) / math.factorial(i)
    #         total += a
    #     possibility.append(f"P(X = {x[0]} <= 0 <= {x[1]}) = {total}")

    if isinstance(x, str):
        thawed = re.findall(r">=|<=|\d+", x)
        if ">=" in thawed:
            total = 0
            for i in range(0, int(thawed[1]) + 1):
                a = (math.e ** (-μ) * μ ** i) / math.factorial(i)
                total += a

            res = 1 - total
            possibility.append(f"P(X = >= {thawed[1]}) = {res}")

        elif "<=" in thawed:
            total = 0
            for i in range(0, int(thawed[1]) + 1):
                a = (math.e ** (-μ) * μ ** i) / math.factorial(i)
                total += a

            possibility.append(f"P(X = <= {thawed[1]}) = {total}")

        else:
            total = 0

            charred = re.findall(r"\(|\)|\[|\]|\d+", x)

            if charred[0] == '[' and charred[-1] == ']':
                for i in range(int(charred[1]),int( charred[2]) + 1):
                    a = (math.e ** (-μ) * μ ** i) / math.factorial(i)
                    total += a
                possibility.append(f"P(X = {charred[1]} <= 0 <= {charred[2]}) = {total}")

            elif charred[0] == '(' and charred[-1] == ']':
                for i in range(int(charred[1]) + 1,int( charred[2]) + 1):
                    a = (math.e ** (-μ) * μ ** i) / math.factorial(i)
                    total += a
                possibility.append(f"P(X = {charred[1]} < 0 <= {charred[2]}) = {total}")

            elif charred[0] == '[' and charred[-1] == ')':
                for i in range(int(charred[1]),int( charred[2])):
                    a = (math.e ** (-μ) * μ ** i) / math.factorial(i)
                    total += a
                possibility.append(f"P(X = {charred[1]} <= 0 < {charred[2]}) = {total}")

            elif charred[0] == '(' and charred[-1] == ')':
                for i in range(int(charred[1]) + 1,int( charred[2]) ):
                    a = (math.e ** (-μ) * μ ** i) / math.factorial(i)
                    total += a
                possibility.append(f"P(X = {charred[1]} < 0 < {charred[2]}) = {total}")
            
    else:
        for i in range(0, x + 1):
            a = (math.e ** (-μ) * μ ** i) / math.factorial(i)
            if i == x:
                possibility.append(f"P(X = {i}) = {a}")
    
    return f"{possibility}"

#print(poisson("[2,5]",3))
print(poisson(4,3))
print(poisson(">=4",3))
print(poisson("<=4",3))
print(poisson("[3,4)",3))
print(poisson("(3,4)",3))
print(poisson("[3,4]",3))
print(poisson("(3,4]",3))
#print(poisson("[3,44]",3))