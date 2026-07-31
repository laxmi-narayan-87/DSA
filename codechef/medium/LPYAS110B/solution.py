# cook your dish here
s=str(input())
nv=0
i=0
while i<len(s):
    if s[i] in "aeiou":
        nv+=1
    i+=1
print(nv)