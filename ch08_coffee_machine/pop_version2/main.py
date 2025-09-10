MENU = {
    '에스프레소': {
        '재료': {
            '물': 50,
            '커피': 18,
        },
        '가격': 1.5,
    },
    '라떼': {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격': 1.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격': 3.0,
    },
}

profit = 0
resources = {
    '물': 300,
    '우유': 200,
    '커피': 100,
}

logo = '''
 ____  ____  _____ _____ _____ _____
/   _\/  _ \/    //    //  __//  __/
|  /  | / \||  __\|  __\|  \  |  \
|  \__| \_/|| |   | |   |  /_ |  /_
\____/\____/\_/   \_/   \____\\____\''''

# 함수 정의 영역
def is_resources_enough(
        order_ingredient):  # 만약에 특정 함수 / 메서드의 결과값이 boolean이라면 대개 다음 조건문/반복문의 조건식으로 쓰이는 경우가 많다. 함수형 프로그래밍 개념을 떠올리면 된다.
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f'죄송합니다. {item}이(가) 부족합니다.')
            return False
    return True


def process_coins():
    """동전들을 입력 받아 전체 금액을 반환하는 함수 call3 유형"""
    # 쿼터, 다임, 니켈, 페니 네 종류의 동점
    '''
    쿼터 = 0.25 달러        # quarter
    다임 = 0.1 달러         # dime
    니켈 = 0.05 달러        # nickel
    페니 = 0.01 달러        # penny
    '''
    sum = 0
    # 그리고 다수의 수강생들이 빡세게 collections르 사용하는 바람에 내붕레 조건문이 있거나 반복문이 있는 경우도 있다.
    sum += float(input('쿼터 동전을 입력하세요 >>> ')) * 0.25
    sum += float(input('다임 동전을 입력하세요 >>> ')) * 0.1
    sum += float(input('니켈 동전을 입력하세요 >>> ')) * 0.05
    sum += float(input('페니 동전을 입력하세요 >>> ')) * 0.01
    return sum


# todo - 6 : 우리가 왜 동전 처리 함수를 정의했는지 이해해야 한다. 해당 총합을 가지고, 총합이 '선택한' 음료 가격보다 높다면 다음 과정을 넘어갈 필요가 있다.
def is_transaction_successful(money_received, drink_cost):

    change = money_received - drink_cost
    if change >= 0:
        global profit
        profit += drink_cost
        print(f'잔돈 ${change}을(를) 반환합니다.')
        return True
    else:
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다.')
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f'{choice}☕이(가) 나왔습니다. 맛있게 드세요 !! ')


# 관련 변수 선언 및 초기화
is_on = True
while is_on:
    print(logo)
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ')

    if choice == 'off':
        print('자판기가 종료되었습니다. ')
    elif choice == 'report':
        print(f'물 : {resources['물']}ml')
        print(f'우유 : {resources['우유']}ml')
        print(f'커피 : {resources['커피']}g')
        print(f'돈 : ${profit}')

    elif choice in ('에스프레소', '라떼', '카푸치노'):
        drink = MENU[choice]
        if is_resources_enough(drink['재료']):
            money_received = process_coins()
            # 여기의 money_received는 전역 변수이다. 그리고 process_coins()의 결과값을 변수에 담았다.
            if is_transaction_successful(money_received=money_received, drink_cost=drink['가격']):
                # print(f'{choice}☕이(가) 나왔습니다. 맛있게 드세요 !! ')
                make_coffee(drink_name=choice, order_ingredient=drink['재료'])


    # todo - 5 : choice가 이상의 조건을 충족하지 않을 때 '잘못 입력하셨습니다. 다시 입력하세요'를 출력하는 부분
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요')