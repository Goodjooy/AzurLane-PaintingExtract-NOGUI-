import os
import shutil


def compare():
    dir_old = os.listdir('dir_old')
    dir_new = os.listdir('dir_new')
    dir_add = os.listdir('dir_add')
    for add in dir_add:
        os.remove('dir_add\\%s' % add)

    new_pic = []
    for pic in dir_new:
        if pic not in dir_old:
            shutil.copyfile('dir_new\\%s' % pic, 'dir_add\\%s' % pic)
            shutil.copyfile('dir_new\\%s' % pic, 'dir_old\\%s' % pic)
            new_pic.append(pic)

    with open('new_add.txt', 'w') as file:
        file.write('新增立绘：%d\n' % len(new_pic))
        i = 1
        for pic in new_pic:
            file.write("第%d个，为：%s\n" % (i, pic))
            i += 1

    for new in dir_new:
        os.remove('dir_new\\%s' % new)
