# Update the '_' below to solve the problem

t = int(input())
for i in range(t): 
    a, b = map(int, input().split())
    
    # division of A by B - float / decimal result
    floatDivison = a / b
    
    # division of A by B - integer result
    integerDivison = a // b
    
    print(floatDivison, integerDivison)