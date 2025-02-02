T = int(input())
nums = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(1, T+1):
    cnt = ''
    N = int(input())
    for num in nums:
        cnt += f'{N // num} '
        N %= num
    print(f'#{t}\n{cnt.strip()}')
