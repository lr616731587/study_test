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
    # #  提取出不为0的元素
    # new_list = [i for i in li if i != 0]
    # #  count 返回元素的数量
    # new_list += [0] * li.count(0)
    # li[:] = new_list[:]

    for item in range(len(li), -1, -1):
        if item == 0:
            del li[item]
            li.append(0)


list = [0, 2, 2, 0]
sort_2048(list)
print(list)
