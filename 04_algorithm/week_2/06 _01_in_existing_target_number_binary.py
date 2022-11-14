finding_target = 16
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0 # 최솟값
    current_max = len(array) - 1 # 최댓값
    current_guess = (current_min + current_max) // 2 # 시돗값
    find_count = 0 # 카운트

    while current_min <= current_max: # 최솟값 <= 최댓값
        if array[current_guess] == target: # 시돗값 == 타겟
            return True
        elif array[current_guess] < target: # 시돗값 < 타겟
            current_min = current_guess + 1 # 최솟값 = 시돗값 + 1
        else:
            current_max = current_guess - 1 # 최댓값 = 시돗값 - 1
            
        current_guess = (current_min + current_max) // 2 # 시돗값 반절로 줄이기

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
