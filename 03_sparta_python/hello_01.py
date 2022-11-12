# # 변수, 문자열, 리스트, 딕셔너리

# 변수 선언
# 변수이름 = 값
# js와는 다르게 형태로 쓴다!

# 숫자 넣을 수 있어요

# a = 3
# b = 2

# 이후 다른 변수와 사칙연산이 가능해요

# print(a + b) 더하기
# print(a - b) 빼기
# print(a * b) 곱하기
# print(a / b) 나누기
# print(a ** b) 제곱
# % 는 자주 쓰임
# print(a % b) 나눈 나머지(홀수, 짝수, 동등하게 나누어줄 때 등) - 자주쓰임

# a = 3.5 소수도 가능

# # a, b, c 비교
# a = 3
# b = a
# c = b
# a = 5
# b = 4
# print(c)



# --------------------------------------------------
# 숫자형 자료형 - 자료형이란 프로그래밍을 할 때 쓰이는 숫자, 문자열 등 자료 형태로 사용하는 모든 것을 뜻합니다! 파이썬에서 어떤 '값'을 쓰는지 알아야 코딩을 할 수 있겠죠?

# a = 7
# b = 2

# a+b   # 9
# a-b   # 5
# a*b   # 14
# a/b   # 3.5

# a+3*b         # 13 (여러 연산을 한 줄에 할 경우 사칙연산의 순서대로!)
# (a+3)*b       # 20 (소괄호를 이용해서 먼저 계산할 부분을 표시해줄 수 있어요!)


# --------------------------------------------------
# Bool 자료형 - True 와 False / 참과 거짓 (js boolean 타입 : 조건문에 쓰임)


# a = True
# print(a)

# a = (3 > 2)
# print(a) => True

# a = (2 > 3)
#  print(a) => False

# a = (3 == 2)
#  print(a) => False


# 변수는 '값을 가리키는 것'!
# 변수는 메모리에 연결되어 있다


# --------------------------------------------------
# --------------------------------------------------
# 문자열 다루기 - ('')작은따옴표, ("")큰따옴표 : 시작과 끝은 통일!

# #문자 + 문자 = Do it!
# first_name = 'Seunghyo'
# last_name = 'Lee'

# print(first_name, last_name)

# a = '2'
# b = 'hello'

# print(a + b)


# --------------------------------------------------
# # 숫자 + 문자 = Don't

# a = 2
# b = 'hello'

# print(a + b)



# --------------------------------------------------
# # 숫자 + 문자 = Don't

# a = 2
# b = '2'
# print(a + b)

# --------------------------------------------------
# 문자 + 문자 = Do it!
# 문자 : 연산이 되지 않고 텍스트를 합침


# a = '2'
# b = str(2)

# print(a+b)


# --------------------------------------------------
# # # 문자열의 길이(함수) : js Array.length 와 비슷하다
# # # len()

# text = 'abcdefghijklmnopqrstuvwxyz'

# result = len(text)

# print(result)  # 26


# --------------------------------------------------
# # 인덱싱과 슬라이싱 : js Array.length[index]
# # 문자열[n] : 0부터 수를 센다

# result = text[1] # b - 한글자만
# result = text[3:8] # defgh - 3-8 까지
# result = text[3:] # defghijklmnopqrstuvwxyz - 3에서 끝까지
# result = text[:8] # abcdefgh - 시작에서 8까지
# result = text[:] # abcdefghijklmnopqrstuvwxyz - 처음부터 끝까지
# print(result)


# --------------------------------------------------
# # 특정 문자열로 자르기
# # split('')

# myemail = 'abc123@naver.com'

# domain = myemail.split('@')[1].split('.')[0]
# print(domain) # naver

# --------------------------------------------------
# # quiz

# text = 'sparta'

# result = text[:3]
# print(result)


# --------------------------------------------------
# --------------------------------------------------
# # 리스트 : 순서가 있는, 다른 자료형 값을 담는 방법!
# # js 와 다른점 : 다른 타입도 담겨집니다! 신기하게 또 리스트도 들어갈 수 있어요

# a_list = ['신라면', '진라면', '너구리', 1, 2, True, ['사과', '바나나', 3, False]]

# print(len(a_list))  # 7
# print(a_list[6][1])  # 바나나

# --------------------------------------------------
# # .append() == 덧붙이기

# a = [1, 2, 3]
# a.append(5)
# print(a)  # [1, 2, 3, 5]

# # 리스트도 넣을 수 있네요
# a.append([1, 2])
# print(a)  # [1, 2, 3, 5,[1, 2]]

# # a.append(6, 7) don't... 그래서
# a += [6, 7]
# print(a)  # [1, 2, 3, 5, [1, 2], 6, 7]

# --------------------------------------------------
# # 리스트 마지막 출력하기

# a_list = [1, 5, 2, 6, 4, 9]

# result = a_list[-1]  # 9
# print(result)

# --------------------------------------------------
# # 리스트 정렬하기
# a_list.sort()
# print(a_list)  # [1, 2, 4, 5, 6, 9]

# # 리스트 거꾸로
# a_list.sort(reverse=True)
# print(a_list)  # [9, 6, 5, 4, 2, 1]

# # 요소가 리스트 안에 있는지 알아보기
# search = (5 in a_list)
# print(search) # True

# search = (7 in a_list)
# print(search) # False

# --------------------------------------------------
# --------------------------------------------------
# # 딕셔너리 : 딕셔너리는 키(key)와 밸류(value)의 쌍으로 이루어진 자료의 모임입니다. 영한사전에서 영어 단어를 검색하면 한국어 뜻이 나오는 것처럼
# # 딕셔너리 이름 = {"키(key)":"밸류(value)"}

# a_dick = {'name':'hyo', 'age': 26, 'friend':['성범','민수','유민']}

# result = a_dick['name']
# print(result) # hyo

# result = a_dick['age']
# print(result) # 26

# result = a_dick['friend']
# print(result) # ['성범','민수']

# result = a_dick['friend'][1]
# print(result) # 민수

# --------------------------------------------------
# #  값을 업데이트하거나 새로운 값을 넣을 수도 있어요!

# a_dick['height'] = 180
# print(a_dick) # {'name': 'hyo', 'age': 26, 'friend': ['성범', '민수', '유민'], 'height': 180}

# # 요소가 딕셔너리에 있는지 확인
# search2 = ('height' in a_dick)
# search3 = ('weghit' in a_dick)
# print(search2) # True
# print(search3) # False


# --------------------------------------------------
# --------------------------------------------------
# 리스트와 딕셔너리 조합
# 리스트 안에 딕셔너리가 여러개!

# person = [
#   {'name':'jinwoo', 'age':'25'},
#   {'name':'hoohyon', 'age':'29'}
# ]

# 인덱스와 키로 접근할 수 있어요
# print(person[1]) # {'name':'hoohyon', 'age':'29'}
# print(person[1]['age']) # 29


# --------------------------------------------------
# --------------------------------------------------
# quiz
# people = [
#     {'name': 'bob', 'age': 20, 'score': {'math': 90, 'science': 70}},
#     {'name': 'carry', 'age': 38, 'score': {'math': 40, 'science': 72}},
#     {'name': 'smith', 'age': 28, 'score': {'math': 80, 'science': 90}},
#     {'name': 'john', 'age': 34, 'score': {'math': 75, 'science': 100}}
# ]

# # target : 90
# print(people[2]['score']['science']) # 90

