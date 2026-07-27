# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        count=0
        if n%2!=0:
            print("-1")
            continue
        for i in range(n):
            if a[i]==1:
                count+=1
        print((count-(n-count))//2)