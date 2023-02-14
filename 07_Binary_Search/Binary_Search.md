## 이진 탐색 알고리즘
- 순차 탐색(Sequential Search): 리스트 안에 있는 특정한 <b>데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인</b>하는 방법
- 이진 탐색(Binary Search): 정렬되어 있는 리스트에서 <b>탐색 범위를 절반씩 좁혀가며 데이터를 탐색</b>하는 방법
  * 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.

- 이진 탐색 소스코드: 재귀적 구현
```python
def binary_search(array, target, start, end):
	if start > end:
    return None
  mid = (end + start) // 2
  # 찾은 경우 중간값을 반환
  if array[mid] == target:
    return mid
  # 중간값보다 찾고자 하는 값이 작은 경우 왼쪽 탐색
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  # 중간값보다 찾고자 하는 값이 큰 경우 오른쪽 탐색
  else:
    return binary_search(array, target, mid+1, end)
        
# n(데이터의 갯수), target(찾고자 하는 값) 입력
n, target = list(map(int, input().split()))
# 전체 데이터 입력
array = list(map(int, input().split()))
 
# 이진 탐색의 수행결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
  print('데이터가 존재하지 않습니다.')
else:
  print(result+1)
```

- 이진 탐색 소스코드: 반복문
```python
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
```

### 이진 탐색의 시간 복잡도
- 단계마다 탐색 범위를 2로 나눈 것과 동일하므로 <b>연산 횟수는 logN에 비례</b>
- 예를 들어 초기 데이터 갯수가 32개일 때, 이상적으로 1단계를 거치면 16개의 데이터만 남음.
  * 2단계를 거치면 8개가량의 데이터만 남음
  * 3단계를 거치면 4개가량의 데이터만 남음
- 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장

### 파이썬 이진 탐색 라이브러리
- bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
```python
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))
```

- 값이 특정 범위에 속하는 데이터 구하기
```python
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)

  return right_index - left_index

# 배열 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 갯수 출력
print(count_by_range(a,4,4))

# 값이 [-1, 3] 범위 안에 있는 데이터 갯수 출력
print(count_by_range(a,-1,3))
```

### 파라메트릭 서치(Parametric Search)
- <b>파라메트릭 서치</b>란 <ins>최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법</ins>입니다.
  * 예시: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 <b>이진 탐색을 이용하여 해결</b> 가능

** 최적화 문제: 어떤 함수의 값을 가능한 낮추거나 최대한 높이는 문제
