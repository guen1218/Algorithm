n = int(input())
list = []
for i in range(n):
    age, name = input().split()
    list.append([int(age), name])

list.sort(key=lambda l: l[0])
for j in range(n):
    print(list[j][0],list[j][1])