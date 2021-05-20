class Grade():
    def __init__(self,samsung, apple, lg):
        self.samsung = samsung
        self.apple = apple
        self.lg = lg

    def avg(self):
        return(self.samsung + self.apple + self.lg)/ 3

    def get_grade(self):
        grade :''
        score = (self.samsung + self.apple + self.lg) / 3
        if score > 90:
            grade = ' 합격'
        elif score > 80:
            grade = ' 재검사'
        else :
            grade = '불합격'

    @staticmethod
    def main():
        g = Grade(int(input('삼성점수')),int(input('애플점수')),int(input('엘지점수')))
            print(f'삼성의 합격 여부 : {g.get_grade()}')


Grade.main()