# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        total=cost=ans=0
        for i in range(n):
            total+=a[i]
            cost=max(cost,a[i])
            if total-cost<=k:
                ans=i+1
        print(ans)