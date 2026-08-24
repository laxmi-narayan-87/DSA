# cook your dish here
if __name__=="__main__":
    s=input()
    freq={}
    for x in s:
        if x.isalpha():
            if x not in freq:
                freq[x]=1
            else:
                freq[x]+=1
    # max_x=max(freq,key=freq.get)
    max_freq=max(freq.values())
    max_x=min(x for x in freq if freq[x]==max_freq )
    print(max_x)