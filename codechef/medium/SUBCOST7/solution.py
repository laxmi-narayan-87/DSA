# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x,y=map(int,input().split())
        if n<=3:
            print(n*x)
        else:
            print((3*x)+((n-3)*y))