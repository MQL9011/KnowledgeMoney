# coding: utf-8

#需要自行修改截图Frame "x, y, w, h "
#冲顶大会截图坐标
cddh_ques_loca       = "70, 150, 310, 120"
cddh_answer_one_loca = "100, 275, 270, 35"
cddh_answer_two_loca = "100, 330, 270, 35"
cddh_answer_thr_loca = "100, 376, 270, 35"

#百万英雄截图坐标
bwyy_ques_loca       = "70, 115, 310, 130"
bwyy_answer_one_loca = "100, 265, 270, 35"
bwyy_answer_two_loca = "100, 330, 270, 35"
bwyy_answer_thr_loca = "100, 390, 270, 35"

#芝士超人截图坐标
zscr_ques_loca       = "70, 95, 310, 90"
zscr_answer_one_loca = "100, 195, 270, 35"
zscr_answer_two_loca = "100, 255, 270, 35"
zscr_answer_thr_loca = "100, 315, 270, 35"

#网易新闻截图坐标
wyxw_ques_loca       = "90, 165, 310, 70"
wyxw_answer_one_loca = "100, 215, 270, 35"
wyxw_answer_two_loca = "100, 275, 270, 35"
wyxw_answer_thr_loca = "100, 345, 270, 35"

#other
questions = []

import time
import datetime
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

def getImgFromScreenCapture(ques, ans_one, ans_two, ans_thr):
    question = os.system("screencapture -R \" {} \" ./question_screenshot.png".format(ques))
    answer_one = os.system("screencapture -R \"{}\" ./answers_one.png".format(ans_one))
    answer_two = os.system("screencapture -R \"{}\" ./answers_two.png".format(ans_two))
    answer_thr = os.system("screencapture -R \"{}\" ./answers_thr.png".format(ans_thr))

    question_img = Image.open("./question_screenshot.png")
    answer_one_img = Image.open("./answers_one.png")
    answer_two_img = Image.open("./answers_two.png")
    answer_thr_img = Image.open("./answers_thr.png")

    question_enh = getImageFromImageEnhanceForQuestion(question_img)
    ans_one_enh  = getImageFromImageEnhance(answer_one_img)
    ans_two_enh  = getImageFromImageEnhance(answer_two_img)
    ans_thr_enh  = getImageFromImageEnhance(answer_thr_img)

    #使用简体中文解析图片
    print('OCR  ' + datetime.datetime.now().strftime('%H:%M:%S'))
    question_text = pytesseract.image_to_string(question_enh, lang='chi_sim')
    question = question_text
    answers = ['','','']
    return question, answers

def getImgFromScreenCaptureAgain(ques, ans_one, ans_two, ans_thr):
    question = os.system("screencapture -R \" {} \" ./question_screenshot.png".format(ques))
    answer_one = os.system("screencapture -R \"{}\" ./answers_one.png".format(ans_one))
    answer_two = os.system("screencapture -R \"{}\" ./answers_two.png".format(ans_two))
    answer_thr = os.system("screencapture -R \"{}\" ./answers_thr.png".format(ans_thr))

    question_img = Image.open("./question_screenshot.png")
    answer_one_img = Image.open("./answers_one.png")
    answer_two_img = Image.open("./answers_two.png")
    answer_thr_img = Image.open("./answers_thr.png")

    question_enh = getImageFromImageEnhanceForQuestion(question_img)
    ans_one_enh  = getImageFromImageEnhance(answer_one_img)
    ans_two_enh  = getImageFromImageEnhance(answer_two_img)
    ans_thr_enh  = getImageFromImageEnhance(answer_thr_img)

    #使用简体中文解析图片
    # print('OCR  ' + datetime.datetime.now().strftime('%H:%M:%S'))
    question_text = pytesseract.image_to_string(question_enh, lang='chi_sim')
    # print(question_text)
    ans_one_text = pytesseract.image_to_string(ans_one_enh, lang='chi_sim')
    # print(ans_one_text)
    ans_two_text = pytesseract.image_to_string(ans_two_enh, lang='chi_sim')
    # print(ans_two_text)
    ans_thr_text = pytesseract.image_to_string(ans_thr_enh, lang='chi_sim')
    # print(ans_thr_text)
    question = question_text
    answers = [ans_one_text, ans_two_text, ans_thr_text]
    print(answers)
    return question, answers

def getImageFromImageEnhanceForQuestion(image):
        #处理图像参数
        enh_con = ImageEnhance.Contrast(image)
        #对比度,锐度,亮度
        contrast = 2.0
        sharpness = 5.0
        brightness = 5.0
        enh_image = enh_con.enhance(contrast)
        enh_image = enh_con.enhance(sharpness)
        enh_image = enh_con.enhance(brightness)
        # enh_image.show()
        return enh_image



def getImageFromImageEnhance(image):
        #处理图像参数
        enh_con = ImageEnhance.Contrast(image)
        #对比度,锐度,亮度
        contrast = 10.0
        sharpness = 10.0
        brightness = 15.0
        enh_image = enh_con.enhance(contrast)
        enh_image = enh_con.enhance(sharpness)
        enh_image = enh_con.enhance(brightness)
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



def start_browser_and_search(question, answers, opBrowserFlag):
    print('拉起浏览器    ' + datetime.datetime.now().strftime('%H:%M:%S'))
    print('问题:  ' + question)
    print('1 %s'% answers[0])
    print('2 %s'% answers[1])
    print('3 %s'% answers[2])
    if opBrowserFlag == True:
        print('true')
        m1 = Thread(methods.run_algorithm(0, question, answers))
        m2 = Thread(methods.run_algorithm(1, question, answers))
        m3 = Thread(methods.run_algorithm(2, question, answers))
        m1.start()
        m2.start()
        m3.start()
    else:
        print('false')
        m2 = Thread(methods.run_algorithm(1, question, answers))
        m3 = Thread(methods.run_algorithm(2, question, answers))
        m2.start()
        m3.start()




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

def startPlay(questionLocation,answer_one_loadtion,answer_two_loadtion,answer_thr_loadtion):
    while True:
        try:
            print('开始   ' + datetime.datetime.now().strftime('%H:%M:%S'))
            question, answers = getImgFromScreenCapture(questionLocation,answer_one_loadtion,answer_two_loadtion,answer_thr_loadtion)
            start_browser_and_search(question, answers, True)
            question_again, answers_again = getImgFromScreenCaptureAgain(questionLocation,answer_one_loadtion,answer_two_loadtion,answer_thr_loadtion)
            start_browser_and_search(question, answers, False)
            input('已暂停,按任意键继续')
            # input('%s \n %s' % (question,answers))
            time.sleep(1)
        except Exception as error:
            print(error)
            time.sleep(1)
            startPlay()


def main():
    index = input(' 1.冲顶大会 \n 2.百万英雄 \n 3.芝士超人\n 4.网易新闻\n请选择玩哪个: \n')
    if index == '1':
        input('冲顶大会_题目出现后按回车开始识别!')

        startPlay(cddh_ques_loca, cddh_answer_one_loca, cddh_answer_two_loca, cddh_answer_thr_loca)
    elif index == '2':
        input('百万英雄_题目出现后按回车开始识别!')

        startPlay(bwyy_ques_loca, bwyy_answer_one_loca, bwyy_answer_two_loca, bwyy_answer_thr_loca)
    elif index == '3':
        input('芝士超人_题目出现后按回车开始识别!')

        startPlay(zscr_ques_loca, zscr_answer_one_loca, zscr_answer_two_loca, zscr_answer_thr_loca)
    elif index == '4':
        input('网易新闻_题目出现后按回车开始识别!')

        startPlay(wyxw_ques_loca, wyxw_answer_one_loca, wyxw_answer_two_loca, zscr_answer_thr_loca)
    else:
        print('重选!')
        main()






if __name__ == '__main__':
    main()
