import requests
from bs4 import BeautifulSoup

class Nnews:
    def newspull(self,coin, counter):
        ret = []
        url = "https://coinmarketcap.com/ru/currencies/"+coin+"/news/"
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')
        title = soup.find("meta", property="og:image")
        st = title['content']
        coinid = st.rpartition('/')[2].rpartition('.')[0]
        ll = requests.get('https://api.coinmarketcap.com/content/v3/news?coins='+coinid+'&page=1&size=10')
        data = ll.json()
        #for x in range(5):
        ret.append(data.get('data')[counter].get('meta').get('title')+": ")
        newsurl = data.get('data')[counter].get('meta').get('sourceUrl')
        newspage = requests.get(newsurl)
        soup2 = BeautifulSoup(newspage.text, 'html.parser')
        try:
            news = soup2.findAll('p', limit=None)
            newlen = len(news)
            totex = []
            for y in range(newlen):
                totex.append(news[y].text)
            ret.append(max(totex, key=len))
            rettex = ret[0] + ret[1]
            return rettex
        except: AttributeError