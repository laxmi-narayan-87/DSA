# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        h,x,y=map(int,input().split())
        print(math.ceil((h-y)/x)+1)