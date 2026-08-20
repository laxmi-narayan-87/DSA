# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x,y=map(int,input().split())
        if y==0:
            print("YES")
        elif(y%x==0):
            print("YES")
        else:
            print("NO")