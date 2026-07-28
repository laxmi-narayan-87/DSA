# cook your dish here
if __name__=="__main__":
    n=int(input())
    v=list(map(int,input().split()))
    p=list(map(int,input().split()))
    v.sort()
    p.sort()
    flag=True
    for i in range(n):
        if v[i]<p[i]:
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("NO")