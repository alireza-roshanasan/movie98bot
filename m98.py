# -*- coding: utf-8 -*-
import time
import datetime
import telepot
import cfscrape
import requests
from bs4 import BeautifulSoup
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

def handle(msg):
    print msg
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command
    if command == '/chat_id': #get user chat-id 
            print chat_id
    elif command == command:
        if chat_id != 1578421667: #can delete it 
            num = 1
            for i in range(1, 2): # number of pages 
                ############  get web page source   #######################
                scraper = cfscrape.create_scraper() 
                url = "http://movie98.net/page/"  + str(i) + "?s=" + command
                get =  scraper.get(url).content # use scraper for bypass some bot blockers :-\
                soup = BeautifulSoup(get, "html.parser")
                soup.prettify() 
                # print soup
                ##########   get title  ##############
                for post in soup.find_all("a" ,attrs={"rel": "bookmark", "class":"more"}): 
                    # print post
                    ti =  post['title']
                    seri = ti.split()
                    if u'سریال' not in seri: 
                            href = post ['href']
                            tit2 = ti.encode('utf-8')
                            href8 = href.encode('utf-8')
                            hashtag = "\n" + "#" + "movie" + "_" +str(num)
                            tit = tit2 + hashtag
                            ########### get continue link ##############
                            bot.sendMessage(chat_id, "######## Next Video ########")
                            bot.sendMessage(chat_id,tit)
                            get_two = scraper.get(href).text
                            soup_two = BeautifulSoup(get_two, "html.parser")
                            soup_two.prettify("utf-8")
                            num = num + 1 
                            ############# get images  ##############
                            for cont in soup_two.find_all("div", attrs={"class":"context"}):
                                for pis in cont.find_all("p"):
                                    for img in pis.find_all("img", attrs={"class":"size-full","height":"500"}): # find images and send to user ,but some pictures were not sent(I could not fix it)because of this i disable it 
                                        co = 1
                                        image = img['src']
                                        # image8 = image.encode('utf-8')
                                        # print image8
                                        # print image
                                        # de = image.decode('utf-8')
                                        # bot.sendPhoto(chat_id, str(de))
                                        # print "aaaaaa"
                                for data in cont.find_all("p", attrs={"style":"text-align: justify;"}):
                                    if co <= 1 :
                                        co = co + 1
                                        data2 = data.getText()
                                        # print data2
                                        # print "ccccccc"
                            for download in soup_two.find_all("div", attrs={"class":"downloadmovie"}): # get the download links 
                            ############  get informations ########################
                                data4 = data2.encode('utf-8')
                                data8 = data4.replace(':','')
                                # print data8
                                data5 = data8.replace('منتشر کننده فایل  Movie98', '')
                                # print data5
                                data6 = data5.replace('زیرنویس  در ادامه مطلب', 'زیرنویس : در ادامه')
                                # print data6
                                # print "bbbbbb"
                                bot.sendMessage(chat_id, data6)
                                qu = 0
                                for li in download.find_all("li"):
                                    lili = li.getText()
                                    lili = lili.encode('utf-8')
                                    # print "fffff"
                            ############  remove other texts #######################
                                    del1 = lili.replace('دانلود', '')
                                    info = del1.replace('زیرنویس', '')
                                    # print info
                            ########## get download link ##########################
                                    link_sub2 = '<a href="#"></a>'
                                    for sub in li.find_all("a", attrs={"class":"msubtitle"}):
                                        sub = sub['href']
                                        link_sub = '<a href="%s">download subtitle...</a>' %sub
                                        link_sub2 = link_sub.encode('utf-8')
                                        # print "hhhhh"
                                    for a in li.find_all("a", attrs={"class":"mlink"}):
                                        lin =  a['href'] 
                                        qu = 1 + qu
                                        text = "لینک دانلود شماره"
                                        # text2 = text.encode('utf-8')
                                        qul = text+str(qu)
                                        ### make link with parsing html
                                        link = '<a href="%s">%s</a>' %(lin, ti)
                                        link2 = link.encode('utf-8')
                                        full = qul + '\n' + link2 + '\n' + info + '\n' + link_sub2
                                        bot.sendMessage(chat_id, full, parse_mode="HTML", disable_web_page_preview='true')

bot = telepot.Bot('YOUR TOKEN')
MessageLoop(bot, handle).run_as_thread()
print 'ITS WORKING ...'

while 1:
    time.sleep(35)

######
