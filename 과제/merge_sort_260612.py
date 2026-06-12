def merge_sort(lists, left, right):
    # 칠판 필기: if (left < right)
    if left < right:
        mid = (left + right) // 2
        
        # 칠판 필기: merge_sort(lists, left, mid)
        merge_sort(lists, left, mid)
        # 칠판 필기: merge_sort(lists, mid + 1, right)
        merge_sort(lists, mid + 1, right)
        
        # 칠판 필기: merge(lists, left, mid, right)
        merge(lists, left, mid, right)

def merge(lists, left, mid, right):
    temp = []
    # 칠판 필기: i는 왼쪽 구역 시작점, j는 오른쪽 구역 시작점
    i = left
    j = mid + 1

    # 두 구역 중 하나가 끝날 때까지 비교하며 temp에 수집
    while i <= mid and j <= right:
        if lists[i] < lists[j]:
            temp.append(lists[i])
            i += 1
        else:
            temp.append(lists[j])
            j += 1

    # 칠판 필기 2번째 장: 남은 찌꺼기들 전부 털어넣기
    while i <= mid:
        temp.append(lists[i])
        i += 1
    while j <= right:
        temp.append(lists[j])
        j += 1

    # [매우 중요] 임시 방(temp)의 내용물을 원본(lists)의 원래 구역[left ~ right]에 복사
    for k in range(len(temp)):
        lists[left + k] = temp[k]

lists = [5,21,14,3,31,8,27,15]
merge_sort(lists, 0, len(lists)-1)
print(lists)