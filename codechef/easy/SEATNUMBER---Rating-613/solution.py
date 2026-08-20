# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        s1=[1,2,3,4,5,6,7,8,9,10]
        s2=[11,12,13,14,15]
        s3=[16,17,18,19,20,21,22,23,24,25]
        s4=[26,27,28,29,30]
        if n in s1:
            print("Lower Double")
        elif n in s2:
            print("Lower Single")
        elif n in s3:
            print("Upper Double")
        else:
            print("Upper Single")