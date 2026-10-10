# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,k,m=map(int,input().split())
        print(math.ceil(n/(k*m)))