class Stock():
    def __init__(self,company, code):
        self.company = company
        self.code = code

    def get_stock(self):
        return f' 삼성 = stock ({self.company}, {self.code})'


    @staticmethod
    def main():

        while True:
            code = int(input('0 break, 1 입력 2 전체'))

            if code == 1 :
                s = Stock(input('종목명'), int(input('종목코드')))
            elif code == 2:
                print(s.get_stock())
            elif code == 0 :
                break
            else :
                print('올바른 값 입력해주세요')
                continue


Stock.main()
