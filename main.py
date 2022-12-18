import pyttsx3
import requests
from bs4 import BeautifulSoup
import sys
import io



def use_pyttsx3():
    # 创建对象,初始化获取语音引擎

    engine = pyttsx3.init()
    # 获取当前语音速率
    rate = engine.getProperty('rate')
    print(f'语音速率：{rate}')

    # 设置新的语音速率
    engine.setProperty('rate', 130)
    # 获取当前语音音量
    volume = engine.getProperty('volume')
    print(f'语音音量：{volume}')
    # 设置新的语音音量，音量最小为 0，最大为 1
    engine.setProperty('volume', 1.0)
    # 获取当前语音声音的详细信息
    voices = engine.getProperty('voices')
    print(f'语音声音详细信息：{voices}')
    # 设置当前语音声音为女性，当前声音不能读中文
    engine.setProperty('voice', voices[1].id)
    # 设置当前语音声音为男性，当前声音可以读中文
    engine.setProperty('voice', voices[0].id)
    # 获取当前语音声音
    voice = engine.getProperty('voice')
    print(f'语音声音：{voice}')
    # 语音文本
    path = 'test.txt'
    with open(path, encoding='utf-8') as f_name:
        words = str(f_name.readlines()).replace(r'\n', '')
    # 将语音文本说出来
    engine.say(words)
    engine.runAndWait()
    engine.stop()

def spider():
    text = str(input("Paste article\n"))
    res = requests.get(text)
    # res.encoding = 'utf-8'
    res.encoding = 'gdk'
    # print(res.text)
    f = open("test.txt","w",encoding='utf-8')
    data = BeautifulSoup(res.text,'html.parser')
    # print(data)
    articles = []
    #select.p查找标签，返回一个列表
    # print(data.select('.p'))
    # for i in range(len(data.select('.p'))):
    #     article = data.select('.p')[i].getText().strip()
    #     print(article)
    #     articles.append(article)
    x = data.find_all('p')
    print(x)
    # temp = data.select('#root > div > main > div > article > div.Post-RichTextContainer > div > div > div > p')
    for i in range(len(x)):
        # article = temp.select('.p')[i].getText().strip()
        article =x[i].getText().strip()
        # print(article)
        articles.append(article)
    text1 = " ".join(articles)
    f.write(text1)
    f.close()


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
    spider()
    use_pyttsx3()