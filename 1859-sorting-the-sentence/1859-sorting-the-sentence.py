class Solution:
    def sortSentence(self, s: str) -> str:
        data = s.split()
        n = len(data)
        for i in range(n):
            for j in range(n - 1):
                if (data[j][-1] > data[j + 1][-1]):
                    data[j], data[j + 1] = data[j + 1], data[j]
        for i in range(n):
            a = data[i]
            data[i] = a[0:-1]
        return " ".join(data)
        
        