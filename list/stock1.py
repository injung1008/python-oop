class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_string(self):
        return f'종목명 : {self.name}, 종목 코드 : {self.code}'

    @staticmethod
    def del_elemant(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]



    @staticmethod
    def main():
        ls = []
        while True:
            menu = int(input('0: exit, 1: creat, 2:read 3: update 4: delete'))
            if menu == 0:
                break
            elif menu == 1:
                ls.append(Stock(input('name'), input('code')))
            elif menu == 2:
                for i in ls:
                    print(i.to_string())
            elif menu == 3:
                name = input('수정하고싶은 종목코드 : ')
                s=Stock(name ,input('수정할 종목코드'))
                s.del_elemant(ls, name)
                ls.append(s)

            elif menu == 4:
                s= Stock(None, input('삭제할 종목코드 : '))
                s.del_elemant(ls, s.name)

            else :
                print('오류생성')
                continue



Stock.main()
