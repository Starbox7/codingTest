import math
N = int(input())
count = 0
answer = 0
X = input().split()
while N:
    if int(math.sqrt(int(X[count])))*int(math.sqrt(int(X[count])))==int(X[count]):
        answer = 1
    if N == 1 :
        print(answer)
    else:
        print(answer, end=" ")
    answer=0
    N-=1
    count+=1