class  Grade:
    def setGrade(self, english, math, science):
        self.english = english
        self.math = math
        self.science = science

    def sum(self):
        return g.english + g.math + g.science

    def avg(self):
        return g.sum()/ 3



if __name__ == '__main__':
    g = Grade()
    g.setGrade(1,2,3)
    print(g.sum())




