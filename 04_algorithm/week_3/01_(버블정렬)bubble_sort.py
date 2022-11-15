# 버블 정렬
input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)  # n = input의 길이
    for i in range(n - 1):  # 돌면서 길이-1 하며 반복
        for j in range(n - i - 1):  # 돌면서 길이-1에 줄어든 길이 만큼 또 반복(이중 for문)
            if array[j] > array[j + 1]:  # 첫번째 숫자가 두번째 숫자 보다 크면,
                # 둘의 값을 교환 ex)a, b = b, a
                array[j], array[j + 1] = array[j + 1], array[j]
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
