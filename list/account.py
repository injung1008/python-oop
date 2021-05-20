

class Account():
    import random
    def __init__(self, name, money, account):
        self. name = name
        self.money = money
        self.account = randint(100, 999)



    def get_account(self):
        return f'예금주 : {self.name}, 계좌번호 : {self.account}'



    @staticmethod
    def main():
        while True:
            menu = int(input('0번 브레이크, 1번 입력, 2번 출력'))

            if menu == 1 :
                a = Account(input('예금주'), int(input('조기잔액')))


            elif menu == 2 :
                print(f'은행이름: SC뱅크 {a.get_account()}')
            elif menu == 0:
                break
            else :
                print('다시 입력해주세요')
                continue


Account.main()

