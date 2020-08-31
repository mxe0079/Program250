# 这个脚本是从煎蛋网ooxx模块下载随手拍图片，只使用了最简单的requests模块和re模块的用法
```python
import requests
import re
import time


def open_jandan_page(url):
    r = requests.get(url)
    html = r.content.decode()
    pattern = r'<span class="current-comment-page">(.+?)</span>\s+?<a href="(.+?)">'  # Find the next page
    result = re.findall(pattern, html)
    try:
        next_page = result[1][1]
    except IndexError:
        next_page = None
    next_page = 'http:' + next_page
    pattern = r'<a href="(.+?)" target="_blank" class="view_img_link" referrerPolicy="no-referrer">'   # Find these pictures url
    result = re.findall(pattern, html)
    picture_url = []
    for i in result:
        picture_url.append('http:'+i)
    return next_page, picture_url


def download_store_picture(url):
    for i in url:
        r = requests.get(i)
        path = 'D:\Image\ooxx\\' + str(time.time()) + '.jpg'
        with open(path, 'wb') as f:
            f.write(r.content)


def main():
    current_page = 'http://i.jandan.net/ooxx/MjAyMDA4MzEtOTE=#comments'
    while True:
        next_page, picture_url = open_jandan_page(current_page)
        download_store_picture(picture_url)
        current_page = next_page
        if current_page == 'http:':
            exit(0)


if __name__ == "__main__":
    main()

```
