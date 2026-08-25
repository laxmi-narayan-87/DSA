# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        if n%m==0 and (n//m) %2==0:
            print("Yes")
        else:
            print("NO")