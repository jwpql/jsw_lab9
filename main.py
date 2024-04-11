# julia wu

def encode(pw):  # pw is a string
    e = ""  # encoded password
    for n in range(len(pw)):
        digit = 3 + int(pw[n])  # adds 3 to each digit
        e = e + (str(digit))[-1]  # adds digit to the encoded password
    return e
def decode(e):
    encode_string = ''
    for char in e:
         char = int(char) - 3
         encode_string += str(char)
    return encode_string

if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        a = int(input("Please enter an option:"))
        if a == 1:
            password = str(input("Please enter your password to encode:"))
            password = encode(password)  # encodes password
            print("Your password has been encoded and stored!")
        elif a == 2:
            pw = decode(password)
            print(f'The encoded password is: {password}, and the original password is: {pw}')
            print()


        elif a == 3:
            break