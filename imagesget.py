# coding:utf-8
import urllib.request
import re

def get_html(url):
    page = urllib.request.urlopen(url)
    html_code = page.read()
    return html_code
def get_image(html_code):
    reg = r'src="(.+?\.gif_s400x0)" width'
    reg_img = re.compile(reg)
    html_code = html_code.decode('utf-8')  # python3
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:
      urllib.request.urlretrieve(img,'D:\\mp4\\%s.gif' % x)
      x += 1

url = input("请输入url:")
if url:
    pass
else:
    url = 'http://tieba.baidu.com/p/1753935195'
html_code = get_html(url)
get_image(html_code)
