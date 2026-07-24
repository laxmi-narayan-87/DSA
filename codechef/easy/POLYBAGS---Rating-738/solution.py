# cook your dish here
import math
def bagrequire(n):
    bag=math.ceil(n/10)
    return bag
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        print(bagrequire(n))