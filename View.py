from projects_2048.Conterllor import Conterllor


class View():
    max_count = 0

    def __init__(self):
        self.map = [
            [2, 2, 2, 2],
            [4, 4, 4, 4],
            [8, 8, 8, 8],
            [16, 16, 16, 16]
        ]
        self.con = Conterllor()

    def main(self):

        self.con.random_num(self.map)
        self.con.random_num(self.map)
        self.print_map()
        while True:
            if self.con.random_num(self.map) == 0:
                self.con.count = 0
                self.map = [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                ]
            self.select_menu_item()

    def select_menu_item(self):
        select = input('请输入操作“w、a、s、d”')
        if select == 'w':
            self.con.up_move(self.map)
            self.random_print()

        if select == 'a':
            self.con.left_move(self.map)
            self.random_print()

        if select == 's':
            self.con.down_move(self.map)
            self.random_print()

        if select == 'd':
            self.con.right_move(self.map)
            self.random_print()

    def random_print(self):
        self.con.random_num(self.map)
        self.print_map()

    def print_map(self):
        print("----------------")
        print('目前总成绩为：{}'.format(self.con.count))
        if View.max_count < self.con.count:
            View.max_count = self.con.count
        print('最高记录为：{}'.format(View.max_count))
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                print(self.map[r][c], end="   ")
            print()
