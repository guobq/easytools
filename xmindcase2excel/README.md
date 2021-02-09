# xmindcase2excel
一个用于xmind用例转换excel格式的小工具

build:

```shell
pyinstaller -F xmindcase2xlsUI.py  -p xmindcase2xls.py  打包exe
pyinstaller -F -w xmindcase2xlsUI.py  -p xmindcase2xls.py 不带控制台的打包
pyinstaller -F -w -i xmind2xls.ico xmindcase2xlsUI.py  -p xmindcase2xls.py 打包指定exe图标打包
```

windows .exe Release:链接：https://pan.baidu.com/s/1kExAHmokHqig9DEdU9vKJQ提取码：easy 

xmind用例模板:https://github.com/guobq/easytools/blob/main/xmindcase2excel/dist/test.xmind

use:根据用例模板编写xmind用例,双击xmindcase2xlsUI可图形化操作如下

![](https://raw.githubusercontent.com/guobq/mysource/master/PictureBed/xindcase2excel_example.gif)



