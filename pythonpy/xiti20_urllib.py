import urllib.request

baidu=urllib.request.urlpoen('http://www.baidu.com/').read()
print(baidu.info) #输出baidu首页头部信息
print(baidu.getcode()) #输出baidu首页网页的状态码
print(baidu.geturl()) #输出请求的url地址
for line in baidu:
    print(line)
baidu.close() #关闭对象方法
