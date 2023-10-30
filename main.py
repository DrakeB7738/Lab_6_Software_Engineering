
def encode(passcode):
    password = ""
    for i in passcode:
        each_password_digit = (int(i) + 3) % 10
        password += str(each_password_digit)
    return password
def decode(passcode):
    password = ""
    for i in passcode:
        each_password_digit = (int(i) - 3) % 10
        password += str(each_password_digit)
    return password
if __name__ == '__main__':

    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        user_input = input('Please enter an option: ')
        if user_input == "1":
            password_input = input('Please enter your password to encode: ')
            encoded_password = encode(password_input)
            print('Your password has been encoded and stored!')
        if user_input == "2":
            print('The encoded password is', encoded_password,', and the original password is', password_input,'.')

        if user_input == "3":
            break