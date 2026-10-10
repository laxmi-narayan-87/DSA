# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        total=sum(a)
        rem=sum(a[n-k:n])
        minr=rem
        lefts=0
        rights=sum(a[n-k+1:n])
        for x in range(1,k+1):
            lefts+=a[x-1]
            rem=lefts+sum(a[n-(k-x):n]) if k-x>0 else lefts
            minr=min(minr,rem)
        print(total-minr)