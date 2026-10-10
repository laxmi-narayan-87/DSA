# cook your dish here
def fact(n):
    prod=1
    for i in range(1,n+1):
        prod=i*prod
    return prod
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        print(fact(n))