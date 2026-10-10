# The code below is incorrect. Debug the code to solve the problem

t = int(input())
for i in range(t):
    X, N = map(int, input().split())
    points_per_testcase = X//10
    score = points_per_testcase*N
    print(score)