# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        req=21-(a+b)
        if 1<=req<=10:
            print(req)
        else:
            print("-1")