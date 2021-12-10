#!/usr/bin/python3
from password import Password


def example(value1, value2):
    return value1 + value2

if __name__ == "__main__":
    valid_passwords_a = 0
    valid_passwords_b = 0    
    with open("02.in") as f:
        for line in f.readlines():
            passwd = Password(line.strip())
            valida, validb = passwd.IsValid()
            if(valida):
                valid_passwords_a += 1
            if(validb):
                valid_passwords_b += 1

    print("02A valid passwords:", valid_passwords_a)
    print("02B valid passwords:", valid_passwords_b)
