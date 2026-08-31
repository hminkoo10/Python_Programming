# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a / b)  # 나눗셈
print(a % b)  # 나머지
print(a // b)  # 몫
print(a ** b)  # 제곱

# 복합 대입 연산자
a += 4
print(a)

a -= 2
print(a)

# 증감 연산자 없음
# a++
a += 1

# 비교 연산자
print(3 == 3.0)  # 같음
print(3 != 4)  # 같지 않음
print("apple" < "apble") # True
print(1 < 2 < 3) # 1 < 2 and  2 < 3
print(1 < 3 < 2) # 1 < 3 and 3 < 2

# 논리 연산자 (and, or not)
print(True and False) 
print(True or False)
print(not True)

# Short-circuit 테스트
a = 10
b = 0

# print(a / b) # 0으로 나눌 수 없음

if a > 0 or a / b:
    print("yes")
else:
    print("no")