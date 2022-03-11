## 💡Python 코딩테스트 대비 기초 문법정리
> 
>
> **Ref**: 이것이 취업을 위한 코딩테스트다 with 파이썬 
> 
> 

## 자료형
### 자료형 연산
```python
a = 7
b = 3

# 나누기
print(a / b) # 2.333333333333335

# 나머지
print(a % b) # 1

# 몫
print(a // b) # 2

# 거듭제곱
print(a ** b) # 343
```

### 리스트 자료형

```선언 시에 list() 또는 대괄호( "[]" ) 이용가능```

```python
a = [1, 2, 3, 4, 5 ,6 ,7, 8, 9]
print(a) # [1, 2, 3, 4, 5 ,6 ,7, 8, 9]

# 빈 리스트 선언방법 1)
a = list() # []

# 빈 리스트 선언방법 2)
a = [] # []
```

```크기 N인 1차원 리스트 초기화 방법```
```python
n = 10
a = [0] * n
print(a) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

```리스트 인덱싱과 슬라이싱```
```python
a = [1, 2, 3, 4, 5 ,6 ,7, 8, 9]

# 뒤에서 첫 번째 원소 출력
print(a[-1]) # 9

# 4번째 원소 값 변경
a[3] = 7
print(a) # [1, 2, 3, 7, 5 ,6 ,7, 8, 9] 


a = [1, 2, 3, 4, 5 ,6 ,7, 8, 9]
# 두 번째 원소부터 네 번째 원소까지 
print(a[1 : 4]) # [2, 3, 4]
```

```리스트 컴프리헨션```
<br>
> ```('[]') 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트 초기화```

```python
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)] # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
```

```리스트 관련 기타 메서드```
<br>

```python
a = [1, 4, 3]

a.append(2)
print("삽입: ", a) # 삽입: [1, 4, 3, 2]

a.sort()
print("오름차순 정렬: ", a) # 오름차순 정렬: [1, 2, 3, 4]

a.sort(reverse=True)
print("내림차순 정렬: ", a) # 내림차순 정렬: [4, 3, 2, 1]

a.reverse() 
print("원소 뒤집기: ", a) # 원소 뒤집기: [1, 2, 3, 4]

a.insert(2, 3)
print("인덱스 2에 3 추가: ", a) # 인덱스 2에 3 추가: [1, 2, 3, 3, 4]

# 특정 값인 데이터 개수 세기
print(a.count(3)) # 2

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a) # 값이 1인 데이터 삭제: [2, 3, 3, 4]
```

```특정 원소 지우는 리스트 컴프리헨션```
```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result) # [1, 2, 4]
```

### 문자열 자료형
```문자열 연산```

```python
a = "String"
print(a * 3) # StringStringString

a = "ABCDEF"
print(a[2:4]) # CD 
```

### 튜플 자료형
```
- 튜플을 한 번 선언된 값을 변경할 수 없음
- 리스트 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용
```

```python
a = (1, 2, 3, 4)
print(a) # (1, 2, 3, 4) 
```

### 사전 자료형
```key-value 쌍을 데이터로 가지는 자료형```

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data) # {'사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut'}

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
```
```
- keys() -> 키 데이터만 뽑아서 리스트로 이용
- values() -> 값 데이터만을 뽑아서 리스트로 이용
```
```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list) # dict_keys(['사과', '바나나', '코코넛'])
print(value_list) # dict_values(['Apple', 'Banana', 'Coconut'])

for key in key_list:
    print(data[key])
# Apple
# Banana
# Coconut
```

### 집합 자료형
```
- 중복을 허용하지 않음
- 순서가 없음
```

```python
# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5]) 
print(data) # {1, 2, 3, 4, 5}

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data) # {1, 2, 3, 4, 5}
```

```집합 자료형의 연산```
```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a|b) # 합집합 {1, 2, 3, 4, 5, 6, 7}
print(a&b) # 교집합 {3, 4, 5}
print(a-b) # 차집합 {1, 2}
```

```집합 자료형 관련 함수```
```python
data = {1, 2, 3}
print(data) # {1, 2, 3}

# 새로운 원소 추가
data.add(4)
print(data) # {1, 2, 3, 4}

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data) # {1, 2, 3, 4, 5, 6}

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data) # {1, 2, 4, 5, 6}
```

## 함수

```python
def add(a, b):
    return a + b
print(add(3, 7)) # 10

def add(a, b):
    print('함수의 결과:', a + b)

add(b = 3, a = 7)
```

```함수 안에서 함수 밖의 변수 데이터 변경 시 global 키워드 사용```
```python
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a) # 10
```

```람다 표현식```
```python
def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7)) # 10

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7)) # 10
```

## 입출력

```python
# 데이터 개수 입력
n = int(input()) # 5 입력

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split())) # 65 90 75 34 99 , 리스트로 입력
print(data) # [65, 90, 75, 34, 99]

n, m, k = map(int, input().split()) # 3 5 7
print(n, m, k) # 3 5 7
```

```readline() 사용 소스코드 얘시```
```python
import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip() # Hello World
print(data) # Hello World
```

```문자열 출력```
```python
a = 1
b = 2
print(a, b) # 1 2

print(a)
print(b)
# 출력
# 1 
# 2

answer = 7
print("정답은 " + answer + "입니다.") # 에러발생
print("정답은 " + str(answer) + "입니다.") # 정답은 7입니다.
print("정답은", str(answer), "입니다.") # 정답은 7 입니다. (콤마로 출력시 띄어쓰기 들어감)
print(f"정답은 {answer}입니다.") # 정답은 7입니다. #  파이썬 3.6부터 f-string 문법 적용가능 
```


## 주요 라이브러리의 문법과 유의점
### 내장 함수
```python
# eval - 문자열로 들어오는 수식을 계산한 결과를 반환
result = eval("(3 + 5) * 7")
print(result) # 56

result = sorted([('아무개', 50), ('이순신', 75), ('홍길동', 35)], key=lambda x: x[1], reverse=True)
print(result) # [('이순신', 75), ('아무개', 50), ('홍길동', 35)]
```

### itertools
>```반복되는 데이터를 처리하는 기능을 포함하는 라이브러리```

```순열```
```python
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

```조합```
```python
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 모든 순열 구하기
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

```product```
```python
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

```combination_with_replacement```
```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result) # ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]`
```

```headq```
```
- 파이썬의 힙은 최소 힙으로 구성되어 있음
- 단순히 원소를 힙에 넣었다가 빼는 것만으로도 O(NlogN)에 오름차순 정렬이 완료
- 최상단 원소가 가장 작은 원소
```
```python
# 최소 힙
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# 최대 힙
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

```bisect```
```
- bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
- '정렬된 리스트'에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 효과적 
```

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))  # 2
print(bisect_right(a, x)) # 4
```
```collections - deque```
```python
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data) # deque([1, 2, 3, 4, 5])
print(list(data)) # [1, 2, 3, 4, 5] 리스트 자료형으로 변환 
```

```collections - Counter```

>원소별 등장 횟수 세는 기능 제공

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # 3 'blue'가 등장한 횟수 출력
print(counter['green']) # 1 'green'이 등장한 횟수 출력
print(dict(counter)) # {'red': 2, 'blue': 3, 'green': 1} 사전 자료형으로 변환 
```