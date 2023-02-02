t = int(input())
item = []
data = {}
data['clothes'] = []
while t :
    num = int(input())
    count = 0
    while num :
        clothes = input().split(' ')
        if clothes[1] in item:
            data['clothes'][clothes[1]] += 1
        else :
            item.append(clothes[1])
            data['clothes'].append({
                clothes[1] : 1
            })
        num-=1
    for i in range(0, len(data['clothes'])):
        count*=data['clothes'][i]
    count-=1
    print(count)
    t-=1