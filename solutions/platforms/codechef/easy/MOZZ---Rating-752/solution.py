# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y,r=map(int,input().split())
        n=(x+(r/30))/y
        print (math.ceil(n))