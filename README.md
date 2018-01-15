
- 环境:`python3` `pip3`  `OCR`办法目前只支持`Mac`

---


# OCR文字识别搜题,目前只支持Mac
采用的大致原理是手机连上Mac,通过自带的QuickTime实时显示手机屏幕,具体做法可以百度「怎么用 Quick Time Player 为 iPhone 录制屏幕」

- 安装[google的文字识别引擎](https://github.com/tesseract-ocr/tesseract/wiki)

```
brew install tesseract
```

- 下载[中文语言识别包](https://github.com/tesseract-ocr/tessdata)
- 找到语言包`chi_sim.traineddata`
- 下载下来后放到,这里是`Mac`上的路径  
`/usr/local/Cellar/tesseract/3.05.01/share/tessdata/`


- 安装python依赖库

```
pip3 install -r requirements.txt
```

- 自行修改代码中的屏幕截图区域Frame

```

#由于每个人屏幕尺寸不同需要自行修改截图Frame "x, y, w, h "
#冲顶大会截图坐标
cddh_ques_loca       = "70, 150, 310, 120"
cddh_answer_one_loca = "100, 275, 270, 35"
cddh_answer_two_loca = "100, 330, 270, 35"
cddh_answer_thr_loca = "100, 376, 270, 35"

```

- 运行程序

```
python3 KnMoney.py
```

# 识别效果   
- OCR毕竟比不上接口直接拿数据,会存在一定误差,发现识别不准是可以自行调节图像处理参数

```
#处理图像
enh_con = ImageEnhance.Contrast(image)
#对比度,锐度,亮度
contrast = 2.0
sharpness = 5.0
brightness = 5.0
```

- 这是截图后识别成文字的效果  



![image.png](http://upload-images.jianshu.io/upload_images/1755091-e9fe0a308314904a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/800)

- 这是丢进百度搜索的效果


![image.png](http://upload-images.jianshu.io/upload_images/1755091-29976d8fb0419b5f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/800)



# 感谢

- 部分代码出自[TopSup](https://github.com/Skyexu/TopSup)

# 喜欢的话记得star哦
