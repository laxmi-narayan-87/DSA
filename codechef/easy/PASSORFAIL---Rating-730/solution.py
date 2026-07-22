# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y,z=map(int,input().split())
        if (x >= y and x <= z) or (x <= y and x >= z):
            print(x)
        elif (y >= x and y <= z) or (y <= x and y >= z):
            print(y)
        else:
            print(z)