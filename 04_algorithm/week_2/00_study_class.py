class person:
    def __init__(self, param_name) -> None:
        print('i am created', self)
        self.name = param_name

    def talk(self):
        print('안녕하세요 제 이름은', self.name, '입니다.')


person1 = person('유재석')
print(person1)
print(person1.name)
person1.talk()
person2 = person('박명수')
print(person2)
print(person2.name)
person2.talk()
