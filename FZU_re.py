import re
import pymysql
import requests
from pymysql import Connection
connection=pymysql.connect(host='localhost',
               port=3308,
               database='star',
               user='root',
               password='123456'
               )


if __name__=="__main__":
    url2="https://jwch.fzu.edu.cn/jxtz.htm"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
    }
    response=requests.get(url=url2,headers=headers)
    response.encoding=response.apparent_encoding
    fzu_text=response.text
    
    """
    fp=open("./ap.html","w",encoding="utf-8")
    fp.write(fzu_text)
    """
    
    com1=re.compile(r'\n')#匹配换行符
    com2=re.compile(r'\r')#匹配\r
    color=re.compile(r'<font color="red">')# remove color
    color2=re.compile(r'</font>')
    pp=re.compile(r' ')
    fzu_text=com1.sub('',fzu_text)
    fzu_text=com2.sub('',fzu_text)
    fzu_text=color.sub('',fzu_text)
    fzu_text=color2.sub('',fzu_text)
    fzu_text=pp.sub('',fzu_text)
    notice=r'<li>.*?<spanclass="doclist_time">(.*?)</span>(.*?)<ahref="(.*?)"target=".*?"title="(.*?)">.*?</a>'
    notice_list=re.findall(notice,fzu_text,re.S)
    """
    print(notice_list)
    print(len(notice_list))
    """
    notice_list3=[]
    for k in range(182,177,-1):
        url1='https://jwch.fzu.edu.cn/jxtz/%s.htm'%k
        fzu_left=requests.get(url=url1,headers=headers)
        fzu_left.encoding=fzu_left.apparent_encoding
        left=fzu_left.text
        left=com1.sub('',left)
        left=com2.sub('',left)
        left=pp.sub('',left)
        notice_list2=re.findall(notice,left,re.S)
        notice_list3.extend(notice_list2)
    notice_list.extend(notice_list3)
    len=(len(notice_list))


    
    try:
        with connection.cursor() as cursor:
            for date , title ,url, event in notice_list:
                url='https://jwch.fzu.edu.cn/'+url
                sql = "INSERT INTO FZU (date,title,event,url) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql,(date , title , event, url))
                #cursor.execute(sql,(date , title , event))
        connection.commit()
    finally:
        connection.close()