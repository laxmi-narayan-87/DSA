# cook your dish here
if  __name__=="__main__":
    x,a,y,b,d=map(int,input().split())
    if ((x*a)+(y*b)) >=d:
        print("YES")
    else:
        print("NO")