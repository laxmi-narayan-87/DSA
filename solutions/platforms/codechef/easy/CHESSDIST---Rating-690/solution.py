# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x1,y1,x2,y2=map(int,input().split())
        print(max(abs(x1-x2),abs(y1-y2)))