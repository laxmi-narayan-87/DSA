# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        b1,b2,b3=map(int,input().split())
        if b1+b2+b3<2:
            print("Water filling time")
        else:
            print("Not now")