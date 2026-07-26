# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=list(input())
        for i in range(n):
            ch=s[i]
            match ch:
                case "A":
                    s[i]="T"
                case "T":
                    s[i]="A"
                case "C":
                    s[i]="G"
                case "G":
                    s[i]="C"
        print("".join(s))