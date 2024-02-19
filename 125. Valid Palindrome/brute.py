def isPalindrome(self, s: str) -> bool:
    s = filter(str.isalnum, s)
    s = ''.join(s)
    s = s.lower()
    return s == s[::-1]
