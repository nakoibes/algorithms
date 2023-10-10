from typing import List


class ATM:

    def __init__(self):
        self.banknotes = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}

    def deposit(self, banknotesCount: List[int]) -> None:
        self.banknotes[20] += banknotesCount[0]
        self.banknotes[50] += banknotesCount[1]
        self.banknotes[100] += banknotesCount[2]
        self.banknotes[200] += banknotesCount[3]
        self.banknotes[500] += banknotesCount[4]

    def withdraw(self, amount: int) -> List[int]:
        data = self.banknotes.copy()
        for denomination in sorted(self.banknotes.keys(), reverse=True):
            if amount == 0:
                break
            necessary = amount // denomination
            got = data[denomination]
            if got < necessary:
                data[denomination] = 0
                amount = amount - got * denomination
            else:
                data[denomination] = got - necessary
                amount %= denomination

        if amount == 0:
            ans = [self.banknotes[20] - data[20], self.banknotes[50] - data[50], self.banknotes[100] - data[100],
                   self.banknotes[200] - data[200], self.banknotes[500] - data[500]]
            self.banknotes = data
            return ans
        else:
            return [-1]


if __name__ == '__main__':
    atm = ATM()
    atm.deposit([0, 0, 1, 2, 1])
    print(atm.withdraw(600))
    atm.deposit([0, 1, 0, 1, 1])
    print(atm.withdraw(600))
    print(atm.withdraw(550))
