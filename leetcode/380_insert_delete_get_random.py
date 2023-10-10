from random import randint


class RandomizedSet:

    def __init__(self):
        # self.data = set()
        self.data_list = list()
        self.data_dict = dict()

    def insert(self, val: int) -> bool:
        if val in self.data_dict:
            return False
        # self.data.add(val)

        self.data_dict[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.data_dict:
            index = self.data_dict[val]
            last_item = self.data_list[-1]
            self.data_dict[last_item] = index

            self.data_list[index] = last_item
            self.data_dict.pop(val)
            self.data_list.pop()

            return True
        return False

    def getRandom(self) -> int:
        n = randint(0, len(self.data_list) - 1)
        return self.data_list[n]


if __name__ == '__main__':
    r = RandomizedSet()
    # print(r.insert(0))
    # print(r.insert(1))
    # print(r.remove(0))
    # print(r.insert(2))
    # print(r.remove(1))
    # a = 1
    # print(r.insert(2))
    # print(r.getRandom())
    # print(r.remove(1))
    # print(r.insert(2))
    # print(r.getRandom())
    print(r.insert(1))
    print(r.remove(2))
    print(r.insert(2))
    print(r.remove(1))
    print(r.insert(2))
