# cook your dish here
if __name__=="__main__":
    x,y=map(int,input().split())
    if x<=y:
        print("UNLOCKED")
    else:
        print(x-y)