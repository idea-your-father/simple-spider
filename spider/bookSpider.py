import urllib.request
import re


# ctrl+alt+l  reformat code

def main():
    data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode('utf-8')
    pat = '<div class="name">(.*?)</div>'
    res = re.compile(pat).findall(data)

    f = open("d:/book.txt", 'a+')

    for i in res:
        print(i)
        f.write(i + "\n")
    f.close()


#     这里我使用懒惰匹配


if __name__ == '__main__':
    main()
