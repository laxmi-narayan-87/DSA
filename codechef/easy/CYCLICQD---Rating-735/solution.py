# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b,c,d=map(int,input().split())
        if 180==(a+c) or 180 ==(b+d):
            print("YES")
        else:
            print("NO")