# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        if n%2!=0:
            print("-1")
        else:
            s=sum(a)
            print(abs((s//2))