# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x=int(input())
        n=x%3
        if n==0:
            print("normal")
        elif n==1:
            print("huge")
        else:
            print("small")