# 해쉬
# 해쉬 테이블이란? 데이터의 검색과 저장이 아주 빠르게 진행됨..

#딕셔너리 == 해쉬 테이블 
#같다고 생각 하면 됨, 내부적으로는 배열을 사용
class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        # ket -> self.items[7] = "test"
        return self.items[index]

    def get(self, key):
        return


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!