import zipfile
import os


def zip_part():
    finish = 0
    file_name = input("打包文件名：")
    if file_name == '':
        file_name = '打包'
    file = zipfile.ZipFile('%s.zip' % file_name, 'w', zipfile.ZIP_DEFLATED)

    for dirpath, dirnames, filenames in os.walk('out'):
        file_path = dirpath.replace('%s\\%s' % (os.getcwd(), file_name), '')
        file_path = file_path and file_path + os.sep or ''

        for filename in filenames:
            file.write(os.path.join(dirpath, filename), file_path + filename)
            finish += 1
            scale=100*(int(finish) / int(len(filenames)))
            print('压缩完成%.2f%%' % scale)

    file.close()
