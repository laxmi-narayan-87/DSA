# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        w=list(map(int,input().split()))
        count=0
        for i in range(len(w)):
            if (w[i]+k)%7==0:
                count+=1
        print(count)