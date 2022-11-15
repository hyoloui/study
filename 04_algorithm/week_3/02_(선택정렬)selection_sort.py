input = [4, 6, 2, 9, 1]
# 선택 정렬
# 리스트를 하나씩 비교해 가면서 최솟값을 앞으로 빼내기
# 1. [4 6 2 9 1]
#      - - - -
# 2. [1 6 2 9 4]
#        - - -
# 3. [1 2 6 9 4]
#          - -
# 4. [1 2 4 6 9]
#            -
# 5. [1 2 4 6 9]


def selection_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)

    for i in range(n - 1):     # i = 0
        min_index = i          # 최솟값 변수 = i
        for j in range(n - i):  # i = 2
            if array[i + j] < array[min_index]:   # 현재 시도하는 인덱스 보다 최솟값이 크다면,
                min_index = i + j  # 최솟값에 i + j 를 대입
        array[i], array[min_index] = array[min_index], array[i]       # i와 최솟값 교환

    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
