#String Formatting?

name=input()
school=input()
age=int(input())

print('학교 : {} 이름 : {} 나이 : {}'.format(school,name,age))

name='홍길동'
school='성균관'
age=20

print('학교 : {} 이름 : {} 나이 : {}'.format(school, name, age))

print('학교 : {} 이름 : {} 나이 : {}'.format('성균과','홍길동',20))

#이렇게 format을 이용하면 
#문자열에서 반복적으로  나오거나 직접 입력해야하는 
#정수, 문자 등을 편하게 출력 할 수 있는 것 같다.