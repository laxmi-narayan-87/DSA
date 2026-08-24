# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        s=sum(a)
        if s>=0 and s%2==0:
            print(s//2)
        else:
            print("-1")