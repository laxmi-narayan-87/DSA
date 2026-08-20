# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print(fact)