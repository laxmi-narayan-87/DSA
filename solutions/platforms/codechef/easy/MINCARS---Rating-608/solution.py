# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        # print(math.ceil(n/4))
        if n%4==0:
            print(n//4)
        else:
            print((n//4)+1)