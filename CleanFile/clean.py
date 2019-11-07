import os
import shutil

desktop_path = os.path.join(os.path.expanduser('~'),'Desktop')

name = input("请输入清理文件夹名称")
clean_path = os.path.join(desktop_path,name)

if not os.path.exists(clean_path):
    os.mkdir(clean_path)

name_list = os.listdir(desktop_path)

for file in name_list:
    file_path = os.path.join(desktop_path,file)
    # print("文件："+file_path)
    if not os.path.isfile(file_path):
        # print("文件夹："+file_path)
        continue
    else:
        #获取文件类型
        file_type = os.path.splitext(file)[1]
        # print("文件类型："+file_type)
        file_type = file_type[1:]
        file_type_path = os.path.join(clean_path,file_type)
        if not os.path.exists(file_type_path):
            print("新建文件夹："+file_type_path)
            os.mkdir(file_type_path)
        if file_type != '':
            shutil.move(file_path,file_type_path)


