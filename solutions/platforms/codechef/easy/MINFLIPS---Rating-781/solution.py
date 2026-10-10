# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        if n % 2:
            print(-1)
            continue

        ones = sum(x == 1 for x in a)

        print(abs(ones - (n - ones)) // 2)