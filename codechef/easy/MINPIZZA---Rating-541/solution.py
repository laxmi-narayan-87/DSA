# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x=int(input())
        if x>5000:
            print(x-500)
        elif  5000>=x>1000:
            print(x-100)
        elif 1000>=x>100:
            print(x-25)
        else:
            print(x)