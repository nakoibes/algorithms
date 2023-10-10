class Set:
    def __init__(self):
        self.data = [[]] * 10

    def add(self, number: int):
        if not self.find(number):  # без этого получится мультимножество
            residue = number % 10
            self.data[residue].append(number)

    def find(self, number: int):
        residue = number % 10
        for item in self.data[residue]:
            if item == number:
                return True
        return False

    def delete(self, number: int):
        residue = number % 10
        size = len(self.data[residue])
        for i in range(size):
            if self.data[residue][i] == number:
                self.data[residue][i] = self.data[residue][size - 1]
                self.data[residue].pop()
                return


if __name__ == '__main__':
    s = Set()
    a = 1
