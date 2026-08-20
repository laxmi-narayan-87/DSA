# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x=map(int,input().split())
        a=list(map(int,input().split()))
        count=0
        for i in range(n):
            if a[i]>=x:
                count+=1
        print(count)