# cook your dish here
if __name__=="__main__":
    r,o,c=map(int,input().split())
    leftover=20-o
    runleft=r+2-c
    if (runleft//leftover)>36:
        print("NO")
    else:
        print("YES")