class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        aa, bb = dict(), dict()
        for i in range(len(s)):
            aa[s[i]] = 1 + aa.get(s[i], 0)
            bb[t[i]] = 1 + bb.get(t[i], 0)
        for i in aa:
            if i not in bb.keys() or aa[i] != bb[i]:
                return False
        return True