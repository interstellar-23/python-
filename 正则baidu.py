import requests
import re
import pymysql

connection=pymysql.connect(host='localhost',
               port=3308,
               database='star',
               user='root',
               password='123456'
               )


if __name__=='__main__':
    url='https://baike.baidu.com/cms/home/eventsOnHistory/11.json?_=1699268312119'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
    }
    response=requests.get(url=url,headers=headers)
    response.encoding=response.apparent_encoding
    day_dic=response.json()
    #print(day_dic)
    #k=str(input(""))
    year_list=[]
    title_list=[]
    class_list=[]
    desc_list=[]
    desc_list2=[]
    kk=''
    """
    新建一些空字典便于储存
    """
    list_2=day_dic["11"]["1106"]
    for year in list_2:
        year_list.append(year['year'])
    #print(year_list)
    for title in list_2:
        title_list.append(title['title'])
    #print(title_list)
    extra='(.*?)<a target="_blank" href=".*?">(.*?)</a>(.*+)'
    for i in range(len(title_list)):
        title_list[i]=re.findall(extra,title_list[i],re.S)
        
        if title_list[i][0][2]=='出生':
            class_list.append('birth')
        elif title_list[i][0][2]=='逝世':
            class_list.append('death')
        else:
            class_list.append('event')
            '''
            写完发现这里可以通过字典直接读取type 但貌似这种方法也行的通 所以先不做更改
            '''
        title_list[i]=title_list[i][0][0]+title_list[i][0][1]+title_list[i][0][2]
        
    #print(len(title_list))
    #print(class_list)
    for desc in list_2:
        desc_list.append(desc['desc'])
    for k in range(len(desc_list)):
        words='(.*?)<a target="_blank" href=".*?">(.*?)</a>(.*?)'
        '''
        据发现 每一串的字符有一定的规律 所以可以定向匹配
        '''
        desc_list[k]=re.findall(words,desc_list[k],re.S)
    #print(len(desc_list))
    print(len(desc_list))
    for s in desc_list:
        for m in s:
            kk=kk+m[0]+m[1]+m[2]
        desc_list2.append(kk)
        kk=''
    """
    到这一步成功的建立了简要信息的列表
    """
    try:
         with connection.cursor() as cursor:
             for year in year_list:
                 sql = "INSERT INTO FZU (year) VALUES (%s)"
                 cursor.execute(sql,year)
             for type in class_list:
                 sql = "INSERT INTO FZU (type) VALUES (%s)"
                 cursor.execute(sql,type)
             for title in title_list:
                 sql = "INSERT INTO FZU (title) VALUES (%s)"
                 cursor.execute(sql,title)
             for desc in desc_list:
                 sql = "INSERT INTO FZU (desc) VALUES (%s)"
                 cursor.execute(sql,desc)
         connection.commit()
    finally:
        connection.close()