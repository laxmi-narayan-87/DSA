# cook your dish here
marks=int(input())
match marks:
    case _ if marks>90:
        print("A")
    case _ if marks >70:
        print("B")
    case _ if marks >=40:
        print("C")
    case _:
        print("F")