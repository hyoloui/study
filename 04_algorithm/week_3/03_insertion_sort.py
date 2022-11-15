# 삽입 정렬
# 필요할 때만 위치를 변경하여 효율적

input = [4, 6, 2, 9, 1]

# 1. [4  6  2  9  1]
#     <-
# 2. [4  6  2  9  1]
#     <- <-
# 3. [2  4  6  9  1]
#     <- <- <-
# 4. [2  4  6  9  1]
#     <- <- <-
# 5. [1  2  4  6  9]
#     <- <- <- <-
for i in range(1, 5):
    for j in range(i):
        print(i-j)


def insertion_sort(array):
    # 이 부분을 채워보세요!
    for i in range(1, 5):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
