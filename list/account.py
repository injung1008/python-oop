
import random
class Account():

    def __init__(self, name, money):
        self.bankname = 'sc뱅크' #변수인지 상수인지는 대문자로 표시
        self. name = name
        self.money = money
        self.account = random.randint(100, 999)



    def get_account(self):
        return f'은행이름 : {self.bankname}, 예금주 : {self.name}, 계좌번호 : {self.account}, 잔액 :  {self.money}'



    @staticmethod
    def main():
        while True:
            menu = int(input('0번 브레이크, 1번 입력, 2번 출력'))
            if menu == 0:
                break
            elif menu == 1 :
                a = Account(input('예금주'), int(input('조기잔액')))

            elif menu == 2 :
                print({a.get_account()})

            else :
                print('다시 입력해주세요')
                continue


Account.main()

