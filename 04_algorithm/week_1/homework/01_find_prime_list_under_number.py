input = 20


def find_prime_list_under_number(number):
    answer = []
    for index in range(number):
        if index > 1:
            if index % 2 != 0 and index % 3 != 0:
                answer.append(index)
    return answer


result = find_prime_list_under_number(input)
print(result)

# 배열에 1 ~ input 까지 넣기
# input 에서 소수찾기(if : input % 2 == 0 && input % 3 == 0)
# 소수 배열에 넣기