input = [3, 5, 6, 1, 2, 4]

#내 풀이
def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = 0
    
    for num in array:
      if max_num < num:
        max_num = num
        
    return max_num

# def find_max_num(array):
#   for num in array:
#     for compare_num in array:
#       if num < compare_num:
#         break
#     else:
#       return num

result = find_max_num(input)
print(result)

# 풀이
# def find_max_num(array):
#     array.sort()
#     return array[-1]