import requests
from bs4 import BeautifulSoup
url='https://free-proxy-list.net/'
headers={'Urgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
proxies=[]

def get_proxies(url,headers):
    res = requests.get(url=url,headers=headers)
    soup=BeautifulSoup(res.content,'html.parser')
    table=soup.find('table',{'class':'table table-striped table-bordered'})
    for tr in table.find_all('tr'):
        td=tr.find_all('td')
        try: 
            proxies.append({'ip': td[0].text.strip(), 'port': td[1].text.strip()})
        except IndexError:
            continue
    return proxies

proxies=get_proxies(url=url,headers=headers)
# print(proxies)
with open('get_proxy.txt','w') as f:
    for proxy in proxies:
        f.write(f"{proxy['ip']}:{proxy['port']}\n")