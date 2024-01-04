import re


def breakPalindrome(palindromeStr):
    # Write your code here
    result = "IMPOSSIBLE"
    s = list(palindromeStr)
    if len(palindromeStr) == palindromeStr.count("a"):
        return result

    elif len(palindromeStr) != palindromeStr.count("a"):
        for i in range(len(palindromeStr)):
            if s[i] != "a":
                s[i] = "a"
                result = "".join(s)
                break
    return result


if __name__ == '__main__':

    palindromeStr = input()

    result = breakPalindrome(palindromeStr)
    print(result)
