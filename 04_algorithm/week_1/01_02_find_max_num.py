input = [3, 5, 6, 1, 2, 4]
max_num = 0

# 풀이
# def find_max_num(array):
#     array.sort()
#     return array[-1]

# 2
def find_max_num(array):
    max_num = array[0]
    for num in array:
      if num > max_num:
        max_num = num
        
    return max_num
  
result = find_max_num(input)
print(result)