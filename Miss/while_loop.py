
atempts=3
while atempts>0:
    
    pin=input('enter pin:')
    atempts = atempts - 1

    if pin =='0924':
        print('Authentication successful!')
        break
    else:
        print(f'number of tries left {atempts}')
else:
    print('Account got locked!')
