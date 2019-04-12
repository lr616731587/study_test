"""
2048项目
"""

# 2020 --> 2200
# 0220 --> 2200


def sort_2048(li):
    """
    将0元素移到最后
    :param li:
    :return:
    """
    #  提取出不为0的元素
    new_list = [i for i in li if i != 0]
    #  count 返回元素的数量
    new_list += [0] * li.count(0)
    li[:] = new_list

    # for item in range(len(li), -1, -1):
    #     if item == 0:
    #         del li[item]
    #         li.append(0)

def merge_2048(li):
    """
    合并元素2：
        [2, 2, 0, 0] --> [4, 0, 0, 0],
        [2, 0, 2, 0] --> [4, 0, 0, 0],
        [2, 2 ,2, 0] --> [4, 2, 0, 0]
    :param li:
    :return:
    """
    sort_2048(li)

    for i in range(len(li) - 1):
        if li[i] == li[i + 1]:
            li[i] += li[i + 1]
            li[i + 1] = 0

    sort_2048(li)

    #排序
    # for i in range(len(li) - 1):
    #     if li[i] < li[i + 1]:
    #         li[i], li[i + 1] = li[i + 1], li[i]

def pri_list(li):
    """
    控制台输出列表：

    :return:
    """
    for i in range(len(li)):
        for j in range(len(li[i])):
            print(li[i][j], end=' ')
        print()

def left_move(li):
    """
    向左移动并合并
        [2, 0, 0, 2]，               4 0 0 0
        [2, 2, 0, 0],                4 0 0 0
        [2, 0, 4, 4],                2 8 0 0
        [4, 0, 0, 2]                 4 2 0 0
    :param li:
    :return:
    """
    for i in range(len(li)):
        merge_2048(li[i])

def right_move(li):
    """
    向右移动并整合
    :param li:
    :return:
    """
    for i in range(len(li)):
        new_list = li[i][::-1]  # 2 2 2 4
        merge_2048(new_list)
        li[i][::-1] = new_list[:]

def up_move(li):
    # for i in range(len(li)):
    #     for c in range(len(li)): #  c列 0
    #         for r in range(len(li) - 1 ): #  r行 0 1 2 3
    #             if li[r][c] < li[r + 1][c]:
    #                 li[r][c], li[r + 1][c] = li[r + 1][c], li[r][c]

    for c in range(len(li)):
        l = []
        for r in range(len(li)):
            l.append(li[r][c])
        merge_2048(l)

        for i in range(len(l)):
            li[i][c] = l[i]

def down_move(li):
    """
    向下移动并合并
    :param li:
    :return:
    """
    for c in range(len(li)):
        l = []
        for r in range(len(li) - 1, -1, -1):
            l.append(li[r][c])
        merge_2048(l)

        for i in range(len(li) - 1, -1, -1):
            li[i][c] = l[len(li)- i -1]


list01 = [
        [2, 0, 0, 2],
        [2, 2, 0, 0],
        [2, 0, 4, 4],
        [4, 2, 0, 2]
    ]


# right_move(list01)
# pri_list(list01)
# print('-----------')
# left_move(list01)
# pri_list(list01)
# print('-----------')
down_move(list01)
# pri_list(list01)
# print('-----------')
# up_move(list01)
pri_list(list01)
