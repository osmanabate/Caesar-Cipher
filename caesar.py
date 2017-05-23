def encrypt(message, rot):
    new_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in message:
        if i.isupper():
            i = i.lower()
            pos = alphabet.index(i)
            pos_new = (pos + rot) % 26
            new_message = new_message + alphabet[pos_new].upper()
        elif i in alphabet:
            pos = alphabet.index(i)
            pos_new = (pos + rot) % 26
            new_message = new_message + alphabet[pos_new]
        elif i == ' ':
            new_message = new_message + ' '
        elif i.isdigit() == True:
            new_message = new_message + i
        else:
            new_message = new_message + i

    return new_message


def main():
    print(encrypt(input("put word here:\n\t"), int(input("add rotation here:\n\t"))))
if __name__ == '__main__':
    main()


