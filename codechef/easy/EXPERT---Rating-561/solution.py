# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y=map(int,input().split())
        p=(y/x)*100
        if p>=50:
            print("YES")
        else:
            print("NO")