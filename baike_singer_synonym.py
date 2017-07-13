# coding: utf-8
import sys
import json
import urllib
from BeautifulSoup import BeautifulSoup

reload( sys )
sys.setdefaultencoding('utf-8')


def data_collect(url, soup, count, total):
    print 'Crawing %d / %d url: ' % (count, total)
    print json.dumps(url, ensure_ascii=False)
    data_want = {}
    data_want['url'] = url

    table_node = soup.find('dl', attrs={'class': 'basicInfo-block basicInfo-left'})
    data_want['table'] = table_node.getText().replace("&nbsp;", "")

    return data_want


def make_url():
    urls = []
    singers = []
    with open("/home/lulu/Desktop/vinci/svm/test/v2/歌手信息/热门华语歌手.txt") as f:
        for word in f:
            word = word.strip()
            if word != "":
                singers.append(word)
                url = 'http://baike.baidu.com/item/' + word
                urls.append(url)
    return urls, singers


def crawler(urls):
    all_singers = []
    count = 0
    total = len(urls)
    for i in range(len(urls)):
        try:
            count = count + 1
            response = urllib.urlopen(urls[i].decode('utf-8').encode('utf-8'))
            data = response.read()
            soup = BeautifulSoup(data)
            table_content = data_collect(urls[i], soup, count, total)
            all_singers.append([singers[i], table_content["table"]])
        except:
            print "crawl failed url: %s" % urls[i]
    return all_singers


def save_all_singers(all_singers):
    with open("/home/lulu/Desktop/vinci/svm/test/v2/歌手信息/singer_info.txt", "w") as ret_f:
        for word in all_singers:
            ret_f.write(json.dumps(word, ensure_ascii=False))
            ret_f.write("\n")


urls, singers = make_url()
# urls = urls[400:405]
# singers = singers[400:405]
all_singers = crawler(urls)
save_all_singers(all_singers)

