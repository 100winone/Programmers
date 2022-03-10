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
