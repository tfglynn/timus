N = int(input())
if N >= 1:
    print(N * (N + 1) // 2)
else:
    print(1 - N * (N - 1) // 2)
