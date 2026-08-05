# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x=map(int,input().split())
        if x>n:
            print(0)
        else:
            print(math.ceil((n-x)/4))