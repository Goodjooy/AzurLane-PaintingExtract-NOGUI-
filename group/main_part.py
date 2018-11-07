# -*- coding: UTF-8 -*-
# 这是程序的主要部分，使用时运行该文件
# coding：UTF-8

# 首先，导入需要的库
import json
import time
import os
import sys
import shutil

import group.function


def restore_pic():
    # 开始前的提醒。
    global mesh_in, pic_in, out_in, mesh_in_path, pic_in_path

    # input the ships' chinese name
    with open("files\\names.json", 'r')as file:
        names = json.load(file)
    print("请确保需要还原的文件PNG图片在Texture2D文件夹中。\n请确保需要还原的文件OBJ文件在Mesh文件夹中。")
    time.sleep(1)
    try:

        # find out all file in the Dir
        pic_in = group.function.all_file('Texture2D')
        mesh_in = group.function.all_file('Mesh')
        out_in = group.function.all_file('out')

        # get the path of the file in the dir
        pic_in_path = group.function.all_file_path('Texture2D')[1]
        mesh_in_path = group.function.all_file_path('Mesh')[1]
    except FileNotFoundError:
        print('文件不存在')
        print("需要打开 Unity Studio吗?")
        in_ = input("\t(y\\n)\t")
        if in_ == 'y' or in_ == 'Y':
            place = os.getcwd()
            place += "\\UnityStudio\\UnityStudio.exe"
            os.system(place)

    # if the dir is null ask whether open the unity studio or no
    while (pic_in == [] or mesh_in == [] or (pic_in[0] == 'README.txt' and len(pic_in) == 1) or (
            mesh_in[0] == 'README' and len(mesh_in) == 1)) or pic_in in out_in:

        # when there is nothing in the dir
        if (pic_in == [] or mesh_in == [] or (pic_in[0] == 'README.txt' and len(pic_in) == 1) or (
                mesh_in[0] == 'README' and len(mesh_in) == 1)):
            print("在目标文件夹中没有文件。")

        # when all of ships are restores and seem can't work
        elif pic_in == out_in:
            print("所有图片已经还原了。")
        # ask for open unity studio
        print("需要打开 Unity Studio吗?")
        in_ = input("\t(y\\n)\t")
        if in_ == 'y' or in_ == 'Y':
            # open unity studio
            place = os.getcwd()
            place += "\\UnityStudio\\UnityStudio.exe"

            os.system(place)
            # read all file in dir again ,if they still are null,the loop will continue
            pic_in = group.function.all_file('Texture2D')
            mesh_in = group.function.all_file('Mesh')
        elif in_ == 'n' or in_ == 'N' and (pic_in == [] or mesh_in == []):
            sys.exit()
        elif in_ == 'n' or in_ == 'N' and pic_in == out_in:
            break

    # when the dir have someting the following statement will work
    if not (pic_in == [] or mesh_in == [] or
            (pic_in[0] == 'README.txt' and len(pic_in) == 1) or
            (mesh_in[0] == 'README.txt' and len(mesh_in) == 1)):

        # now is prepare for the work

        # when find ships which have been restored ,and if user order restore them again it will turn True
        restore_again = False

        # when the ship can use RestoreTool to restore ,will turn True
        restore = True

        # the following value is hold the each type of work worked
        restore_num = 0
        restore_again_num = 0
        copy_only = 0
        bad_restore = 0
        pass_num = 0
        num = 0

        # a list hold NoMeshFile
        NoMeshFile = []

        # A list hold ships' chinese name
        pic_cn = []

        # write the names into the list
        for pic in pic_in:
            pic = pic.split('.')[0]
            pic_cn.append('%s.png' % names[pic])
        # get the number of the ships which had restored
        for out_pic in out_in:
            if out_pic in pic_cn:
                num += 1
        print("检查完成！有%d个。\n 其中有%d个图像已经还原了！" % (len(pic_in), num), end='')

        # when has the ships which had restored,show it
        if num != 0:
            print("是否重新操作？")
            in_ = input("(y\\n)\t")
            if in_ == "y" or in_ == "Y":
                restore_again = True

        # ask for choice
        print("还原模式：\n\t1. 只有图片\n\t2. 只有手动微调器\n\t3. 两种都要")
        choice = input('选择# #\b\b')
        try:
            choice = int(choice)
        except ValueError:
            choice = int(choice[0])
        if choice == '' or choice > 3 or choice < 1:
            choice = 1

        # ask before start
        print("还原操作即将开始，是否确认？")
        in_ = input("(y\\n)\t")
        if in_ == 'y' or in_ == 'Y':
            # start
            number = 0

            # cut the ".png"part
            for msg in pic_in:
                restore = True
                msg = msg.split('.')
                msg = msg[0]

                # tact the ship name
                if msg == "UISprite":
                    # a type of usless pic,pass it
                    print("无效的被还原图！\n")
                    restore = False
                    bad_restore += 1
                if msg == "README":

                    # a type of info file ,pass it
                    print("无效的被还文件！\n")
                    restore = False
                else:
                    if names[msg] + ".png" in out_in:

                        # restore pic .
                        print("%s 已还原过！" % names[msg], end='')

                        if restore_again:

                            # restore again
                            print("\t重新还原！")
                            restore = True
                            restore_again_num += 1
                            restore_num -= 1
                        else:

                            # pass
                            print("跳过", end='\n')
                            restore = False
                            pass_num += 1

                    if msg + "-mesh.obj" not in mesh_in and restore:

                        # can't find Mesh file ,it might doesn't need restore,just copy
                        print("%s 找不到还原文件，将把Texture2D中的图片直接拷贝到out文件夹！" % msg)
                        shutil.copyfile("Texture2D\\" + msg + ".png", "out\\" + names[msg] + ".png")

                        # add it into the NOMeshName list
                        NoMeshFile.append(msg)

                        if restore_again:
                            restore_num += 1
                        restore = False
                        copy_only += 1

                    if restore:
                        # if the value of 'restore' is true run the tool
                        group.function.restore_tool(msg, names, mesh_in_path, pic_in_path, choice)
                        restore_num += 1

                    number += 1

                    # show the percent of the finished
                    scale = (100 * (int(number) / int(len(pic_in))))
                    try:
                        print("完成第%d个！,为：%s\n完成%.2f%%\n" % (number, names[msg], scale))
                    except KeyError:
                        print("跳过！完成%.2f%%\n" % scale)

            print("全部完成！")

            # show every type of works work times
            print("其中 ：\n无效还原有%d个\n重新还原有%d个\n已还原并跳过有%d个\n只有拷贝的有%d个\n正常还原%d个\n信息文件%d个"
                  % (bad_restore, restore_again_num, pass_num, copy_only, restore_num, 0))

            # save the NoMeshName into file
            with open('files\\nomeshfile.json', 'w')as file:
                json.dump(NoMeshFile, file)

            # wait 15 second
            time.sleep(15)

        elif in_ == 'n' or in_ == 'N':
            # if choice NO close tool
            sys.exit()
