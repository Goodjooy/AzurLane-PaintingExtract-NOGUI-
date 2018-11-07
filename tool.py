import tools.writer, tools.test, tools.show, tools.compare_news, tools.park, tools.autoload
import time

tool_list = ["展示所有在out文件夹中的图片",
             "把舰娘的名称写入文件",
             "比较新增的文件",
             "测试",
             "添加新的舰娘的中文名",
             "把out文件夹的图片打包",
             "批处理painting文件夹的文件",
             "删除已解压的文件",
             "将所有的舰娘名列出到文件"
             ]
print("请选择需要选择的工具：")

num = 1
for tool in tool_list:
    print("\t%d） %s" % (num, tool))
    num += 1
an = input("你的选择为#_#\b\b")

if an[0] == '1':
    tools.show.show()
elif an[0] == '2':
    tools.writer.writer()
elif an[0] == '3':
    tools.compare_news.compare()
elif an[0] == '4':
    tools.test.test()
elif an[0] == '5':
    tools.writer.new_pic_add()
elif an[0] == '6':
    tools.park.zip_part()
elif an[0] == '7':
    tools.autoload.auto_load()
elif an[0] == '8':
    tools.autoload.compare()
elif an[0] == '9':
    tools.writer.sxe()
else:
    print("选择错误!")

print("完成")
time.sleep(3)
