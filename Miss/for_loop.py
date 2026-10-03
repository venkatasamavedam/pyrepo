num=range(1,11)
for i in num:
    print(i)
print('end')
print('------------------')
for i in range(1,10):
    if i==5:
        break
    print(i)
print('------------------')
for i in range(1,10):
    if i==3:
        continue
    print(i)
print('------------------')

table=int(input('give me the number to write a table:'))
for i in range(1,11):
    print (f'{table}*{i}=',table*i)

print('------------------')
name=input('please enter your name:')
print(f"Name : {name}")
revstr = ""
for i in name:
    revstr = i + revstr
    print(revstr)

print(f"Reverse: {revstr}")
    