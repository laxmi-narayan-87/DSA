# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y,z=map(int,input().split())
        m=x//3
        if (x%3==0):
            m=m-1
        total_time= (x*y)+(m*z)
        print(total_time)