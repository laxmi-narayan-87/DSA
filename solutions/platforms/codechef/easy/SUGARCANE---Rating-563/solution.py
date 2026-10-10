# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        n=n*50
        # expend=(n//5)+(n//5)+((3*n)//10)
        expend=(n*.2)+(n*.2)+(n*.3)
        print(int(n-expend))