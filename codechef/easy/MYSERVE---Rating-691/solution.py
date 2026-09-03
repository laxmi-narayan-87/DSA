# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        p,q=map(int,input().split())
        n=p+q+1
        r=n%4
        if r==1 or r==2:
            print("Alice")
        else:
            print("Bob")