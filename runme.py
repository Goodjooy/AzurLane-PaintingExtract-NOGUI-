import group.main_part
import os
import zipfile

dir_list = ['Texture2D', 'out', 'Mesh', 'dir_add', 'dir_old', 'dir_new', 'UnityStudio']

for per_dir in dir_list:
    try:
        os.makedirs(per_dir)
    except FileExistsError:
        print("%s文件夹已存在" % per_dir)
    else:
        print("创建%s文件夹" % per_dir)

file_name = 'UnityStudio.zip'
IsZip = zipfile.is_zipfile(file_name)
if IsZip:
    print('检查完成，开始解压UnityStudio.zip')
    file = zipfile.ZipFile(file_name, 'r')
    for files in file.namelist():
        file.extract(files, 'UnityStudio')
    print('解压完成\n')

group.main_part.restore_pic()
