# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,m,x=map(int,input().split())
        row=(x+m-1)//m
        print(min(row,n-row+1))