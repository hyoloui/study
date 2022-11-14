finding_target = 20
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 시간복잡도 : O(N)


def is_existing_target_number_sequential(target, array):
    find_count = 0  # 숫자세기
    for number in array:
        find_count += 1  # for 문 돌면서 숫자세는 변수에 += 1
        if target == number:  # target 과 하나씩 증가하는 number 가 같아지면
            print(find_count)  # 14!
            return True  # True 반환!

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True