# cook your dish here
def passed(x,y,z):
    ts=x*y
    percent=(z/ts)*100
    if percent>50:
        return "YES"
    else:
        return "NO"
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y,z=map(int,input().split())
        print(passed(x,y,z))