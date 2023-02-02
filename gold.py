global nums 
def solve(n) :
    m=1
    temp = int(n/2)
    while 1 :
        if nums[temp]==False:
            print(str(temp)+" "+str(temp))
            break;
        if nums[temp-m]==False and nums[temp+m]==False:
            print(str(temp-m)+" "+str(temp+m))
            break
        m+=1
        
nums = [False] * 10001
for i in range(2,10001):
    j=2
    if nums[i] == True:
        continue
    while j:
        if i*j<10001:
            nums[int(i*j)] = True
        else: break
        j+=1
t = int(input())
while t :
    n = int(input())
    solve(n)
    t-=1

    