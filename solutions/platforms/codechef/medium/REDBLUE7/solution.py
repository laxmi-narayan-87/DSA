# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        s=sum(a)
        sr=0
        maxvalue=0
        for k in range(1,n//2+1):
            sr+=a[n-k]
            value=sr*(n-2*k)+s*k
            maxvalue=max(value,maxvalue)
        print(maxvalue)