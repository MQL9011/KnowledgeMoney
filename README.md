
- 环境:`python3` `pip3`  `OCR`办法目前只支持`Mac`



#冲顶大会快速搜索(废弃了,接口不能用,只能用OCR的办法)


---

# OCR文字识别的方法,目前只支持Mac
采用的大致原理是手机连上Mac,通过自带的QuickTime实时显示手机屏幕,具体做法可以百度「怎么用 Quick Time Player 为 iPhone 录制屏幕」

- 安装[google的文字识别引擎](https://github.com/tesseract-ocr/tesseract/wiki)

```
brew install tesseract
```

- 下载[中文语言识别包](https://github.com/tesseract-ocr/tessdata)
- 找到语言包`chi_sim.traineddata`
- 下载下来后放到,这里是`Mac`上的路径  
`/usr/local/Cellar/tesseract/3.05.01/share/tessdata/`
- `Win`上的请去看[google的官方文档](https://github.com/tesseract-ocr/tesseract/wiki)


- 安装python依赖库

```
pip3 install -r requirements.txt
```

- 自行修改代码中的屏幕截图区域Frame

```
#自行修改截图位置 "x, y, w, h "
#问题的截图  60, 95, 340, 280
questionLocation = "60, 95, 340, 80"
#答案一截图  95, 200, 270, 35
answer_one_loadtion = "95, 200, 270, 35"
#答案二截图  95, 260, 270, 35
answer_two_loadtion = "95, 260, 270, 35"
#答案三截图  95, 316, 270, 35
answer_thr_loadtion = "95, 316, 270, 35"
```

- 运行程序

```
python3 KnMoney.py
```




# 感谢

- 部分代码出自[TopSup](https://github.com/Skyexu/TopSup)

# 喜欢的话记得star哦 或 请我喝咖啡吧


支付宝

![image.png](http://upload-images.jianshu.io/upload_images/1755091-b6dbc081dd54c2e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/200)
