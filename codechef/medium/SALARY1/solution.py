# cook your dish here

def earning(s,b,r):
    total = s+b*r
    return total

if __name__=="__main1__":
    s,b,r= map(int,input().split())
    print(earning(s,b,r))
    
if __name__=="__main__":
    s,b,r=map(int,input().split())
    total=s+b*r
    print(total)