# # 조건문, 반복문, 함수
# # 조건문

# 라면 = 5000

# if 라면 > 3800:
#   print('국수를 사자')
# elif 라면 > 1900:
#   print('라면을 사자')
# else :
#   print('라면을 두개 살 수 있어 >.<')

# # 파이썬은 들여쓰기가 엄청 중요하다!
# # 들여쓰기에 따라 내용물이 달라진다!

# if : 이게 맞아?
# elif : 그럼 이건?
# elif : 그럼 이건?
# .
# .
# .
# else : 이거라도...


# --------------------------------------------------
# --------------------------------------------------
# # 반복문

# 점심메뉴 = ['신라면', '진라면', '너구리', '짜빠게티', '불닭볶음면']

# for 라면 in 점심메뉴:
#   print(라면)
# # 신라면 진라면 너구리 짜빠게티 불닭볶음면

# --------------------------------------------------

# # 라면예제
# 라면종류 = [
#     {'name': '신라면', 'history': 30},
#     {'name': '진라면', 'history': 26},
#     {'name': '너구리', 'history': 21},
#     {'name': '짜빠게티', 'history': 16},
#     {'name': '불닭볶음면', 'history': 9},
#     {'name': '삼양라면', 'history': 57},
#     {'name': '쇠고기면', 'history': 32},
#     {'name': '스낵면', 'history': 11}
# ]

# # 모든 라면 종류별로 다 보여줘
# for 라면 in 라면종류:
#   name = 라면['name']
#   history = 라면['history']
#   print(name, history)

# # 라면 역사가 20년 이상 된 라면만 보여줘
# for 라면 in 라면종류:
#   name = 라면['name']
#   history = 라면['history']
#   if history > 20:
#     print(name, history)

# --------------------------------------------------

# # i, enumerate(), break - for를 돌면서 리스트에 순서를 붙여줌
# # 라면 역사가 20년 이상 된 라면 4개만 보여줘
# # 데이터가 많은 작업을 할 때 쓰기 좋음! ex) 라면종류 100000개.. 로딩시간 오래걸림

# for i, 라면 in enumerate(라면종류):
#     name = 라면['name']
#     history = 라면['history']
#     print(i, name, history)
#     if i > 2:
#         break


# --------------------------------------------------
# # quiz
# # 짝수 출력하기

# num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
# count = 0

# for num in num_list:
#   if num % 2 == 0:
#     count += 1

# print(count)


# --------------------------------------------------
# # # quiz
# # 리스트에 있는 모든 숫자 더하기

# num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
# sum = 0

# for num in num_list:
#     sum += num

# print(sum)

# # --------------------------------------------------
# # # quiz
# # 리스트에 있는 자연수중 가장 큰 숫자 구하기
# num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

# # 내가 푼 식
# num_list.sort()
# print(num_list[-1])

# # 해설
# max = 0
# for num in num_list:
#     if max < num:
#         max = num
# print(max)


# --------------------------------------------------
# --------------------------------------------------
# # 함수
# def hello():
#   print('안녕!')
#   print('좋은 날씨야')

# hello()
# hello()


# --------------------------------------------------
# # return 을 만나면 해당 "변수는 return 으로 반환" 되어 값이 변환된다!
# def sum(a,b):
#   return a + b

# result = sum(1,2)
# print(result)


# --------------------------------------------------
# # 함수와 조건문

# def bus_rate(age):
#   if age > 65:
#     print('무료입니다')
#   elif age > 20:
#     print('성인입니다')
#   else :
#     print('청소년입니다')

# bus_rate(15) # 청소년입니다.
# bus_rate(33) # 성인입니다.

# --------------------------------------------------
# # 함수와 조건문 2

# def bus_rate(age):
#   if age > 65:
#     return 0
#   elif age > 20:
#     return 1200
#   else :
#     return 750

# my_rate = bus_rate(66)
# print(my_rate) # 0

# my_rate = bus_rate(40)
# print(my_rate) # 1200

# my_rate = bus_rate(3)
# print(my_rate) # 750

# --------------------------------------------------
# # quiz
# def check_gender(pin):
#     if int(pin.split('-')[1][0]) % 2 == 0:
#         print('여성입니다.')
#     else:
#         print('남성입니다.')


# my_pin = '200101-3012345'
# check_gender(my_pin)
# my_pin = '200101-4012345'
# check_gender(my_pin)
# my_pin = '200101-5012345'
# check_gender(my_pin)
# # 조건문, 반복문, 함수
# # 조건문

# 라면 = 5000

# if 라면 > 3800:
#   print('국수를 사자')
# elif 라면 > 1900:
#   print('라면을 사자')
# else :
#   print('라면을 두개 살 수 있어 >.<')

# # 파이썬은 들여쓰기가 엄청 중요하다!
# # 들여쓰기에 따라 내용물이 달라진다!

# if : 이게 맞아?
# elif : 그럼 이건?
# elif : 그럼 이건?
# .
# .
# .
# else : 이거라도...


# --------------------------------------------------
# --------------------------------------------------
# # 반복문

# 점심메뉴 = ['신라면', '진라면', '너구리', '짜빠게티', '불닭볶음면']

# for 라면 in 점심메뉴:
#   print(라면)
# # 신라면 진라면 너구리 짜빠게티 불닭볶음면

# --------------------------------------------------

# # 라면예제
# 라면종류 = [
#     {'name': '신라면', 'history': 30},
#     {'name': '진라면', 'history': 26},
#     {'name': '너구리', 'history': 21},
#     {'name': '짜빠게티', 'history': 16},
#     {'name': '불닭볶음면', 'history': 9},
#     {'name': '삼양라면', 'history': 57},
#     {'name': '쇠고기면', 'history': 32},
#     {'name': '스낵면', 'history': 11}
# ]

# # 모든 라면 종류별로 다 보여줘
# for 라면 in 라면종류:
#   name = 라면['name']
#   history = 라면['history']
#   print(name, history)

# # 라면 역사가 20년 이상 된 라면만 보여줘
# for 라면 in 라면종류:
#   name = 라면['name']
#   history = 라면['history']
#   if history > 20:
#     print(name, history)

# --------------------------------------------------

# # i, enumerate(), break - for를 돌면서 리스트에 순서를 붙여줌
# # 라면 역사가 20년 이상 된 라면 4개만 보여줘
# # 데이터가 많은 작업을 할 때 쓰기 좋음! ex) 라면종류 100000개.. 로딩시간 오래걸림

# for i, 라면 in enumerate(라면종류):
#     name = 라면['name']
#     history = 라면['history']
#     print(i, name, history)
#     if i > 2:
#         break


# --------------------------------------------------
# # quiz
# # 짝수 출력하기

# num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
# count = 0

# for num in num_list:
#     if num % 2 == 0:
#         count += 1

# print(count)


# --------------------------------------------------
# # quiz
# # 리스트에 있는 모든 숫자 더하기

# num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
# sum = 0

# for num in num_list:
#     sum += num

# print(sum)

# # --------------------------------------------------
# # quiz
# # 리스트에 있는 자연수중 가장 큰 숫자 구하기
# num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

# # 내가 푼 식
# num_list.sort()
# print(num_list[-1])

# # 해설
# max = 0
# for num in num_list:
#     if max < num:
#         max = num
# print(max)


# --------------------------------------------------
# --------------------------------------------------
# # 함수
# def hello():
#   print('안녕!')
#   print('좋은 날씨야')

# hello()
# hello()


# --------------------------------------------------
# # return 을 만나면 해당 "변수는 return 으로 반환" 되어 값이 변환된다!
# def sum(a,b):
#   return a + b

# result = sum(1,2)
# print(result)


# --------------------------------------------------
# # 함수와 조건문

# def bus_rate(age):
#   if age > 65:
#     print('무료입니다')
#   elif age > 20:
#     print('성인입니다')
#   else :
#     print('청소년입니다')

# bus_rate(15) # 청소년입니다.
# bus_rate(33) # 성인입니다.

# --------------------------------------------------
# # 함수와 조건문 2

# def bus_rate(age):
#   if age > 65:
#     return 0
#   elif age > 20:
#     return 1200
#   else :
#     return 750

# my_rate = bus_rate(66)
# print(my_rate) # 0

# my_rate = bus_rate(40)
# print(my_rate) # 1200

# my_rate = bus_rate(3)
# print(my_rate) # 750

# --------------------------------------------------
# quiz
def check_gender(pin):
    if int(pin.split('-')[1][0]) % 2 == 0:
        print('여성입니다.')
    else:
        print('남성입니다.')


my_pin = '200101-3012345'
check_gender(my_pin)
my_pin = '200101-4012345'
check_gender(my_pin)
my_pin = '200101-5012345'
check_gender(my_pin)
