# cook your dish here
if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=1
    for i in range(n):
        if a[i-1]!=a[i]:
            c+=1
    print(c)
    #     if a[i-1]==a[i]:
    #         continue
    #     else:
    #         b.append(a[i])
    # print(len(b))
    