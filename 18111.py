# #마인크래프트
# #세로 N 가로 M
# # 맨 왼쪽 위 좌표 : 0, 0
# # 넣기 2초 꺼내기 1초 / 최소시간과 높이 시작 블록 B개

from sys import stdin

X = list(map(int, stdin.readline().split(' '))) #N, M, B 세로, 가로, 블록 입력 받음
N = int(X[0]) #세로
M = int(X[1]) #가로
B = int(X[2]) #제공 블록
A = [[0]*M for _ in range(N)] #높이 입력 받을 2차원 배열
L = '' #줄 입력 변수
sum = B #총 블록 개수 변수
T = 0 #총 작업 시간 변수
Max = 0 #현재 최대 높이
Min = 256 #현재 최소 높이

for i in range(0, N): #세로 반복
    L = list(map(int, stdin.readline().split(' '))) #한줄씩 입력 받음
    for j in range(0, M): #가로 반복
        A[i][j] = int(L[j]) #각 위치의 높이를 배열화
        sum += int(L[j]) #높이당 블록을 추가하여 총 블록 개수를 계산
        if int(L[j]) < Min :
            Min = int(L[j])
        if int(L[j]) > Max :
            Max = int(L[j])


answerT = 0
answerH = 0
S = Min #기준 시작 높이
while S<=Max-int((Max-Min)/2)+1 :
    if S*(N*M) > sum : break
    for i in range(0, N):
        for j in range(0, M):
            if A[i][j] < S :
                T += (S-A[i][j])
            elif A[i][j] > S :
                T += ((A[i][j]-S)*2)
    if S == Min : 
        answerT = T
        answerH = S
    elif answerT >= T : 
        answerT = T
        answerH = S
    S+=1
    T = 0


print(answerT, end=' ')
print(answerH)