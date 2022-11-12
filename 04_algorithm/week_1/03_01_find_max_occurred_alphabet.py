input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    max_occurrence = 0
    max_alphabet = alphabet_array[0]
    
    for alphabet in alphabet_array:
        occurrence = 0
        
        for char in string:
            if char == alphabet_array:
                occurrence += 1
                
            if occurrence > max_occurrence:
                max_occurrence = occurrence
                max_alphabet = alphabet
                
    return max_alphabet  # a


result = find_max_occurred_alphabet(input)
print(result)


# 들어온 string 을 한글자씩 쪼개기
# 아스키코드로 해당 배열 찾아 +=1
# 배열에서 가장 큰 수 찾기
# 큰수의 배열 넘버로 아스키코드 교환하여 출력
