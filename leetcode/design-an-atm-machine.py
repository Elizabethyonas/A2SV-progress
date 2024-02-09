class ATM:
    def __init__(self):
        self.banknotes = [0, 0, 0, 0, 0]  # $20, $50, $100, $200, $500

    def deposit(self, banknotesCount):
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount):
        withdrawCount = [0, 0, 0, 0, 0]  # $20, $50, $100, $200, $500
        remainingAmount = amount

        for i in range(4, -1, -1):
            banknotesToWithdraw = min(remainingAmount // [20, 50, 100, 200, 500][i], self.banknotes[i])
            withdrawCount[i] = banknotesToWithdraw
            remainingAmount -= banknotesToWithdraw * [20, 50, 100, 200, 500][i]

        if remainingAmount == 0:
            for i in range(5):
                self.banknotes[i] -= withdrawCount[i]
            return withdrawCount
        else:
            return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)