from webscrap.bugsmusic import BugsMusic
bm = BugsMusic()

```
from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic():

    url = ''
    # init이 제거된것이아니라 파라미터가 없는 생성자(bugs = BugsMusic())가 필요하면 생략가능.
    # 표기가 생략되었을뿐 , self.url = url 이것과 같다

    def __str__(self):
        return self.url

   # bugs.url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210524&charthour=15'
    @staticmethod
    def main():
        bugs = BugsMusic()

        while True:
            menu = int(input('0:exit, 1:Input URL, 2:get Ranking '))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('input url')
            elif menu == 2:
                print(f'input url is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                n_artist = 0
                print('---------------artist ranking------------------')
                for link1 in soup.find_all(name = 'p',attrs=({"class":"artist"}) ):
                         # p class="title" adult_yn>0
                    n_artist +=1 # 숫자 랭킹이 1씩 늘어남을 뜻함
                    print(f'{str(n_artist)} ranking') #2 ranking
                    print(f'title: {link1.find("a").text}')
                     #p를 클릭해서 보면 a herf = ~~ 로 되어있어서 이 구조에서 a 를찾는 구문

                print('_______________title ranking__________________')
                n_title = 0
                for link1 in soup.find_all(name = 'p',attrs=({"class":"title"}) ):
                    n_title +=1
                    print(f'{str(n_title)} ranking')
                    print(f'title: {link1.find("a").text}')

            else:
                print('오류')
                continue

BugsMusic.main()

```