class Wiki():
    def __init__(self, url) -> str:
        self.url = url
    def __str__(self):
        return self.url


    @staticmethod
    def main():
        w = Wiki

        while True:
            menu = int(input('0: exit, 1 :Input URL, 2: URL 출력'))

            if menu == 0:
                break
            elif menu == 1:
                w = Wiki(input('Input URL'))
            elif menu == 2 :
                print(f'URL : {w}')
            else :
                print('오류')
                continue

Wiki.main()
