#Madeline Berryman-Dages

def encode(password):
    encoding = ''
    for i in password:
        encoding += str((int(i) + 3)%10)
    return encoding

def decode(password):
    decoded_password = ""
    for char in password:
        new_char = (char - 3) % 10 
        decoded_password += str(new_char)
        print decoded_password

if __name__ == '__main__':
    while True:
        print('''Menu
---------
1. Encode
2. Decode
3. Quit''')
        option = input('Please enter an option')
        if option == '1':
            password = int(input('Please enter your password to encode:'))
            encode(password)
            print('Your password has been encoded and stored!')
        if option == '2':
            print(f'The encoded password is {encode(password)}, and the original password is {decode(encode(password))}. ')
        if option == '3':
            break



           
