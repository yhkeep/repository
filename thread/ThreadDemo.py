#
# L = []
# for i in range(100):
#     L.append("www.baidu.com")
# import time,threading
# def func():
#     for ls in L:
#         print(ls)
#         time.sleep(0.1)
# def func1():
#     for ls in L[0:50]:
#         print(ls)
#         time.sleep(0.1)
# def func2():
#     for ls in L[50:0]:
#         print(ls)
#         time.sleep(0.1)
# time1 = time.time()
# # func()
# # func1()
# t1 = threading.Thread(target=func)
# t2 = threading.Thread(target=func1)
# t3 = threading.Thread(target=func2)
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# time2 = time.time()
# print(time2-time1)


from bs4 import BeautifulSoup
import requests,xlwt
# 设置ua才能访问某些反爬虫网站
head = {
    "User-Agent":"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"
}
re = requests.get("http://www.runoob.com/python3/python3-multithreading.html",headers=head)
# print(re.status_code)
# 设置相应的编码个格式，re.encoding = "UTF-8"
re.encoding = re.apparent_encoding
# print(re.text)
soup = BeautifulSoup(re.text, 'html.parser')
# find_all( name , attrs , recursive , text , **kwargs )
# 此处访问只有a标签的并且属性是跳转_blank,这里使用遍历只是为了格式好看
value = []
string = "http://"
for values in soup.find_all("a",attrs={"target": "_blank"}):
    get_href = str(values.get("href"))
    if get_href[0:6] != "http://":
        if get_href[0].__eq__("/"):
            get_href.replace(str(get_href[0]), "")
            string += get_href
            value.append(get_href)
            string = "https://"
        elif get_href[0:1] == "//":
            get_href.replace(get_href[0:1],"http://")
            value.append(get_href)
    #     http://example.com/elsie
    value.append(get_href)
print(value)
# workBook = xlwt.Workbook()
# sheet = workBook.add_sheet("菜鸟",cell_overwrite_ok=True)
# for row,i in enumerate(value):
#     for col,v in enumerate(i):
#         sheet.write(row,v)
# workBook.save("菜鸟.xls")