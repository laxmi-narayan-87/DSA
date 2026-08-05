# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x1,y1,x2,y2=map(int,input().split())
        if (x1==y1) and (x2==y2):
            print(0)
        if abs(x1-y1)==abs(x2-y2):
            print(1)
        else:
            if(x1+y1)%2 != (x2+y2)%2:
                print("-1")
            else:
                print(2)