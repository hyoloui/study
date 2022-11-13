# # 튜플 (tuple)
# # 튜플은 리스트와 똑같이 생겼지만, 불변형입니다.

# # 1 - [리스트]
# 카페 = ['스타벅스', '이디야', '더리터']

# 카페[1] = '엔젤리너스'
# print(카페) # ['스타벅스', '엔젤리너스', '더리터']


# # 2 - (튜플) - 삽입, 추가, 삭제 불가
# 카페 = ('스타벅스', '이디야', '더리터')

# 카페[1] = '엔젤리너스' # 이건 안됨
# print(카페) # ['스타벅스', '엔젤리너스', '더리터']

# --------------------------------------------------

# # 집합 (set) - 중복을 제거한다!
# # 1
# 숫자 = [1, 2, 3, 5, 4, 6, 7, 1, 3, 5, 2]

# 숫자_셋 = set(숫자)
# print(숫자_셋) # {1, 2, 3, 4, 5, 6, 7}

# # 2
# a = ['사과', '감', '배', '수박', '딸기']
# b = ['배', '사과', '포도', '참외', '수박']

# a_set = set(a)
# b_set = set(b)

# # 교집합
# print(a_set & b_set) # {'사과', '배', '수박'}
# # 합집합
# print(a_set | b_set) # {'참외', '수박', '감', '사과', '포도', '배', '딸기'}

# --------------------------------------------------
# # quiz

# student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
# student_b = ['물리1','수학1','미술','화학2','체육']

# a_set = set(student_a)
# b_set = set(student_b)
# print(a_set - b_set)


# --------------------------------------------------
# --------------------------------------------------
# # f-string
# # 굉장히 자주 쓰임!!! js `${variable}` 과 같은 기능!

# scores = [
#     {'name': '영수', 'score': 70},
#     {'name': '영희', 'score': 65},
#     {'name': '기찬', 'score': 75},
#     {'name': '희수', 'score': 23},
#     {'name': '서경', 'score': 99},
#     {'name': '미주', 'score': 100},
#     {'name': '병태', 'score': 32}
# ]

# for s in scores:
#     name = s['name']
#     score = s['score']

# print(name +'의 점수는 '+ str(score) +'점 입니다.')
# # print(f'{name}의 점수는 {score}점 입니다.')
# # 위와 아래와 같음, js `${variable}` 과 같은 기능!


# --------------------------------------------------
# --------------------------------------------------
# 예외처리 - 남용하면 무슨 에러가 나는지 모른다.. 그래서 왠만하면 쓰지 않는게 좋음
# try: 실행할 코드
# except: 에러를 대체할 코드

# people = [
#     {'name': 'bob', 'age': 20},
#     {'name': 'carry', 'age': 38},
#     {'name': 'john', 'age': 7},
#     {'name': 'smith', 'age': 17},
#     {'name': 'ben', 'age': 27},
#     {'name': 'bobby'}, # 'age' 삭제
#     {'name': 'red', 'age': 32},
#     {'name': 'queen', 'age': 25}
# ]

# for person in people:
#   try:
#     if person['age'] > 20:
#       print(person['name'])
#   except:
#     print(person['name'],'에러입니다.')


# --------------------------------------------------

# 파일 불러오기 file 에 연습 예제 있음!

# --------------------------------------------------
# # 한줄의 마법
# # if 문

# num = 3

# # 1.
# if num % 2 == 0:
#     result = '짝수'
# else:
#     result = '홀수'

# # 2.
# result = ('짝수' if num % 2 == 0 else '홀수')  # 한줄의 마법

# print(f'{num}은 {result}입니다.')

# for 문

# a_list = [1,3,2,5,1,2]
# b_list = []


# # 1.
# for a in a_list:
#   b_list.append(a * 2)

# # 2.
# b_list = [a*2 for a in a_list]  # 한줄의 마법

# print(b_list)


# --------------------------------------------------
# --------------------------------------------------
# # map, filter, lambda 식
# # map(a, b) : b(list)를 하나씩 돌면서 a(함수)에 넣어라

# people = [
#     {'name': 'bob', 'age': 20},
#     {'name': 'carry', 'age': 38},
#     {'name': 'john', 'age': 7},
#     {'name': 'smith', 'age': 17},
#     {'name': 'ben', 'age': 27},
#     {'name': 'bobby', 'age': 57},
#     {'name': 'red', 'age': 32},
#     {'name': 'queen', 'age': 25}
# ]


# # def check_adult(person):
# #     return '성인' if person['age'] >= 20 else '청소년'


# # result = map(check_adult, people)

# # map + lambda 식
# # result = map(lambda person: ('성인' if person['age'] >= 20 else '청소년'), people)

# # # filter(): true 인자들만 뽑아오기
# result = filter(lambda x: x['age'] > 20, people)

# print(list(result))


# --------------------------------------------------
# --------------------------------------------------
# # 함수 심화
# # 함수에 인수를 넣을 때, 어떤 매개변수에 어떤 값을 넣을지 정해줄 수 있어요. 순서 상관 없음!

# def cal(a, b):
#     return a+2*b


# result = cal(1, 2)
# # result = cal(b=2, a=1) # 지정하면 순서 상관 없음!
# print(result)

# --------------------------------------------------
# # 인수를 미리 지정해놓으면 기본값이 된다! (다만, b에 데이터 안들어 왔을 때)

# def cal2(a, b=2):
#     return a+2*b


# result = cal2(1)
# print(result)

# --------------------------------------------------
# # 입력값의 개수를 지정하지 않고 모두 받는 방법!

# def call_names(*args):
#     for name in args:
#         print(f'{name}야 밥먹어라~')

# call_names('성범', '민수', '유민', '대호')

# --------------------------------------------------
# # 딕셔너리 반환
# # 키워드 인수를 여러 개 받는 방법!

# def get_kwargs(**kwargs):
#     print(kwargs)


# get_kwargs(name='bob')
# get_kwargs(name='john', age='27')


# --------------------------------------------------
# --------------------------------------------------
# # 클래스 -
# class Monster():
#     hp = 100
#     alive = True

#     def damage(self, attack):
#         self.hp = self.hp - attack
#         if self.hp <= 0:
#             self.alive = False

#     def status_check(self):
#         if self.alive:
#             print('살아있다')
#         else:
#             print('죽었다')


# 괴물1 = Monster()
# 괴물2 = Monster()

# 괴물1.damage(120)
# 괴물2.damage(80)

# print(괴물1.hp)
# 괴물1.status_check()

# print(괴물2.hp)
# 괴물2.status_check()

