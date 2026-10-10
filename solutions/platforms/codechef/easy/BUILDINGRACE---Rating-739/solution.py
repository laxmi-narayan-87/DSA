# cook your dish here

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b,x,y=map(int,input().split())
        f1=a/x
        f2=b/y
        if f1==f2:
            print("Both")
        elif f1<f2:
            print("Chef")
        else:
            print("Chefina")