# cook your dish here
if __name__=="__main__":
    l,r=map(int,input().split())
    flag=False
    for i in range(l,r+1):
        if i %2==0:
            flag=True
            break
    if flag:
        print("YES")
    else:
        print("NO")