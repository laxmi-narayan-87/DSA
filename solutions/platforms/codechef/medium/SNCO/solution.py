# cook your dish here
if __name__=="__main__":
    a,x,b,y=map(int,input().split())
    if a*x==b*y:
        print("YES")
    else:
        print("NO")