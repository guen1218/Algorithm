def quick_sort(lists, left, right):
    # 칠판 필기: if (left < right)
    if left < right:
        # 분할 작전을 수행하고, 제자리를 찾은 피벗의 최종 위치(pivot_index)를 받아옵니다.
        pivot_index = partition(lists, left, right)
        
        # 피벗을 제외한 왼쪽 구역 정렬
        quick_sort(lists, left, pivot_index - 1)
        # 피벗을 제외한 오른쪽 구역 정렬
        quick_sort(lists, pivot_index + 1, right)

def partition(lists, left, right):
    pivot = lists[left]
    i = left + 1
    j = right

    while True:
        # i는 피벗보다 큰 값을 찾을 때까지 오른쪽으로 (최대 right까지)
        while i <= right and lists[i] <= pivot:
            i += 1
            
        # [수정된 부분] j는 피벗보다 작은 값을 찾을 때까지 왼쪽으로 (최대 left까지)
        # j > left 조건을 앞에 두어, j가 left 이하로 떨어지면 lists[j]를 아예 검사하지 않도록 차단합니다.
        while j > left and lists[j] >= pivot:
            j -= 1

        # 손가락이 서로 엇갈렸다면 반복문 탈출
        if i >= j:
            break
            
        # 엇갈리지 않았다면 두 원소의 자리를 바꿈
        lists[i], lists[j] = lists[j], lists[i]

    # i와 j가 교차되면 pivot과 j를 바꾼다
    lists[left], lists[j] = lists[j], lists[left]
    
    return j

arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
quick_sort(arr, 0, len(arr) - 1)
print(arr)