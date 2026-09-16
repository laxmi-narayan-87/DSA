# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        if k==n-1:
            print("NO")
        else:
            print("YES")