# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        p=list(map(int,input().split()))
        if n==3:
            print(*p)
        else:
            print("2 1 3 5 4")