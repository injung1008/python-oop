'''
이름, 출생년도. 주소를 입력받아서 회원가입한 사람의 이름, 만나이 주소를 출력하시오
'''

class Person:
    def __init__(self,name, birth, address):
        self.name = name
        self.birth = birth
        self.address = address

    def age(self):
       return 2021 - self.birth

    @staticmethod
    def main():

        p = Person(input('이름'), int(input('출생년도')), input('주소'))
        print(f' 만나이 : {p.age()}')

Person.main()
