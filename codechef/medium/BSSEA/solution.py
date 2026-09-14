# cook your dish here
if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    avg=(a[0]+a[-1])/2
    close=a[0]
    for x in a:
        if (abs(x-avg)<abs(close-avg)) or (abs(x-avg)==abs(close-avg) and x<close):
            close=x
    print(close)