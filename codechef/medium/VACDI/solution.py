# cook your dish here
if __name__=="__main__":
    n=int(input())
    v=list(map(int,input().split()))
    p=list(map(int,input().split()))
    v.sort()
    p.sort()
    if v[n-1]>p[n-1]:
        print("YES")
    else:
        print("NO")