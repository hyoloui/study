input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        # 가장 큰 숫자가 들어 왔을 때 만! max_alphabet_index를 저장 한다!
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)


# 들어온 string 을 한글자씩 쪼개기
# 아스키코드로 해당 배열 찾아 +=1
# 배열에서 가장 큰 수 찾기
# 큰수의 배열 넘버로 아스키코드 교환하여 출력
