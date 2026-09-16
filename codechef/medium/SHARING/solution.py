# cook your dish here
if __name__=="__main__":
    a,b=map(int,input().split())
    if (a-b)%2==0:
        print((a-b)//2)
    else:
        print("-1")