# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x,k=map(int,input().split())
        print(min(n,(k//x)))