# mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)
print(mean) # 20.2


# median
list2 = [12, 18, 30, 26, 15, 28, 25, 23, 24, 20]
list2.sort()

if len(list2) % 2 == 0:
    m1 = list2[len(list2)//2]
    m2 = list2[len(list2)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list2[len(list2)//2]
print(median) # 23.5


# mode
list3 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list3:
    frequency.setdefault(i, 0) # {12: 0, 16: 0, 20: 0, 30: 0, 25: 0, 23: 0, 24: 0}
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        print(i) # 20
