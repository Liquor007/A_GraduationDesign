# 怎么在windows下练习shell
1. 安装git

自己百度“git安装”

2. 创建一个shell script类型的文件

打开cmd.exe（快捷键win+R键）  
进入git bin目录，创建可执行的shell script（后缀为.sh的文件）.  
3. 编辑执行shell脚本

我不喜欢在命令行里对文本进行修改，比较麻烦，所以我一般先生成一个简单的shell script，然后用记事本打开test.sh编辑就行了。
```
#!/bin/bash
echo "Hello World!"
```
OK，用记事本打开输入以上内容。
shell解释：“#!” 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种Shell。

回到cmd.exe，让我们执行一下test.sh。
```
sh .\test.sh
```

