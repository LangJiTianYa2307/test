# from urllib.request import urlopen
# textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
#
# print(textPage.read())
# from urllib.request import urlopen
#
# textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
# print(str(textPage,'utf-8'))

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# html_content = urlopen('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1505727259613_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1505727259614%5E00_1292X653&word=%E5%B0%91%E5%8F%B8%E5%91%BD&f=3&oq=shaosi&rsp=0')
# bsObj = BeautifulSoup(html_content,'html.parser')
# # meta_content:存储文档的编码格式
# print(bsObj)
# # print(bsObj)
# # def pick_charset(html):
# #     """
# #     从文本中提取 meta charset
# #     :param html:
# #     :return:
# #     """
# #     charset = None
# #     m = re.compile('<meta .*(http-equiv="?Content-Type"?.*)?charset="?([a-zA-Z0-9_-]+)"?', re.I).search(html)
# #     if m and m.lastindex == 2:
# #         charset = m.group(2).lower()
# #     return charset
# # print(bsObj)
# # print(charset)
# # print(pick_charset("""charset ='utf-8'"""))

# from urllib.request import urlopen
# from io import StringIO
# import csv
#
# data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('utf-8','ignore')
# dataFile = StringIO(data)
# dictReader = csv.DictReader(dataFile)
#
# # print(dictReader.fieldnames)
#
# for row in dictReader:
#     print(row)

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import