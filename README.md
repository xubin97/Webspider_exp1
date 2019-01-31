# spiders
simple python spider

编写这个简单的python爬虫是为了数据分析中收集数据这一步来做基础。这是最基础的，还会继续在此基础上继续扩展，使其功能更加完整！

此次是爬取的烂番茄网的排名top100的100个电影网页，来制成一个包含电影名称，观众评分，观看人数的datafrome表格。

步骤：现将100个网页html下载到rt_html文件夹中，然后运用python的beautiful soup构造函数中的.find() .find_all()来对其进行解析，查找。

```
from bs4 import BeautifulSoup
import os
import pandas as pd
```
```
df_list = []#创建字典列表，等待转成datafrome
folder = 'rt_html'#下载的html文件夹所在路径
for movie_html in os.listdir(folder):#循环从rt_html文件夹中加载当前要用的网页
    with open(os.path.join(folder, movie_html)) as file:
        soup=BeautifulSoup(file,'lxml')
        title=soup.find('title').contents[0][:-18]#获取当前网页标题（即电影名称）
        audience_score=soup.find('div',class_='audience-score meter').find('span').contents[0][:-1]#获取电影的观众评分
        a=soup.find('div',class_='audience-info hidden-xs superPageFontColor')#获取观众的人数
        num_audience_ratings=a.find_all('div')[1].contents[2].strip().replace(',','')
       
        
        df_list.append({'title': title,
                        'audience_score': int(audience_score),
                        'number_of_audience_ratings': int(num_audience_ratings)})

df = pd.DataFrame(df_list, columns = ['title', 'audience_score', 'number_of_audience_ratings'])#转换成datafrome
```
df.head()
#展示


            title        	           audience_score	   number_of_audience_ratings
0	12 Angry Men (Twelve Angry Men) (1957)	  97	          103672  

1	12 Years a Slave (2013)                 	90	          138789

2	A Hard Day's Night (1964)               	89	          50067

3	A Streetcar Named Desire (1951)	          90            54761

4	Alien (1979)	                            94	          457186

5	All About Eve (1950)	                    94	          44564
