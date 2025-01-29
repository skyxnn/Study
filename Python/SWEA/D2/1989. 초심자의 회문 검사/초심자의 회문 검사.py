T = int(input())
for t in range(1, T+1):
    string = input()
    for i in range(len(string)//2):
        if string[i] != string[-i-1]:
            result = 0
            break
        else:
            result = 1
    print(f'#{t} {result}')
