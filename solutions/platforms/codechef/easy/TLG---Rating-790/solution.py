# cook your dish here
if __name__ =="__main__":
    n=int(input())
    sa=sb=0
    maxl=0
    for _ in range(n):
        a,b=map(int,input().split())
        sa+=a
        sb+=b
        lead=abs(sa-sb)
        if lead>maxl:
            maxl=lead
            if sa>sb:
                w=1
            else:
                
                w=2
    print(w,maxl)