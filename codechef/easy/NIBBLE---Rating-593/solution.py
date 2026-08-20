# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        if n%4==0:
            print("GOOD")
        else:
            print("NOT GOOD")