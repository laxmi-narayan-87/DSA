# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        if a<b:
            print("<")
        elif a>b:
            print(">")
        else:
            print("=")