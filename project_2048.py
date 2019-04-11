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
    li[:] = new_list[:]

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

def sort_merge(list):
    """
    向左移动并合并
        [2, 0, 0, 2]，               4 0 0 0
        [2, 2, 0, 0],                4 0 0 0
        [2, 0, 4, 4],                2 8 0 0
        [4, 0, 0, 2]                 4 2 0 0
    :param list:
    :return:
    """
    for i in range(len(list)):
        #左移
        # merge_2048(list[i])

        #右移
        new_list = list[i][::-1]
        merge_2048(new_list)
        list[i][::-1] = new_list[:]

    pri_list(list)


list01 = [
        [2, 0, 0, 2],
        [2, 2, 0, 0],
        [2, 0, 4, 4],
        [4, 0, 0, 2]
    ]


sort_merge(list01)
