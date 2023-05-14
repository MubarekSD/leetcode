class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        aa = dict()
        bb = dict()
        for i in range(len(s)):
            if s[i] not in aa.keys():
                aa.setdefault(s[i], 1)
            if t[i] not in bb.keys():
                bb.setdefault(t[i], 1)
            aa[s[i]] += 1
            bb[t[i]] += 1
        for i in aa:
            if i not in bb.keys() or aa[i] != bb[i]:
                return False
        return True