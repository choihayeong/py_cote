## 정렬 알고리즘
- <b>정렬(Sorting)</b>이란 <ins>데이터를 특정한 기준에 따라 순서대로 나열</ins>하는 것
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용

## 선택 정렬(Selection Sort)
- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복합니다.
```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
	min_index = i #가장 작은 원소의 인덱스
  for j in range(i+1, len(array)):
  	if array[min_index] > array[j]:
    	min_index = j
	array[i], array[min_index] = array[min_index], array[i] #swap
    
print(array)
```

### 선택 정렬의 시간 복잡도
- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 합니다.
- 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같습니다.

N + (N - 1) + (N - 2) + ... + 2

- 이는 (N^2 + N - 2) / 2로 표현할 수 있는데, 빅오 표기업에 따라서 O(N^2)이라고 작성

## 삽입 정렬(Insertion Sort)
- 처리되지 않은 데이터를 하나씩 골라 <b>적절한 위치에 삽입</b>합니다.
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작합니다.
```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
	for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
    if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]
    else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
    	break
            
print(array)
```

### 삽입 정렬의 시간 복잡도
- 삽입 정렬의 시간 복잡도는 O(N^2)이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용
- 삽입 정렬은 <ins>현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작</ins>합니다.
  * 최선의 경우 O(N)의 시간 복잡도를 가짐
  * 이미 정렬되어 있는 상태에서 다시 삽입 정렬을 수행 한다면?

## 퀵 정렬
- <ins>기준 데이터를 설정</ins>하고 그 <b>기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법</b>입니다.
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나입니다.
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘입니다.
- 가장 기본적인 퀵 정렬은 <b>첫 번째 데이터를 기준 데이터(Pivot)로 설정</b>합니다.

### 퀵 정렬이 빠른 이유: 직관적인 이해
이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)를 기대할 수 있음
- <b>너비 X 높이</b> = N X logN = NlogN

### 퀵 정렬의 시간 복잡도
- 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가짐
- 최악의 경우 O(N^2)의 시간 복잡도를 가짐.
  * 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행하면?

```python
array = [5,7,9,0,1,6,2,4,8]

def quick_sort(array, start, end):
	if start >= end: # 원소가 1개인 경우 종료
    return
  pivot = start # 피벗은 첫 번째 원소
  left = start + 1
  right = end
  while left <= right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
      # 피벗보다 작은 데이터를 찾을 때까지 반복
      while right > start and array[right] >= array[pivot]:
        right -= 1
      if left > right: # 엇갈릴 경우 작은 데이터와 피벗을 교체
        array[right], array[pivot] = array[pivot], array[right]
      else: 
        array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)
    
quick_sort(array, 0, len(array)-1)
print(array)
```

```python
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
	if len(array) <= 1:
    return array
        
  pivot = array[0]
  tail = array[1:]
    
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
    
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
print(quick_sort(array))
```

## 계수 정렬(Count Sort)
- 특정한 조건이 부합할 때만 사용할 수 있지만 <b>매우 빠르게 동작하는</b> 정렬 알고리즘
  * 계수 정렬은 <b>데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때</b> 사용 가능
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N + K)를 보장

```python
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array) + 1) # 0으로 초기화

for i in range(len(array)):
	count[array[i]] += 1 
    
for i in range(len(count)):
	for j in range(count[i]):
    print(i, end=' ')
```

### 계수 정렬의 복잡도 분석
- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N + K)
- 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있습니다.
  * 데이터가 0과 999,999로 단 2개만 존재하는 경우
- 계수 정렬은 <b>동일한 값을 가지는 데이터가 여러 개 등장할 때</b> 효과적으로 사용 가능
  * 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적