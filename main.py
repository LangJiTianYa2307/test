# import json
# from urllib.request import urlopen
#
# def getCountry(ipAddress):
#     response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
#     print(response)
#     responseJson = json.loads(response)
#     print(responseJson)
#     return responseJson.get('country_name'),responseJson.get('country_code'),responseJson.get('city')
#
# print(getCountry('61.142.3.131'))

# import csv
#
# # 当前路径创建文件
# scvFile = open("./test.csv",'w+')
# try:
#     write = csv.writer(scvFile)
#     write.writerow(('nuber','number plus 2','number times 2'))
#     for i in range(8):
#         write.writerow((i,i+2,i*2))
# finally:
#     scvFile.close()

# import csv
# from  urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html =urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
# bsObj = BeautifulSoup(html,'html.parser')
# try:
#     table = bsObj.find_all('table',class_ = 'wikitable')[0]
# except:
#     print(False)
# rows = table.findAll('tr')
#
# csvFile = open('./editors.csv','wt',newline='',encoding='utf-8')
# writer = csv.writer(csvFile)
# try:
#     for row in rows:
#         csvRow = []
#         for cell in row.findAll(['td','th']):
#             csvRow.append(cell.get_text())
#         writer.writerow(csvRow)
# except:
#     print(False)
# finally:
#     csvFile.close()
import pymysql

# suport_unicode1 = "ALTER DATABASE scraping CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci"
# suport_unicode2 ="""ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"""
# suport_unicode3 ="ALTER TABLE pages CHANGE title title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
# suport_unicode4 = "ALTER TABLE pages CHANGE content content VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
# 光标和连接，一个光标，可以有多个连接,光标和连接都应该关闭
conn = pymysql.connect(host='127.0.0.1',user ='root',passwd='1',db='mysql',charset="utf8")
# cur = conn.cursor()
cur1 = conn.cursor()
creat_database_scraping = """CREATE DATABASE scraping"""
try:
    cur1.execute(creat_database_scraping)
except:
    pass
# cur.execute("USE scraping")
cur1.execute("USE scraping")
try:
    cur1.execute("DROP TABLE pages")
except:
    print(False)
finally:
    cur1.execute("CREATE TABLE pages (id BIGINT(7) NOT NULL AUTO_INCREMENT, \
                                    title VARCHAR(200),\
                                    content VARCHAR(10000),\
                                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\
                                    PRIMARY KEY(id))")
sql = "SELECT * FROM pages"
sql_insert = """INSERT INTO pages(title,content) VALUES ("我的世界","This is a boy")"""
sql_delete = "delete from pages where id = %d"
# cur.execute(sql_delete %(2))
# cur.execute(sql_delete %(3))
# cur.execute(sql_delete %(4))
# cur.execute(sql_delete %(5))
# cur.execute(sql_delete %(6))
# cur.execute(suport_unicode1)
# cur.execute(suport_unicode2)
# cur.execute(suport_unicode3)
# cur.execute(suport_unicode4)
# cur.execute(sql_insert)
# cur.execute(sql)
cur1.execute("SELECT * FROM pages WHERE id=2")
# print(cur.fetchall())
# print(cur1.rowcount)
cur1.execute("""INSERT INTO pages(title,content) VALUES ("it","This is a boy")""")
cur1.execute(sql_insert)
cur1.execute(sql_insert)
cur1.execute(sql_insert)
cur1.execute(sql_insert)
cur1.execute(sql_insert)
cur1.execute(sql_insert)
# cur1.execute("""INSERT INTO pages(id,title,content) VALUES (1,'a','a')""")
# print(cur1.lastrowid)

cur1.execute("SELECT * FROM pages WHERE title ='我的世界'")
# conn.commit()
# print(cur1.lastrowid)
# cur.close()
# print(cur1.rowcount)
print(cur1.fetchone()[0])
cur1.close()
conn.close()

# import pymysql
# import re
# import datetime
# import random
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
#
# conn = pymysql.connect(host='127.0.0.1',user ='root',passwd='1',db='mysql',charset="utf8")
# cur = conn.cursor()
# cur.execute("USE scraping")
# try:
#     cur.execute("DROP TABLE pages")
# except:
#     print(False)
# finally:
#     cur.execute("CREATE TABLE pages (id BIGINT(7) NOT NULL AUTO_INCREMENT, \
#                                     title VARCHAR(200),\
#                                     content VARCHAR(10000),\
#                                     created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\
#                                     PRIMARY KEY(id))")
# random.seed(datetime.datetime.now())
#
# def store(title,content):
#     cur.execute("INSERT INTO pages(title,content) VALUES (%s,%s)",(title,content))
#     cur.connection.commit()
#
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html,'html.parser')
#     title = bsObj.find("h1").get_text()
#     content = bsObj.find('div',id='mw-content-text').find('p').get_text()
#     store(title,content)
#     return bsObj.find('div',id='bodyContent').findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
#
# links = getLinks("/wiki/Kevin_Bacon")
# try:
#     while(len(links)>0):
#         newArticle = links[random.randint(0,len(links)-1)].attrs['href']
#         print(newArticle)
#         getLinks(newArticle)
# except:
#     print(False)
# finally:
#     cur.close()
#     conn.close()
