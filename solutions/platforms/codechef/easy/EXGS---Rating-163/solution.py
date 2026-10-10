# cook your dish here
if __name__=="__main__":
    x,y=map(int,input().split())
    total=x*100+((y-x)*150)
    print(total)