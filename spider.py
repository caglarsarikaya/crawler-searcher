import urllib
from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
import  requests
from bs4 import BeautifulSoup



class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    # dosyayı oluştur ve başla
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # sonuçları ekrana yazdırma ve dosyaları guncelleme
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            a= Spider.get_title(page_url)
            b=Spider.get_title2(page_url)
            #print(a)
            Spider.crawled.add(page_url + "*" + str(b) + "*" + str(a))
            Spider.update_files()

    @staticmethod
    def get_title(page_url):
        r = requests.get(page_url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        for i in soup.find_all("meta", {"name": "keywords"}):
            data = i
            return data

    @staticmethod
    def get_title2(page_url):
        r = urllib.request.urlopen(page_url)
        soup = BeautifulSoup(r, 'html.parser')
        return (soup.title.text)



    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # linkleri kuyruga ekleme
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
