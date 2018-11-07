import os
import PIL.Image
import PIL.ImageDraw
import json
import shutil

try:
    import clr
    import System
except ModuleNotFoundError:
    pass


def sub_save(print_group, name, bg, names):
    try:
        os.makedirs("out\\" + names[name] + "_sub_pic\\index\\restore_hand")

    except FileExistsError:
        pass

    try:
        os.makedirs("out\\" + names[name] + "_sub_pic\\pic")
    except FileExistsError:
        pass

    i = 0
    pic_num = {}
    pic_area = {}
    bg = bg.copy()

    for index in print_group:
        if i % 2 == 0:
            pass
        else:
            area = index[0]
            pic = index[1]

            pic_size = pic.size

            rect = (area[0], area[1], area[0] + pic_size[0], area[1] + pic_size[1])

            rect_draw(rect, bg)

            file_name = "out\\" + names[name] + "_sub_pic\\pic\\" + str(i) + ".png"
            pic.save(file_name)

            pic_num[str(i)] = "..\\pic\\" + str(i) + ".png"

            pic_area[str(i)] = [area, pic_size]

        i += 1

    with open("out\\" + names[name] + "_sub_pic\\index\\index.json", 'w') as file:
        file.write(json.dumps([pic_num, pic_area, "map.png"]))

    bg.save("out\\" + names[name] + "_sub_pic\\index\\map.png")

    shutil.copyfile("group\\mod.py", "out\\" + names[name] + "_sub_pic\\index\\restorer for " + name + ".py")

    shutil.copyfile("restore_hand\\__init__.py", "out\\" + names[name] + "_sub_pic\\index\\restore_hand\\__init__.py")
    shutil.copyfile("restore_hand\\support.py", "out\\" + names[name] + "_sub_pic\\index\\restore_hand\\support.py")
    shutil.copyfile("restore_hand\\scr_class.py", "out\\" + names[name] + "_sub_pic\\index\\restore_hand\\scr_class.py")
    shutil.copyfile("files\\char.ttf", "out\\" + names[name] + "_sub_pic\\index\\char.ttf")


def rect_draw(rect, bg):
    draw_pic = PIL.ImageDraw.Draw(bg)

    draw_pic.rectangle(rect, outline=(0, 0, 0))
