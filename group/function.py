import PIL.Image
import group.SUBSAVE
import os


def get_unity_file():
    pass


def all_file(dir_name):
    had = []
    list_keep = os.listdir(dir_name)
    out_list = []
    dir_list = []
    for file in list_keep:
        if not isfile(dir_name + "\\" + file) and not (file in had):
            dir_list.append(file)
        else:
            out_list.append(file)
    for file in dir_list:
        re = all_file(dir_name + "\\" + file)
        had.extend(re)
        out_list.extend(re)

    return out_list


def all_file_path(dir_name):
    had = []
    list_keep = os.listdir(dir_name)
    diction = {}
    dir_list = []
    file_list = []
    for file in list_keep:
        if not isfile(dir_name + "\\" + file) and not (file in had):
            dir_list.append(file)
        else:
            file_list.append(file)
    for file in dir_list:
        re = all_file_path(dir_name + "\\" + file)
        had.extend(re[0])
        file_list.extend(re[0])
        for keys in re[1]:
            diction[keys] = re[1][keys]
    for index in range(len(file_list)):
        if not file_list[index] in had:
            diction[file_list[index]] = dir_name + "\\" + file_list[index]
            file_list[index] = dir_name + "\\" + file_list[index]

    return file_list, diction


def isfile(file):
    try:
        with open(file, 'r')as file:
            pass
    except FileNotFoundError:
        return False
    except PermissionError:
        return False
    else:
        return True


def re_int(num):
    """四舍五入"""
    if group.scale >= 1:
        return num
    else:
        int_num = int(num)
        float_num = num - int_num

        if float_num >= group.scale:
            return int_num + 1
        if float_num < group.scale:
            return int_num


def restore_tool(ship_name, names, mesh_in_path, pic_in_path, choice=2, ):
    """拼图用的函数"""

    # 用于存储相应参数
    blit_place = [None]
    cut_place = [None]
    restore_way = []
    printer = []

    # 文件信息读取，分类
    with open(mesh_in_path["%s-mesh.obj" % ship_name], 'r')as info:
        for msg in info.readlines():

            if msg[0] == "g":
                continue

            elif msg[0] == "v" and msg[1] != 't':
                msg = msg[:-3]
                msg = msg.split(" ")
                msg = msg[1:]
                msg = [int(msg[0]), int(msg[1])]
                blit_place.append(msg)

            elif msg[0] == "v" and msg[1] == "t":
                msg = msg[:-1]
                msg = msg.split(" ")
                msg = msg[1:]
                msg = [float(msg[0]), float(msg[1])]
                cut_place.append(msg)

            elif msg[0] == 'f':
                msg = msg[:-1]
                msg = msg.split(" ")
                msg = [int(msg[1].split('/')[0]),
                       int(msg[2].split('/')[0]),
                       int(msg[3].split('/')[0]),
                       ]
                restore_way.append(msg)

    # 拼图准备
    temp = ([], [])
    for num in blit_place[1:]:
        temp[0].append(num[0])
        temp[1].append(num[1])

    X = (max(temp[0]) - min(temp[0]))
    Y = (max(temp[1]) - min(temp[1]))

    del temp

    # 背景准备

    bg = PIL.Image.new('RGBA', (X, Y), (255, 255, 255, 0))

    # 图片加载
    img = PIL.Image.open(pic_in_path["%s.png" % ship_name], 'r')

    width = img.width
    height = img.height

    # 坐标镜像处理

    for num in range(len(blit_place) - 1):
        blit_place[num + 1][0] = -blit_place[num + 1][0]
        blit_place[num + 1][1] = Y - blit_place[num + 1][1]
        cut_place[num + 1][0] = cut_place[num + 1][0]
        cut_place[num + 1][1] = 1 - cut_place[num + 1][1]
    Pos = [[], []]
    for num in blit_place[1:]:
        Pos[0].append(num[0])
        Pos[1].append(num[1])

    move_x = min(Pos[0])
    move_y = min(Pos[1])

    # 切割模块
    for index in restore_way:
        # 索引，拆分
        blit_p = [blit_place[index[0]], blit_place[index[1]], blit_place[index[2]]]
        cut_p = [cut_place[index[0]], cut_place[index[1]], cut_place[index[2]]]

        blit_area = [min(blit_p[0][0], blit_p[1][0], blit_p[2][0]) - move_x,
                     min(blit_p[0][1], blit_p[1][1], blit_p[2][1]) - move_y]

        cut_x = re_int(min(cut_p[0][0], cut_p[1][0], cut_p[2][0]) * width)
        cut_y = re_int(min((cut_p[0][1], cut_p[1][1], cut_p[2][1])) * height)

        end_x = re_int(
            (max(cut_p[0][0], cut_p[1][0], cut_p[2][0])) * width)
        end_y = re_int(
            (max(cut_p[0][1], cut_p[1][1], cut_p[2][1])) * height)

        cut_size = (cut_x, cut_y, end_x, end_y)

        cut = img.crop(cut_size)

        printer.append([blit_area, cut])

    # 开始拼图
    if choice == 2 or choice == 3:
        group.SUBSAVE.sub_save(printer, ship_name, bg, names)
    if choice == 3 or choice == 1:
        for index in printer:
            bg.paste(index[1], index[0])

        pic = bg

        pic.save("out\\%s.png" % names[ship_name])


def cut_pic(name):
    """a method to read the pic which had been restored,and tell the user"""

    cut_part = []
    save_part = []
    save_scale = []

    bg_size = PIL.Image.open("out\\%d" % name).size

    bg = PIL.Image.new('RGBA', bg_size, (255, 255, 255, 0))

    change_pic = PIL.Image.open('changed\\%s' % name)

    change_size = change_pic.size

    if change_size[0] > bg_size[0] or change_size[1] > bg_size[1]:
        scale = min(bg_size[0] / change_size[0], bg_size[1] / change_size[1])

        change_pic = change_pic.resize(
            (re_int(change_size[0] * scale), re_int(change_size[1] * scale), PIL.Image.ANTIALIAS))

    start_x = re_int((bg_size[0] - change_size[0]) / 2)
    start_y = re_int((bg_size[1] - change_size[1]) / 2)

    bg.paste(change_pic, (start_x, start_y))
