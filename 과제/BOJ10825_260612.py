n = int(input())
list = []
for i in range(n):
    name, a, b, c = input().split()
    list.append([name, int(a), int(b), int(c)])

list.sort(key=lambda l: (-l[1], l[2], -l[3], l[0]))
for j in range(n):
    print(list[j][0])