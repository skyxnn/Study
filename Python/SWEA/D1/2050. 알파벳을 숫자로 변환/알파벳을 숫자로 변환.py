alphabet = list(input())
for a in alphabet:
    if ord(a) < 91:
        print(ord(a) - 64, end = ' ')
    else:
        print(ord(a) - 96, end = ' ')
