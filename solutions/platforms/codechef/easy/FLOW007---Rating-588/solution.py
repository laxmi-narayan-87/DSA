# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=str(input())
        print(int("".join(reversed(n))))