# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        x=n//7
        if n%7>=2:
            x+=1
        print(x)