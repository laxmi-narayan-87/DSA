# cook your dish here
if __name__=="__main__":
    x,y,k=map(int,input().split())
    if abs(x-y)<=k:
        print("YES")
    else:
        print("NO")