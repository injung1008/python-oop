


class Bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height


    def div(self):
        return  self.weight / self.height * self.height

    def grade(self):
        grade = ''

        score = (self.weight / self.height * self.height)*10000
        if score > 70:
            grade = '위험'
        elif score >60:
            grade = '중 위험'
        else :
            grade = '정상'

        return grade

    @staticmethod
    def main():
         b = Bmi(int(input('키')), int(input('몸무게')))
         print(f' BMI : {b.grade()}')

Bmi.main()
