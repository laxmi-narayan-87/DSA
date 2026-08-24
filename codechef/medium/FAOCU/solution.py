# cook your dish here
if __name__=="__main__":
    s=input()
    p=input()
    k=len(p)
    tar=sorted(p)
    res=[]
    for i in range(len(s)-k+1):
        ran=s[i:i+k]
        if sorted(ran)==tar:
            res.append(i)
    print(*res)