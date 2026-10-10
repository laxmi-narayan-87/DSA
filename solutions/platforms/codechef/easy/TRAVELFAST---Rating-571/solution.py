# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y=map(int,input().split())
        if x>y:
            print("CAR")
        elif x==y:
            print("SAME")
        else:
            print("BIKE")