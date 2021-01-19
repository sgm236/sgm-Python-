#이번에는 변수에 문자열을 넣어보자
a = 'Hello_Python' #꼭 ''를 써주도록 하자
print(a)

#변수에 넣은 문자열의 길이를 length함수를 이용해서 구해보자
print(len(a))

#파이썬은 문자열을 입력받을때 index로 입력을 받게되는데 
#이를 이용해서 내가 입력한 문자열중 원하는 문자만 출력하거나 문자들을 출력할 수 있다.

print(a[11]) #결과 e => 여기서 1을 하면 H가 나와야되는거 아닌가? 하는 궁금증이 생긴다

#e가 나오는 이유는 문자열이 index에서 0부터 저장되기 때문이다.

#그러면 H | e | l | l | o | _ | P | y | t | h | o | n | 
#ㄱㄱㄱ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 
#Hello Python이 index에 이렇게 저장이 되기때문에 e가 나오게 되는 것이다.

#출력하고싶은 부분만 출력을 해보자!

print(a[3:6]) #결과 => lo_ 

#이렇게 index를 원하는거 하나만 또는 원하는 부분을 출력할 수 있다.

#repeat?
print(a*2) # => Hello_PythonHello_Python
print((a+'\n')*2) 
#=> Hello Python
#   Hello Python
# 이런식으로 repeat를 이용할 수 있다.    
