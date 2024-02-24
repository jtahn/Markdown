"""brute force"""
def isPalindrome(self, s: str) -> bool:
    s = filter(str.isalnum, s)
    s = ''.join(s)
    s = s.lower()
    return s == s[::-1]


"""pointers"""
def isPalindrome(self, s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i].isalnum() and s[j].isalnum():
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        else:
            i += not s[i].isalnum()
            j -= not s[j].isalnum()
    return True
