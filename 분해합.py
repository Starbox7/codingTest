N = int(input())
answer = 0
nums = []
sum = 0
for i in range(0, N):
    for j in str(i):
        nums.append(j)
    for k in nums:
        sum+=int(k)
    if sum+i==N:
        answer = i
        break
    nums = []
    sum = 0

print(answer)