
# 效率最高，还可以使用正则进行判断
import os
import glob
def all_files(pattern, search_path, pathsep=os.pathsep):
    # 此处使用绝对路径才能查询工作空间的存放盘符其他文件，此处应将search_path返回最高级盘符
    # 因为os.getcwd()拿取的是工作空间的路径
    for path in search_path.split(pathsep):
        for match in glob.glob(os.path.join(path, pattern)):
            yield match

aaa = all_files('*.py', r"e:")
for match in aaa:
    print(match)


# import os
#
# os.getcwd()  # 获取当前工作目录，即当前工作路径
# os.chdir(path)  # 切换路径(切换到path路径下)
# os.path.isdir(path)  # 判断路径是否存在(判断path是否存在)
# os.listdir()  # 列表形式列出指定目录下的所有文件以及其子文件
# os.curdir()  # 返回当前目录  (为'.')
# os.sep  # 这个就是分隔符，为你使用该系统的分隔符 (windows '\';linux '/')
# os.pardir  # 获取当前目录的父目录名称，字符串('..')

'''
	author:daihui
'''
import os


# def finddir(startdir, target):
#     # try:
#     #     os.chdir(startdir)  # 切换目录
#     # except:
#     #     return
#     for new_dir in os.listdir(startdir):  # 列表出该目录下的所有文件(返回当前目录'.')
#         print(new_dir)
#         if new_dir == target:
#             print("当当当 找到啦！！！！！！！！！")
#             print(os.getcwd() + os.sep + new_dir)
#             exit()
#         if os.path.isdir(new_dir):  # 判断路径是否存在
#             finddir(new_dir, target)
#             os.chdir(os.pardir)  # 切换到当前目录的父目录
#
#
# lis = ['e:',"d:"]  # 工作空间的盘符使用ch.getdir()不起作用
# target = r'test.py'
# for i in lis:
#     startdir = i
#     finddir(startdir, target)