#Madeline Berryman-Dages
def store(password):
    return password

def encode(password):
    encoding = [0, 1]
    encoding[0:] = str(password)
    for i in range(0, len(str(password))):
        encoding[i] = (int(encoding[i]) + 3) % 10
    return encoding

def print_encoded_pw(password):
    encode(password)
    encoded_password = ''
    for i in range(0,len(str(password))):
        print(encode(password)[i], end = '')

        # print(entry)

        # return password
    return encoded_password

def decode(password):
    decoded_password = ""
    for char in password:
        new_char = char -3 
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
            print(encode(password))
        if option == '2':
            print(f'The encoded password is {print_encoded_pw(password)}, and the original password is {decode(password)}. ')
        if option == '3':
            break



            #I am changing to commit
