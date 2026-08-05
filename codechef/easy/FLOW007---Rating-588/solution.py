# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        rev=0
        for dig in reversed(str(n)):
            rev=rev*10 +int(dig)
        print(rev)