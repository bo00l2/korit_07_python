'''
외부 패키지의 설치 # 1 : settings를 통한 방법
좌측 상단 메뉴버튼 -> file -> settings
좌측 리스트에서 project: 프로젝트명 으로 되어있는 부분 클릭
-> python interpreter 클릭
-> 좌상단에 + 버튼 눌러서 필요한 패키지 검색 및 설치

외부 패키지의 설치 # 2 : 터미널을 이용하는 방법
pip install prettytable
'''
from prettytable import PrettyTable

from ch10_prettytable.pokemon_data import pokemon_data

# PrettyTable의 객체 생성
table = PrettyTable()

table.field_names = ['번호', '이름', '타입']

# for pokemon in pokemon_data:
#     table.add_row(pokemon)

table.add_rows(pokemon_data)
print(table)

#ch11_exception -> main