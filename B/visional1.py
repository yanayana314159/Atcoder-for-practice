import sys


def main():

    li = list(map(str, input().split()))
    n = len(li)
    num = int(li[-1])
    ans = []
    for i in range(n-1):
        s = li[i]
        target = ':'
        idx = s.find(target)
        r = int(s[:idx])
        if num % r == 0:
            ans.append(s[idx:])

    if len(ans) == 0:
        ans = num
    else:
        ans = "".join(ans).replace(":", "")
    print(ans)


if __name__ == '__main__':
    main()
