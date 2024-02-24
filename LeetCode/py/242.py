"""hashing"""
def isAnagram(self, s: str, t: str) -> bool:
    # return Counter(s) == Counter(t)

    counts_s = {}
    counts_t = {}

    ###########################
    # Body:
    # update counts_s, counts_t
    ###########################
    
    return counts_s == counts_t

"""sorting"""
def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
