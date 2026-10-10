# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        if c<a or d<b:
            print("Impossible")
        else:
            print("Possible")