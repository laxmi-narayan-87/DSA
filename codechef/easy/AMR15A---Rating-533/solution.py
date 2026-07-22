# cook your dish here
def check(n,a):
    co=ce=0
    for i in range(n):
        if a[i]%2==0:
            ce+=1
        else:
            co+=1 
    if ce>co:
        return "READY FOR BATTLE"
    else:
        return "NOT READY"
if __name__=="__main__":
    t=int(input())
    x=list(map(int,input().split()))
    print(check(t,x))