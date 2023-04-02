class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ret = []
        ret.append(celsius + 273.15)
        ret.append(celsius * 1.80 + 32.00)
        return ret