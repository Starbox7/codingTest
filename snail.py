data = input().split(' ')
day = int(data[0])-int(data[1])
date = ((int(data[2])-int(data[0]))/day)+1
print(date)
print(date%1)
if date%1>0:
    date+=1
    print(date)
print(int(date))