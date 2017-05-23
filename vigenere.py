def encrypt(message, key):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    j = 0
    for i in message:
        key_length = len(key)
        letter = key[j].lower()
        rot = alphabet.index(letter)
        if i.isupper():
            i = i.lower()
            pos = alphabet.index(i)
            pos_new = (pos + rot) % 26
            encrypted = encrypted + alphabet[pos_new].upper()
            j = (j + 1) % key_length
        elif i in alphabet:
            pos = alphabet.index(i)
            pos_new = (pos + rot) % 26
            encrypted = encrypted + alphabet[pos_new]
            j = (j + 1) % key_length
        elif i == ' ':
            encrypted = encrypted + ' '
        elif i.isdigit() == True:
            encrypted = encrypted + i
        else:
            encrypted = encrypted + i
    return encrypted

def main():
    print(encrypt(input("put word here:\n\t"), str(input("add key here:\n\t"))))
if __name__ == '__main__':
    main()