README
======

## dev & test 步骤(截图功能只能在windows工作)

* 安装 python 2.7.x
* 下载 https://bootstrap.pypa.io/ez_setup.py 并且在 CMD 窗口执行 python ez_setup.py 来安装 easy_install 
* CMD 中执行 easy_install pillow
* 安装 pywin32

## release 步骤

* 安装 pyinstaller
* build/buildwin32.bat
* [-]字节码压缩和混淆

## TODO

* 添加快捷键
* 执行策略
* 支持命令行运行，运行时直接输出识别到的图片的内容，便于其它类按键程序使用

## 已完成功能

* 宋体14号正常字体和粗体中数字、冒号、减号的识别
* 截图
* 打开 IE 浏览器到指定窗口
* 根据坐标截取关键数据的截图
* 识别截图中的数字
* 自动输入数值到文本框并自动点击出价按钮
* 添加了一个基于 wxPython 实现的夸平台 UI

## 预览

### 主界面

<div style="text-align: center">
    <img src="gui/sceenshot/main.png"/>
</div>

