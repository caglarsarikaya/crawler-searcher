import os
from urllib.request import urlopen
from link_finder import LinkFinder
import string

#dizin içerisinde klasör oluşturma
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

# queue ve crawled dosyalarını oluşturma
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# dosya oluşturma
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# dosyaya veri ekleme
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def searcher(word):
    with open("C:/Users/Papi/Downloads/Spider-master/Spider-master/crawler/crawled.txt", 'rt',encoding='utf8') as openfile:
        for line in openfile:
            for part in line.split():
                #print(part)
                #part = changer(part)
                #print(part)
                if word in part.lower():
                    a=line.split('*')[0]
                    print(a)

def changer(word):
    translationTable = str.maketrans("ıİüÜöÖçÇşŞğĞ", "iIuUoOcCsSgG")
    word = word.translate(translationTable)
    return word



# dosyadan silme
def delete_file_contents(path):
    open(path, 'w').close()


# okunan veriyi düzenleme
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt',encoding='utf8') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# toplanan linkleri dosyaya yazma
def set_to_file(links, file_name):
    with open(file_name,"w",encoding='utf8') as f:
        for l in sorted(links):
            f.write(l+"\n")

