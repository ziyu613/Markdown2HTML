#!/usr/bin/python
# coding:utf-8
import os
import markdown
import codecs
import sys
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')

input_dir = './input'
ouput_dir = './output'
input_file_type = '.md'
ouput_file_type = '.html'
pa='./output1 \xbb\xb7\xbe\xb3\xcf\xe0\xb9\xd8'

def mkDir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + ' 目录已存在'
        return False


def dotransferFile(full_name, _dir):
    full_input_path = _dir
    try:
        full_output_path = _dir.replace(input_dir,ouput_dir)
    except OSError as e:
         print ("Error: %s - %s." % (e.filename, e.strerror))

    #
    # tmpFlag = False
    # if _dir == input_dir:
    #     print 'This is first level dir'
    # else:
    #     print 'Converting ' + full_name + ' ...'
    #     tmpSubDir = os.path.split(_dir)[1]
    #     if tmpSubDir != '':
    #         tmpFlag = True;
    #
    # file_name = os.path.splitext(full_name)[0]
    #
    # if tmpFlag:
    #     full_input_file_name = input_dir + '/' + tmpSubDir + '/' + full_name
    #     full_ouput_file_name = ouput_dir + '/' + tmpSubDir + '/' + file_name + ouput_file_type
    # else:
    #     full_input_file_name = input_dir + '/' + full_name
    #     full_ouput_file_name = ouput_dir + '/' + file_name + ouput_file_type
    file_name = os.path.splitext(full_name)[0]
    full_input_file_name = full_input_path + '/' + full_name
    full_ouput_file_name = full_output_path + '/' + file_name + ouput_file_type
    with codecs.open(full_input_file_name, 'r') as ifile:
        in_file_content = ifile.read()
        ou_file_content = markdown.markdown(in_file_content)

        with codecs.open(full_ouput_file_name, 'w', 'gbk') as ofile:
            ofile.write(ou_file_content)
    print '\n Md file transfered Done!'


# main function call init
def mainEntry(in_dir):
    for full_input_file_name in os.listdir(in_dir):
        if os.path.splitext(full_input_file_name)[1] == input_file_type:
            dotransferFile(full_input_file_name,in_dir)
        else:
            if os.path.splitext(full_input_file_name)[1] == '':
                print 'Check folders...'
                try:
                    out_dir = in_dir.replace(input_dir,ouput_dir)
                except OSError as e:
                     print ("Error: %s - %s." % (e.filename, e.strerror))

                in_path = in_dir + '/' + os.path.splitext(full_input_file_name)[0]
                out_path = out_dir + '/' + os.path.splitext(full_input_file_name)[0]
                # make new folders if theres more files
                mkDir(out_path)
                # recurce call on file transfer
                mainEntry(in_path)

def checkoutFolder(ouput_dir):
    files = os.listdir(ouput_dir)
    for file_name in files:
        full_file_name = ouput_dir + '/' + file_name
        if os.path.splitext(file_name)[1] == '':
            try:
                shutil.rmtree(full_file_name)
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))
        else:
            os.remove(full_file_name)
print '\n Delete output folder All Done!'

checkoutFolder(ouput_dir)
mainEntry(input_dir)












