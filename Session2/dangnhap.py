account_name = 'mindX'
account_pass = 'mindX123'
running = True
while running:
    username = input('account_name')
    password = input('account_pass')
    if username == account_name:
        if password == account_pass:
            print('welcome')
            running = False #phai dong nay luon cuoi cung cua lenh while
            #hoac dung lenh break de dung lai
            break
            print('aaaa')
    else:
        print('sai roi')
