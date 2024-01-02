import threading
import queue
import requests

url='https://www.realestate.com.au/sold/in-pyrmont,+nsw+2009/list-1?activeSort=solddate&source=refinement'
q=queue.Queue()
valid_proxies=[]
with open('get_proxy.txt','r') as f:
    proxies=f.readlines()
    for proxy in proxies:
        q.put(proxy)
        
        
def check_proxy():
    global q
    while not q.empty():
        proxy=q.get()
        try:
            response=requests.get('https://www.realestate.com.au/sold/in-pyrmont,+nsw+2009/list-1?activeSort=solddate&source=refinement',
                                  proxies={'http': proxy,'https': proxy})
            
        except:
            continue
        if response.status_code==200:
            print(proxy)
            # return proxy
            # file = open("valid_proxy.txt", "w+")
            # file.write(proxy)
            
for t in range(10):
    threading.Thread(target=check_proxy).start()
    
