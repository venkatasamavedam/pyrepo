input_value=True
print(type(input_value))

input_value="True"
print(type(input_value))

input_value='false'
print(type(input_value))

print('                  ')

x=int(input('enter x value: '))
y=int(input('enter y value: '))

result=(x>y)
print(f'the result is :{result}')

result=(x<y)
print(f'the result is :{result}')

result=(x>=y)
print(f'the result is :{result}')

result=(x<=y)
print(f'the result is :{result}')

result=(x==y)
print(f'the result is :{result}')

result=(x!=y)
print(f'the result is :{result}')

print('                  ')

username='vandana'
passcode='092426'
name=input('Please enter the username:')
num=int(input('Please enter the passcode:'))
result=(username==name and passcode == num)
print(f'result for and is: {result}')
result=(username==name or passcode == num)
print(f'result for or is: {result}')
result=not (username==name)
print(f'result for not is:{result}')
