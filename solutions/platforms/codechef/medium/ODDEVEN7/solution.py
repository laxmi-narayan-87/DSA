# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        ceven=0
        for num in a:
            if num%2==0:
                ceven+=1
        ans=2*min(ceven,(n-ceven))
        if ceven!=(n-ceven):
            ans+=1
        print(ans)