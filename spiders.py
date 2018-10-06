from bs4 import BeautifulSoup
import os
import pandas as pd

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