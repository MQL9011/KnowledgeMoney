# coding: utf-8
# quote from kmaiya/HQAutomator
# 谷歌搜索部分原版搬运，未做修改

import time
import json
import requests
import webbrowser
from urllib import parse
import urllib.parse
from threading import Thread
from PIL import Image
from PIL import ImageEnhance
import pytesseract
import os
#mySelf Part
import methods

questions = []
def getImgFromScreenCapture():
    #常用截图参数 iphone6/6s
    #问题的截图  60, 95, 340, 280
    #答案一截图  95, 200, 270, 35
    #答案二截图  95, 260, 270, 35
    #答案三截图  95, 316, 270, 35

    question = os.system("screencapture -R \"60, 95, 340, 280\" ./question_screenshot.png")
    answer_one = os.system("screencapture -R \"95, 200, 270, 35\" ./answers_one.png")
    answer_two = os.system("screencapture -R \"95, 260, 270, 35\" ./answers_two.png")
    answer_thr = os.system("screencapture -R \"95, 316, 270, 35\" ./answers_thr.png")

    question_img = Image.open("./question_screenshot.png")
    answer_one_img = Image.open("./answers_one.png")
    answer_two_img = Image.open("./answers_two.png")
    answer_thr_img = Image.open("./answers_thr.png")

    ans_one_enh = getImageFromImageEnhance(answer_one_img)
    ans_two_enh = getImageFromImageEnhance(answer_two_img)
    ans_thr_enh = getImageFromImageEnhance(answer_thr_img)

    #使用简体中文解析图片
    question_text = pytesseract.image_to_string(question_img, lang='chi_sim')
    print(question_text)
    ans_one_text = pytesseract.image_to_string(ans_one_enh, lang='chi_sim')
    print(ans_one_text)
    ans_two_text = pytesseract.image_to_string(ans_two_enh, lang='chi_sim')
    print(ans_two_text)
    ans_thr_text = pytesseract.image_to_string(ans_thr_enh, lang='chi_sim')
    print(ans_thr_text)
    question = question_text
    answers = [ans_one_text, ans_two_text, ans_thr_text]
    return question, answers

def getImageFromImageEnhance(image):
        #处理图像参数
        enh_con = ImageEnhance.Contrast(image)
        #对比度
        contrast = 10.0
        enh_image = enh_con.enhance(contrast)
        # enh_image.show()
        return enh_image



def get_answer():
    resp = requests.get('http://htpmsg.jiecaojingxuan.com/msg/current',timeout=4).text
    resp_dict = json.loads(resp)
    if resp_dict['msg'] == 'no data':
        return 'Waiting for question...'
    else:
        resp_dict = eval(str(resp))
        question = resp_dict['data']['event']['desc']

        question = question[question.find('.') + 1:question.find('?')]
        if question not in questions:
            questions.append(question)
            answers = eval(resp_dict['data']['event']['options'])
            search_wd = question + answers[0] + answers[1] + answers[2]
            start_browser_and_search(question, answers)

        else:
            return 'Waiting for new question...'



def start_browser_and_search(question, answers):
    print(question)
    print('1 %s'% answers[0])
    print('2 %s'% answers[1])
    print('3 %s'% answers[2])
    m1 = Thread(methods.run_algorithm(0, question, answers))
    m2 = Thread(methods.run_algorithm(1, question, answers))
    m3 = Thread(methods.run_algorithm(2, question, answers))
    m1.start()
    m2.start()
    m3.start()
    input('已暂停,按任意键继续')




def testPlay():
    # 测试问答
    # question = '参加第一届古代奥运会的国家有'
    question = '以下哪个不是清华大学的代表校花'
    # answers = ['三个', '四个', '五个']
    answers = ['紫荆', '山茶花', '丁香']
    print(question)
    print('1 %s'% answers[0])
    print('2 %s'% answers[1])
    print('3 %s'% answers[2])
    start_browser_and_search(question, answers)


def startCddh():
    while True:
        try:
            print(time.strftime('%H:%M:%S',time.localtime(time.time())))
            # testPlay()
            get_answer()
            time.sleep(1)
        except Exception as error:
            print(error)
            time.sleep(1)
            startCddh()

def startBWYH():
    while True:
        try:
            print(time.strftime('%H:%M:%S',time.localtime(time.time())))
            question, answers = getImgFromScreenCapture()
            start_browser_and_search(question, answers)
            time.sleep(1)
        except Exception as error:
            print(error)
            time.sleep(1)
            startBWYH()


def main():
    index = input(' 1.冲顶大会 \n 2.西瓜视频百万英雄 \n 3.芝士超人(开发中)\n请选择玩哪个: \n')
    if index == '1':
        startCddh()
    elif index == '2':
        startBWYH()
    else:
        print('重选!')
        main()






if __name__ == '__main__':
    main()
