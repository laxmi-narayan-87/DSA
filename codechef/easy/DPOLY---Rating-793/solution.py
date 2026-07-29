# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        for i in range(n-1,-1,-1):
            if a[i]==0:
                i+=1
            else:
                print(i)
                break