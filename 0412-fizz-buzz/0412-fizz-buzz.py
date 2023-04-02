from typing import List, Union

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr: List[Union[int, str]] = []
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                arr.append('FizzBuzz')
            elif (i % 3 == 0):
                arr.append('Fizz')
            elif (i % 5 == 0):
                arr.append('Buzz')
            else:
                arr.append(str(i))
        return arr