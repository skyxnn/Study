test = int(input())
for t_idx in range(1, test+1):
    num = int(input())
    if num % 2:
        result = num//2 + 1
    else:
        result = -(num//2)
    print(f'#{t_idx} {result}')
