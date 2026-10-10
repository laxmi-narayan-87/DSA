# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b,x,y=map(int,input().split())
        if (a*b)<=(x*y):
            print("YES")
        else:
            print("NO")