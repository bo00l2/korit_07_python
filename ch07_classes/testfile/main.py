# 실기 시험 문제 1번 연습 및 작성완료

# for i in range(2):
#     phone_num = input('전화번호를 입력하시오 >>> ')
#
#     if len(phone_num) == 13:
#         print(f'전화번호의 중간 4자리는 {phone_num[4:8]}입니다.')
#     else:
#         print('유효하지 않은 전화번호 형식입니다.')

# 실기 2 번 작성중
# 평균만 구해지면 됨
# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.grade = {}
#
#     def add_grade(self, subject, score):
#         self.grade[subject] = score
#
#     def get_average_grade(self):
#         total = sum(self.grade.values())
#         avg = total / len(self.grade)
#         return avg
#
#
# student0 = Student('김일', 2025001)
# student0.add_grade('국어', 100)
# student0.add_grade('수학', 90)
# student0.add_grade('영어', 80)
#
# print(f'학생 이름 : {student0.name}')
# print(f'평균 성적 : {student0.get_average_grade()} 점')



# 실기 3번 작성완료
num_list = []
# num_plus = 0
# # num_minus = 0
# # num_zero = 0
# #
# # number = int(input('몇 개의 숫자를 입력할까요? >>> '))
# # for i in range(number):
# #     num = int(input(f'{i+1}번째 숫자를 입력하세요 >>> '))
# #     num_list.append(num)
# #     if num % 2 == 0 and num != 0:
# #         num_plus += 1
# #     if num < 0:
# #         num_minus += 1
# #     if num == 0:
# #         num_zero += 1
# #
# # print(f'양수 : {num_plus}개')
# # print(f'음수 : {num_minus}개')
# # print(f'0 : {num_zero}개')



# 실기 4번
# candidates = []
# vote_numbers = 0
# votes = {}
# vote = 0
#
# person = int(input('후보자 수를 입력하시오 >>> '))
#
# for i in range(person):
#     name = input(f'{i+1}번째 후보자의 이름을 입력하시오 >>> ')
#     candidates.append(name)
#     votes[i+1] = 0
#
#
# count = int(input('전체 투표 횟수를 입력하시오 >>> '))
# for i in range(count):
#     vote = int(input(f'{i+1}번째 투표 {votes} >>> '))
#     if vote in votes:
#         votes[vote] += 1
#
# print('--- 투표 결과 ---')
#
# for i in range(person):
#     print(f'{candidates[i]}: {votes[i+1]}표')
