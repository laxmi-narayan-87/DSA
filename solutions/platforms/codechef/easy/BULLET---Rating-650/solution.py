# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y,z=map(int,input().split())
        w=max(0,(z-(y/x)))
        print(math.ceil(w))