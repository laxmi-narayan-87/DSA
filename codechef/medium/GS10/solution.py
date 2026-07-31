t = int(input())       

for i in range(t):     
    # accept 2 integers on the 1st line using map
    A,B=map(int,input().split())
    
    # accept 3 integers on the 2nd line using map
    C,D,E=map(int,input().split())
    
    # output the 5 integers on a single line for each test case
    print(A, B, C, D, E , end=" ")
