import sys
import itertools
from math import ceil


def main():
    s = str(input())
    n = len(s)
    N = []
    ans = []
    for i in range(n):
        N.append(s[i])

    for v in itertools.permutations(N, n):
        if v[0] != "0":
            ans.append(v)

    print(int("".join(sorted(ans)[0])))


def main2():
    s = str(input())
    n = len(s)
    N = []
    ans = []
    for i in range(n):
        N.append(int(s[i]))

    for j in range(n):
        m = min(N)
        if j == 0:
            m = ceil(1)
            ans.append(m)
            N.remove(m)
        else:
            m = min(N)
            ans.append(m)
            N.remove(m)
    print(int("".join(map(str, ans))))


if __name__ == '__main__':
    main2()
