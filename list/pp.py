'''이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.'''
class Contact():
    def __init__(self,name, phone, email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contact(self):
        return f'이름 : {self.name}, 전화번호 : {self.phone}, 이메일 : {self.email}, 주소 : {self.address}'

    @staticmethod
    def del_element(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]


    @staticmethod
    def main():
        ls = []
        while True:

            menu = int(input("0: exit, 1: 입력, 2: 출력 3:삭제 4: 수정"))
            if menu == 0 :
                break
            elif menu == 1 :
                c=Contact(input('이름'), int(input('전화번호')), input('이메일'), input('주소'))
                ls.append(c)
            elif menu == 2 :
                for i in ls :
                    print(f' 주소록 : {i.get_contact()}')+52
            elif menu == 3:
                c.del_element(ls, input('삭제할 이름'))

            elif menu == 4:
                name = input('수정할 이름')
                c = Contact(name, input('수정번호'), input('수정 이메일'), input('수정주소'))
                c.del_element(ls, name)
                ls.append(c)
            else:
                print('잘못된 주문입니다')
                continue



Contact.main()
