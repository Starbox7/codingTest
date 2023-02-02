n, m = input().split()
n = int(n)
m = int(m)
list = []
list = input().split()
l = len(list)
for i in range(0,l):
    list[i] = int(list[i])
sum = 0
store = 0
for x in range(0, l):
    q = list[x]
    for y in range(0, l):
        if x!=y:
            w = list[y]
            for z in range(0, l):
                if (z!=x)&(z!=y) :
                    e = list[z]
                    store = q+w+e
                    if (store<=m)&(store>sum) :
                        sum = store

print(sum)