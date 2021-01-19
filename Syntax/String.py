#간단한 문자열을 출력해보자!
print("Hello")
print('Hello')

# '',"" 도 출력해주고 싶을땐
print("Hello'Python'")
print('Hello"Python"')

#'',""를 동시에 출력할려면?
print("Hello'o' \"w\"orld") 
#Escape를 이용해서 동시에 출력을 해줄 수 있다.(\n, \t, \\, \', \" ...)

# Hello
# Python
# 이렇게 출력하려면 어떻게 해야할까?
print('Hello')
print('Python')
# 이렇게 하는 방법도 있지만 Escape중에서 \n이라는 것을 사용해보자
print('Hello\nPython')
# 이처럼 \n을 사용하여 간단하게 두 줄로 출력할 수 있다.

#이번에는 Docstring이라는것을 사용해보자
print('''Hello 
Python''')
#이처럼 \n을 쓰지않고 줄을 바꿔줄 수 있다.



