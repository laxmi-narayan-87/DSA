# cook your dish here
def check(n,x,p):
    marks= 3*x +(-1)*(n-x)
    if p<=marks:
        return "PASS"
    else:
        return "FAIL"

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x,p=map(int,input().split())
        res=check(n,x,p)
        print(res)