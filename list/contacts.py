'''이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.'''

class Contacts():
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contacts(self):
        return f' 주소록: {self.name}, {self.phone}, {self.email}, {self.address}'


    @staticmethod
    def main():
        ls  = []
        while True:
            menu = int(input("0 프로그램 종료, 1 입력, 2 출력 3 삭제"))

            if menu == 1:
                ls.append(Contacts(input('이름'), int(input('폰')), input('이메일'),input('주소')))
            elif menu == 2:
                for i in ls:
                    print(f'출력 결과 : {i.get_contacts()}')

            elif menu == 3:
                del_name = input('삭제할 이름 : ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]

            elif menu == 0:
                print(' 프로그램을 종료합니다')
                break

            else:
                print('오류')
                continue





Contacts.main()




