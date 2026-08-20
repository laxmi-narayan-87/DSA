# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,a,b= map(int,input().split())
        if x<=(a+2*b):
            print("QUALIFY")
        else:
            print("NOTQUALIFY")