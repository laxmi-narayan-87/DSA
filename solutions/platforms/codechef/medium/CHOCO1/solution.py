# cook your dish here
import math

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        l,b=map(int,input().split())
        print(math.gcd(l,b))