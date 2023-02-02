N = int(input())
i = 1
j = 2
answer = 2
while i :
    if N == 1 :
        answer = 1
        break
    if N <= (6*i)+1:
        break

    answer+=1
    i+=j
    j+=1

print(answer)