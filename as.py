a = int(input())
b = int(input())

count = 0
li = list(map(int,input().split()))
li.sort()
st = 0
en = len(li)-1

while st < en :
    if li[st] + li[en] == b :
        print("같다")
        st += 1
        en -= 1
        count += 1
    if li[st] + li[en] > b :
        print("크다")
        en -= 1
    if li[st] + li[en] < b :
        print("작다")
        st += 1
        
print(count)