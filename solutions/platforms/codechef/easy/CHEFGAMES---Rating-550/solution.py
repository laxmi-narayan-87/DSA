# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        r1,r2,r3,r4=map(int,input().split())
        if r1+r2+r3+r4 ==0:
            print("IN")
        else:
            print("OUT")