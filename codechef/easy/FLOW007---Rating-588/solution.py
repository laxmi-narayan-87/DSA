# cook your dish here
if __name__ =="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        rev=0
        while n>0:
            dig=n%10
            rev=rev*10+dig
            n//=10
        print(rev)