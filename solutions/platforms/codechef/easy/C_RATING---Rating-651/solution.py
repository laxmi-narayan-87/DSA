# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y=map(int,input().split())
        game=(y-x)/8
        print(math.ceil(game))