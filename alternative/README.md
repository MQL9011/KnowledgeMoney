# 冲顶大会 自助截屏搜索工具
这是一个**不可靠**的方案，仅供参考。录播推流有延迟，而答题截止时间戳固定，导致每个问题实际只有 4 到 5 秒的回答时间，而本程序每次执行都要花费4秒以上。

正确的方法是从接口处取得题目(抓包能很轻松看到题目的Restful-Api接口，至于能不能看到答案之类的，有待进一步抓包和解软件安装包分析)，使用诸如bosonnlp一类的平台进行实体、情感、关联度的分析再加以搜索整理。

> 真题ID-731：以下音乐家里，去世时最年轻的是：(1)肖邦(2)莫扎特(3)舒伯特。

实际是问，以上三个人谁的寿命最短，分别搜索三位音乐巨匠的寿命，时间早就过去。


## 本地环境配置
Python3.5或更高（Python2.7请自测）

pytesseract模块

[tesseract-ocr识别引擎<sup>1</sup>](http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe)

[tesseract-ocr中文训练包<sup>2</sup>](https://raw.githubusercontent.com/tesseract-ocr/tessdata/4.00/chi_sim.traineddata)

### 下载必须文件

下载并安装ORC识别引擎<sup>1</sup>，下载中文训练包<sup>2</sup>并复制到 *C:\Program Files (x86)\Tesseract-OCR\tessdata*

### 配置环境变量

Windows用户请设置系统变量：

右键点击我的电脑-高级系统设置-系统属性-高级-环境变量；

用户变量 *Path* 添加 *C:\Program Files (x86)\Tesseract-OCR*

系统变量 *Path* 添加 *C:\Program Files (x86)\Tesseract-OCR*

系统变量添加 *TESSDATA_PREFIX* 设置为 *C:\Program Files (x86)\Tesseract-OCR* 

## 安装支持库

``` python
#开始-运行-输入CMD回车
pip install Pillow
pip install pytesseract
```

安装失败请尝试`easy_install pytesseract`

## 修改cddh.py

如果整张图片进行OCR，会耗费双倍的时间，脚本也是能够正常执行和返回结果的，只是太浪费时间，所以需要根据手机分辨率修改问题尺寸。

box参数设置：手机截一张答题时候的截图，电脑上1比1打开手机截图，用QQ截图分别查看 (黄，红，绿，蓝) 像素长度。


![sc1](https://raw.githubusercontent.com/se4/cddh/master/screenshot/screenshot1.jpg)



## 运行脚本

``` python
#安卓手机打开 usb调试模式
#开始-运行-输入CMD回车，切换到含有cddh.py文件夹目录
cd J:/
python cddh.py
```
