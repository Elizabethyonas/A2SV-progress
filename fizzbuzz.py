class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        FinalList = []

        for i in range (1,n + 1):
            if i % 3 == 0 and i % 5 == 0:
                FinalList.append("FizzBuzz")
            elif i % 3 == 0:
                FinalList.append("Fizz")
            elif i % 5 == 0:
                FinalList.append("Buzz")
            else:
                FinalList.append(str(i))
        return FinalList
