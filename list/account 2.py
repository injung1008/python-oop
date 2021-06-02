import random
class Account():
    def __init__(self, name, money):
        self.BANKNAME = 'SC은행'
        self.name = name
        self.money = money
        self.ACCOUNT = random.randint(100, 999) '-' random.randint(100, 999) '-' random.randint(100000, 999999)


    def get_account():
        return f'은행 : {self.BANKNAME}, 예금주: {self.name}, 잔액 : {self.money}, 계좌번호 : {self.ACCOUNT}'

    @staticmethod
    def main():
        ls = []
        while True:
            menu = int(input('0:EXIT, 1:creat 2:read 3: update 4: delete'))
            if menu == 0:
                break
            elif menu == 1:
                ls.append(Account(input('예금주 입력하시오'), int(input('잔액 입력하시오')))
            elif menu == 2:
                for i in ls:
                print(i.get_account())
            elif menu == 3:
                if edit_name == Account(name,)
                pass
            elif menu == 4:
                del_name = input('삭제할 예금주')
                for i, j in enumerate(ls):
                    if j.name == del_name
                        del ls[i]
            else:
                print('오류')
                continue


Account.main()



