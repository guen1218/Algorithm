n = int(input())
list = []
for i in range(n):
    x, y = map(int, input().split())
    list.append([x,y])

list.sort(key=lambda l: (l[0], l[1]))
for j in range(n):
    print(list[j][0],list[j][1])