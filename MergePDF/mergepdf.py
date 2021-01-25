#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time    : 2021/1/23 22:58
# @author  : bq
# @email guobinqiang93@gmail.com

import os
import sys
from time import sleep
import time

from PyPDF2 import PdfFileReader, PdfFileWriter


def GetFileName(dir_path):
    file_list = [os.path.join(dirpath, filesname)
                 for dirpath, dirs, files in os.walk(dir_path)
                 for filesname in files]
    return file_list


def MergePDF(dir_path, file_name):
    output = PdfFileWriter()
    outputPages = 0
    file_list = GetFileName(dir_path)
    print('file_list', file_list)
    for pdf_file in file_list:
        if pdf_file.endswith(".pdf"):
            print("文件：%s" % pdf_file.split('\\')[-1], end=' ')
            # 读取PDF文件
            input = PdfFileReader(open(pdf_file, "rb"))
            # 获得源PDF文件中页面总数
            pageCount = input.getNumPages()
            outputPages += pageCount
            print("页数：%d" % pageCount)
            # 分别将page添加到输出output中
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))
    print("\n合并后的总页数:%d" % outputPages)
    # 写入到目标PDF文件
    print("PDF文件正在合并，请稍等......")
    with open(os.path.join(dir_path, file_name), "wb") as outputfile:
        # 注意这里的写法和正常的上下文文件写入是相反的
        output.write(outputfile)
    print("PDF文件合并完成")


# 获取脚本文件的当前路径

def cur_file_dir():
    # 获取脚本路径
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    return path


if __name__ == '__main__':
    # 获取存放pdf文件的文件夹路径
    dir_path = cur_file_dir()
    # 目标文件的名字
    file_name = "merged%s.pdf" % time.strftime('%Y%m%d%H%M%S')
    MergePDF(dir_path, file_name)
