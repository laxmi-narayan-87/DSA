# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=list(map(int,input().split()))
        freq={}
        for x in s:
            ms=x.bit_length()-1
            freq[ms]=freq.get(ms,0)+1
        print(max(freq.values()))