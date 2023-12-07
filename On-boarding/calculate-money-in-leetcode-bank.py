class Solution:
    def totalMoney(self, n: int) -> int:
        weeks=n//7
        week1=28
        weekn=28+7*(weeks-1)
        total_money=weeks*(week1+weekn)//2
        for i in range(n%7):
            total_money+=i+weeks+1
        return total_money