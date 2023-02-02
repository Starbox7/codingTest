t = int(input())
nums = []
nums.append(0)
count = 2
while t:
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, n+1):
                if i/j in nums: ()
                else :
                    nums.append(i/j)
                    count+=1

    t-=1
    print(count)
    count = 2
    nums = []
