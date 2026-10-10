# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        maxsum=0
        for i in range(2*n):
            maxsum+= max(a[i],a[2*n-i-1])
        print(maxsum//2)