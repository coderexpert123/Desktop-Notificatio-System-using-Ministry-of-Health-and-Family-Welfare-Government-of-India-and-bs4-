from  plyer import  notification
import  requests
from bs4 import  BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(

        title=title,
        message=message,
        app_icon="we.ico",
        timeout=15
    )

def getData(url):
    r=requests.get(url)
    return r.text
if __name__=="__main__":
    while True:
        #notifyMe("Nishant " , " Stop This epidmic togather ")
        myHtmlData=getData("https://mohfw.gov.in/")
        #print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())
        mydataStr=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):

            mydataStr += tr.get_text()
        mydataStr=mydataStr[1:]
        itemlist=(mydataStr.split("\n\n"))
        stetae=['Maharashtra','Ladakh', 'Kerala']
        for item in itemlist[0:22]:
            datalist=(item.split('\n'))
            if datalist[1] in stetae:
                print(datalist)
                ntitle="Cases of Covid 19 "
                ntext=f" States :{datalist[1]} \nIndian: {datalist[2]}  \nCured : {datalist[3]} \nDeath : {datalist[4]}"
                notifyMe(ntitle,ntext)
                time.sleep(2)
        time.sleep(3600)
