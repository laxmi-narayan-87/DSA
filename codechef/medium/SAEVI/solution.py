# cook your dish here
if __name__=="__main__":
    n,k= map(int,input().split())
    a=list(map(int,input().split()))
    sume=0
    for i in range(n,2):
        if a[i]> 2*k:
            sume=sume+a[i]
    print(sume)