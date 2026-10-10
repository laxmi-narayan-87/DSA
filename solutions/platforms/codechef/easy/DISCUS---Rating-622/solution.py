# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        print(max(a,b,c))