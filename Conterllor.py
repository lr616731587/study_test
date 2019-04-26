import random
import copy
from projects_2048.Location import Location, Direction


class Conterllor:
    def __init__(self):
        self.__list_merge = []
        self.__list_empty_location = []
        self.count = 0
        self.is_change = False

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    def __zero_to_end(self):
        """
        将0元素移到最后
        :param li:
        :return:
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge_2048(self):
        """
        合并元素2：
            [2, 2, 0, 0] --> [4, 0, 0, 0],
            [2, 0, 2, 0] --> [4, 0, 0, 0],
            [2, 2 ,2, 0] --> [4, 2, 0, 0]
        :param li:
        :return:
        """
        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.count += self.__list_merge[i]
                self.__list_merge[i + 1] = 0

        self.__zero_to_end()

    def __left_move(self, map):
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
            self.__merge_2048()
            map[i][:] = self.__list_merge

    def __right_move(self, map):
        """
        向右移动并整合
        :param li:
        :return:
        """
        for i in range(len(map)):
            self.__list_merge[:] = map[i][::-1]  # 2 2 2 4
            self.__merge_2048()
            map[i][::-1] = self.__list_merge[:]

    def __up_move(self, map):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge.append(map[r][c])
            self.__merge_2048()

            for i in range(4):
                map[i][c] = self.__list_merge[i]

    def __down_move(self, map):
        """
        向下移动并合并
        :param li:
        :return:
        """
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):
                self.__list_merge.append(map[r][c])
            self.__merge_2048()

            for i in range(3, -1, -1):
                map[i][c] = self.__list_merge[3 - i]

    def move(self, dir, map):
        original_map = copy.deepcopy(map)
        if dir == Direction.up:
            self.__up_move(map)

        if dir == Direction.down:
            self.__down_move(map)

        if dir == Direction.left:
            self.__left_move(map)

        if dir == Direction.right:
            self.__right_move(map)
        self.is_change = original_map != map

    def random_num(self, map):
        self.__list_empty_location.clear()
        for i in range(4):
            for j in range(4):
                if map[i][j] == 0:
                    loc = Location(i, j)
                    self.__list_empty_location.append(loc)

        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_location.remove(loc)

    def game_is_over(self, map):
        if len(self.__list_empty_location) > 0:
            return False

        for i in range(4):
            for j in range(3):
                if map[i][j] == map[i][j + 1] or map[j][i] == map[j + 1][i]:
                    return False
        return True


