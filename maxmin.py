data = input().split(' ')
if int(data[0])>int(data[1]):
    a = int(data[0])
    b = int(data[1])
else :
    a = int(data[1])
    b = int(data[0])

r1 = b
r2 = a%b
store = 0
if r2==0 :
    max = b
    min = a
else :
    while 1 :
        if r1%r2==0:
            max = r2
            break
        store = r1
        r1 = r2
        r2 = store%r2

min = (a*b)/max
print(max)
print(int(min))