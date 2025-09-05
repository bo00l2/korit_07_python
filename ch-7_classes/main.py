'''
클래스 정의 형식 :

class 클래스명(파스칼 케이스로):
    본문

객체 생성 형식 :
객체이름 = 클래스명()           # new 아님!
'''
# 클래스 정의 형식 예시
class WaffleMachine:
    pass

# 객체 생성 예시
waffle = WaffleMachine()
print(waffle) # 결과값 : <__main__.WaffleMachine object at 0x000001DA3AF152B0>

'''
클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지닌다.(Java 때 방이 가져야 할 구성 요소는 무엇이었냐고 질문함)
    객체를 생성하기 위해서는 객체가 가져야 할 '값'과 '기능'을 지녀야 한다.

    값 = 속성(attribute)
    기능 = 메서드(method)

    클래스를 구성하는 속성은 두 가지로 구분된다.
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수 (Java에서는 얘를 static 변수라고 했다.)
        2) 인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
        
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드
        이다. Java에서 정적 메서드라고 하던게 클래스 메서드에 해당되고, 정적 메서드는 또 따로 있다고 볼수도 있고 Java의 정적 메서드가 파이썬의 클래스메서드 + 정적메서드라고 볼 수도 있다.
        
        그리고 Java에서 this 썼는데(아직 생성되지 않은 객체명을 도입할 수 없으니 사용하는 키워드), python 에서는 self 쓴다
        
        self 키워드
        인스턴스 변수에서 각각의 객체를 의미하기 위해서 self 키워드를 붙여준다.
        인스턴스 메서드에서의 첫 번째 매개변수로 '항상' self를 추가해야 한다. 
'''
# 클래스 정의
class Person:
    # 메서드 정의(함수가 클래스 내에 있으니까)
    def set_info(self, name, age, tel, address):    # call2() / setter
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):                            # call1()
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'연락처 : {self.tel}')
        print(f'주소 : {self.address}')

    def display_info2(self):
        return f'제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}인데, {self.address}에 살고 있습니다.'

# 객체 생성
person01 = Person()
# Person 클래스의 메서드 호출
person01.set_info('김일', 20, '010-1234-5678', '서울특별시 마포구')
person01.show_info()
print()
'''
person02 객체 생성, person02.set_info를 활용하여 이름 나이 연락처 주소 입력
display_info2() (call3() 유형으로 작성)
실행 예
제 이름은 -이고, -살입니다.
연락처는 -인데, -에 살고 있습니다.
'''

person02 = Person()
person02.set_info('김보영', '22', '010-1234-5678', '부산광역시 개금동')
print(person02.display_info2())

