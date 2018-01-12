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
import methods

g_cse_id = ''
g_cse_api_key = ''

questions = []

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
            #只搜题目
            start_browser_and_search(question, answers)

        else:
            return 'Waiting for new question...'

# def start_browser_and_search(search_wd):
#     print(search_wd)
#     s_url = 'https://www.baidu.com/s?wd=' + search_wd
#     search_question = urllib.parse.quote(search_wd)
#     webbrowser.open('https://www.baidu.com/s?wd=' + search_question)
#     input('按任意键继续')

def start_browser_and_search(question, answers):
    m1 = Thread(methods.run_algorithm(0, question, answers))
    m2 = Thread(methods.run_algorithm(1, question, answers))
    m3 = Thread(methods.run_algorithm(2, question, answers))
    m1.start()
    m2.start()
    m3.start()
    input('暂停,按任意键继续')


def main():
    while True:
        print(time.strftime('%H:%M:%S',time.localtime(time.time())))
        # 测试问答
        # start_browser_and_search(' 参加第一届古代奥运会的国家有', ['三个', '四个', '五个'])
        # start_browser_and_search('以下哪个不是清华大学的代表校花', ['紫荆', '山茶花', '丁香'])
        get_answer()
        time.sleep(1)



if __name__ == '__main__':
    main()
