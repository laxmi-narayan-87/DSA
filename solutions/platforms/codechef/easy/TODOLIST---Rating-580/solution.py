# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        d=list(map(int,input().split()))
        count=0
        for i in range(n):
            if d[i]>=1000:
                count+=1
        print(count)