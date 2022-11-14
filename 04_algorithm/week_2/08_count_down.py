def count_down(number):
    if number < 0:         # number 가 0까지만 돌 수 있도록!
        return
    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60) 