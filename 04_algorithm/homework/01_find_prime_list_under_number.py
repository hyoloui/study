# prime = 소수
input = 20


def find_prime_list_under_number(number):
    input_array = []
    input_max = 0
    if input > input_max:
      input_array += input_max
      input_max += 1
    return [input_array]


result = find_prime_list_under_number(input)
print(result) 

# 1 소수 나열하기
# 배열에 1 ~ input 까지 넣기
# input 에서 소수찾기(if : input % 2 == 0 && input % 3 == 0) 
# 소수 배열에 넣기