import os
from projects_2048.Conterllor import Conterllor
from projects_2048.Location import Direction


class View():
    max_count = 0

    def __init__(self):
        self.map = [
            [4, 16, 4, 2],
            [2, 16, 8, 4],
            [32, 128, 16, 8],
            [64, 2, 32, 16]
        ]
        self.con = Conterllor()
        self.list = []

    def main(self):
        self.con.random_num(self.map)
        self.__print_generate_new_number()
        while True:
            self.__select_menu_item()
            if self.con.is_change:
                self.__print_generate_new_number()
            else:
                self.__print_map()

            if self.con.game_is_over(self.map):
                self.con.count = 0
                self.map = [
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                    ]
                self.con.random_num(self.map)
                self.__print_generate_new_number()

    def __select_menu_item(self):
        select = input('请输入操作“w、a、s、d”')
        if select == 'w':
            self.con.move(Direction().up, self.map)

        if select == 'a':
            self.con.move(Direction().left, self.map)

        if select == 's':
            self.con.move(Direction().down, self.map)

        if select == 'd':
            self.con.move(Direction().right, self.map)

    def __print_generate_new_number(self):
        self.con.random_num(self.map)
        self.__print_map()

    def __print_map(self):
        print("----------------")
        os.system('clear')
        print('目前总成绩为：{}'.format(self.con.count))
        if View.max_count < self.con.count:
            View.max_count = self.con.count
        print('最高记录为：{}'.format(View.max_count))
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                print(self.map[r][c], end='\t')
            print()
