# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b,k=map(int,input().split())
        print(math.ceil((abs(b-a)/k)))