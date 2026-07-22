# cook your dish here
import math
def cost(n,x):
    groups=math.ceil(n/6)
    cost=groups*x
    return cost


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x=map(int,input().split())
        print(cost(n,x))