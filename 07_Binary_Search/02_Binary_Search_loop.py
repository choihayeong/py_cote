def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 일치할 경우 중간값 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    
    return None
    
# n, target 입력
n, target = list(map(int, input().split()))
# array 입력
array = list(map(int, input().split()))
 
result = binary_search(array, target, 0, n-1)
if result == None:
    print('데이터가 없습니다')
else:
    print(result + 1)