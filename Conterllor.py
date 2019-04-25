import random
from projects_2048.Location import Location



class Conterllor:
    def __init__(self):
        # self.__map = map
        self.__list_merge = []
        self.__list_empty_location = []
        self.count = 0
        self.list = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]

    # @property
    # def map(self):
    #     return self.__map

    def zero_to_end(self):
        """
        将0元素移到最后
        :param li:
        :return:
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def merge_2048(self):
        """
        合并元素2：
            [2, 2, 0, 0] --> [4, 0, 0, 0],
            [2, 0, 2, 0] --> [4, 0, 0, 0],
            [2, 2 ,2, 0] --> [4, 2, 0, 0]
        :param li:
        :return:
        """
        self.zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.count += self.__list_merge[i]
                self.__list_merge[i + 1] = 0

        self.zero_to_end()

    def random_num(self, map):
        self.__list_empty_location.clear()
        for i in range(4):
            for j in range(4):
                if map[i][j] == 0:
                    loc = Location(i, j)
                    self.__list_empty_location.append(loc)

        if len(self.__list_empty_location) == 0:
            return 0
        loc = random.choice(self.__list_empty_location)
        map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_location.remove(loc)


    def left_move(self, map):
        """
        向左移动并合并
            [2, 0, 0, 2]，               4 0 0 0
            [2, 2, 0, 0],                4 0 0 0
            [2, 0, 4, 4],                2 8 0 0
            [4, 0, 0, 2]                 4 2 0 0
        :param li:
        :return:
        """
        for i in range(len(map)):
            self.__list_merge[:] = map[i]
            self.merge_2048()
            map[i][:] = self.__list_merge

    def right_move(self, map):
        """
        向右移动并整合
        :param li:
        :return:
        """
        for i in range(len(map)):
            self.__list_merge[:] = map[i][::-1]  # 2 2 2 4
            self.merge_2048()
            map[i][::-1] = self.__list_merge[:]

    def up_move(self, map):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge.append(map[r][c])
            self.merge_2048()

            for i in range(4):
                map[i][c] = self.__list_merge[i]

    def down_move(self, map):
        """
        向下移动并合并
        :param li:
        :return:
        """
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):
                self.__list_merge.append(map[r][c])
            self.merge_2048()

            for i in range(3, -1, -1):
                map[i][c] = self.__list_merge[3 - i]


def print_map(map):
    print("----------------")
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c], end=" ")
        print()


# if __name__ == '__main__':
#     # core = Conterllor()
#     print_map(core.map)
#     # core.up_move()
#     # print_map(core.map)
#     # core.down_move()
#     # print_map(core.map)
#     # core.left_move()
#     # print_map(core.map)
#     # core.right_move()
#     # print_map(core.map)
#     core.random_num()
#     core.random_num()
#     print_map(core.map)