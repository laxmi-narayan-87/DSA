# cook your dish here
if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    c=0
    for i in range(len(a)):
        if i==x:
            c+=1
            if c==2:
                inde=i
    if c==0:
        print("-1")
    elif c==1:
        print("-2")
    else:
        print(inde)