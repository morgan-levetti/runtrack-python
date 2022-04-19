
def flag(N):
    if N % 1 == 0:
        border_j = (N * 3) + 2
        border_i = (N * 3) + 2
        for i in range(border_i):
            for j in range(border_j):
                if i in [0, border_i - 1]:
                    print('-', end=' ')
                else:
                    print(' ', end=' ')
                if j in [0, border_j - 1]:
                    print('|', end=' ')
                else:
                    print(' ', end=' ')
            print()
    else:
        raise AssertionError


flag(2)