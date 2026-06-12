n = int(input())
lists = []
for i in range(n):
    lists.append(input())

for j in sorted(list(set(lists)), key=lambda l: (len(l), l)):
    print(j)