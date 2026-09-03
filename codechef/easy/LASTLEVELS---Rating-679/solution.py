# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y,z=map(int,input().split())
        total_time= (x*y)+(((x-1)//3)*z)
        print(total_time)