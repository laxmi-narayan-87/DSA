# cook your dish here
def greateraverage(a,b,c):
    avg=(a+b)/2
    if avg>c:
        return "YES"
    else:
        return "NO"

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        print(greateraverage(a,b,c))