"""neetcode"""
class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res


"""walkccc"""
class Codec:
  def encode(self, strs: List[str]) -> str:
    """Encodes a list of strings to a single string."""
    return ''.join(str(len(s)) + '/' + s for s in strs)

  def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings."""
    decoded = []

    i = 0
    while i < len(s):
      slash = s.find('/', i)
      length = int(s[i:slash])
      i = slash + length + 1
      decoded.append(s[slash + 1:i])

    return decoded