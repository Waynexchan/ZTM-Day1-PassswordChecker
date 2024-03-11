user_id = input('Please enter the user name: ')
user_password = input('Please enter the password: ')
passwordlen = len(user_password)
privacypw = ("*" * passwordlen)

print(f'{user_id}, your password {privacypw} is {passwordlen} letters long')