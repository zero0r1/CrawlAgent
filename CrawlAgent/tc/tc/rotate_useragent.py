# -*-coding:utf-8-*-
from scrapy import log  
  
"""避免被ban策略之一：使用useragent池。 
 
使用注意：需在settings.py中进行相应的设置。 
"""  
  
import random
import base64
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware  
  
class RotateUserAgentMiddleware(UserAgentMiddleware):  
  
    def __init__(self, user_agent=''):  
        self.user_agent = user_agent  
  
    def process_request(self, request, spider):  
        ua = random.choice(self.user_agent_list)  
        if ua:  
            #显示当前使用的useragents
            #print "********Current UserAgent:%s************" % ua
  
            #记录
            #log.msg('Current UserAgent: ' + ua, level='INFO')
            request.headers.setdefault('User-Agent', ua)

        ip = random.choice(self.proxy_list)
        request.meta['proxy'] = ip
  
    #the default user_agent_list composes chrome,I
    #E,firefox,Mozilla,opera,netscape
    #for more user agent strings,you can find it in
    #http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"]

    proxy_list = ["http://1.196.161.162:9999",
    "http://27.155.101.233:3128",
    "http://113.89.55.21:9999",
    "http://112.114.98.93:8118",
    "http://183.30.197.240:9797",
    "http://61.136.163.245:8104",
    "http://125.121.113.147:8118",
    "http://49.5.8.132:8888",
    "http://125.111.6.215:80",
    "http://101.132.148.7:8080",
    "http://114.228.222.81:8118",
    "http://202.100.83.139:80",
    "http://121.8.98.197:80",
    "http://113.88.14.17:9797",
    "http://112.114.98.58:8118",
    "http://124.206.133.219:3128",
    "http://116.228.44.9:8085",
    "http://180.97.104.14:80",
    "http://222.240.81.3:8088",
    "http://113.65.161.120:9797",
    "http://112.114.93.228:8118",
    "http://180.115.81.161:808",
    "http://59.44.164.34:3128",
    "http://222.189.4.164:80",
    "http://113.120.80.55:3128",
    "http://101.132.146.103:8080",
    "http://121.235.232.116:24419",
    "http://58.216.199.222:3129",
    "http://59.44.164.45:3128",
    "http://113.83.241.174:8118",
    "http://60.164.225.5:8080",
    "http://121.8.98.196:80",
    "http://114.97.185.150:808",
    "http://180.173.71.200:9797",
    "http://49.68.37.39:808",
    "http://58.220.95.107:8080",
    "http://113.68.227.123:9999",
    "http://182.42.244.210:808",
    "http://120.40.140.78:808",
    "http://113.118.98.31:9797",
    "http://114.101.19.1:65309",]

  