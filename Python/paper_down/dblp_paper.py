import urllib.request
import re
import os

req = urllib.request.Request('https://dblp.uni-trier.de/search?q=title%3A%20Deep%20reinforcement%20learning%20type%3AConference_and_Workshop_Papers%3A%20venue%3AICLR%7CICML%7CNIPS%20year%3A%202021')
response = urllib.request.urlopen(req)
the_page = response.read().decode('utf-8')

paper_title = re.findall('<span class="title" itemprop="name">(.*?)</span>',the_page,re.S)
# paper_web = re.findall('view</b></p><ul><li><a href="(.*?)" itemprop="url">',the_page,re.S)
paper_web = re.findall('view</b></p><ul><li class="ee"><a href="(.*?)" itemprop="url">',the_page,re.S)

def get_pdf_arxiv(web_site,path):
    rep = urllib.request.urlopen(urllib.request.Request(web_site))
    page = rep.read().decode('utf-8')
    pdf_download = re.findall('<meta name="citation_pdf_url" content="(.*?)"/>',page,re.S)
    print(pdf_download[0])
    if (len(pdf_download) != 0):
        try:
            u = urllib.request.urlopen(pdf_download[0])
        except urllib.error.HTTPError:
            print(pdf_download[0], "url file not found")
            return
        block_sz = 8192
        with open(path, 'wb') as f:
            while True:
                buffer = u.read(block_sz)
                if buffer:
                    f.write(buffer)
                else:
                    break
        print("Sucessful to download " + path)



for i in range(len(paper_web)):
    if (paper_web[i].find("doi") == -1):
        list = paper_title[i].split(" ")
        paper_title[i] = "_".join(list)
        list = paper_title[i].split(":")
        paper_title[i] = "_".join(list)

        print(paper_title[i])
        path_dir = "2021年ICLR-ICML-NIPS_paper"
        dir_list=os.listdir(path_dir)
        path = paper_title[i] + "pdf"
        if path not in dir_list:
            get_pdf_arxiv(paper_web[i], os.path.join(path_dir, path))