# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        code=list(map(str,input().split()))
        l=s=0
        for i in range(n):
            if code[i]=="START38":
                s+=1
            else:
                l+=1
        print(s,l)
                