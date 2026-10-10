# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        if n<m:
            print(n)
        else:
            print(n+abs(m-n))
        