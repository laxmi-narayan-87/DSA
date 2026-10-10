# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        p=list(map(int,input().split()))
        change=True
        while change:
            change=False
            for i in range(n-1):
                if p[i]>p[i+1] and abs(p[i]-p[i+1])>1:
                    p[i],p[i+1]=p[i+1],p[i]
                    change=True
        print(*p)