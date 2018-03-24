from bs4 import BeautifulSoup
import os
import re
import csv
import chardet
import codecs



# 解析页面
def parse(text):
    bs = BeautifulSoup(text, 'lxml')

    # 获取dom节点
    title_dom = bs.find_all('h1', {'class': 'topictitle1'})
    body_dom = bs.find_all('div',{'id':re.compile('body\d+')})

    # 获取内容
    title = ''
    body = ''
    if title_dom:
        title = title_dom[0].text
    if body_dom:
        body = body_dom[0].text.replace('\n', '')
        # print(body)
    if title != '' and body != '':
        row = [title, body]
        save(row)


# 保存tile-body到csv
# 参考：https://www.cnblogs.com/unnameable/p/7366437.html
def save(row):
    # 解决Unicode乱码问题
    out = codecs.open('data.csv', 'a', encoding='utf_8_sig')
    csv_write = csv.writer(out)
    # 写入具体内容
    csv_write.writerow(row)


# 遍历所有html页面
def get_file():
    sum = 0
    cwd = os.getcwd()
    data_path = cwd + '/data'
    all_file = os.listdir(data_path)
    print(len(all_file))
    for file in all_file:
        print(file)
        file_path = os.path.join(data_path, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            print(type(text))
            parse(text)
            # break


if __name__ == '__main__':
    get_file()

