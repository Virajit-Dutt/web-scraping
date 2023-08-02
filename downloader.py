# download file from url and save it locally
import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

def downloader():

    def down(link):
        if link == '':
            return

        extension = link.split('.')[-1]
        if (extension == 'css' or extension == 'js' or extension == 'txt' or 
            extension=='ico' or extension=='png' or extension=='jpg'):
            pass
        else:
            extension = 'html'

        content = requests.get(link, allow_redirects=True)
        fname = link.split('/')[-1]
        
        if fname == '':
            fname = link.split('/')[-2]
        
        # remove special characters from fname
        fname = ''.join(e for e in fname if e.isalnum())

        if extension == 'png' or extension=='jpg' or extension=='ico':
            fol = 'img'
        else:
            fol = extension
        
        # check if directory exists
        if not os.path.exists('website//'+fol):
            os.makedirs('website//'+fol)
        
        open('website//'+fol+'//'+fname+'.'+extension, 'wb').write(content.content)


    # URL of the web page you want to extract
    file1 = open('css_files.txt', 'r')
    css = file1.read()
    content1 = (css.split('\n'))

    for link in content1:
        print(link)
        down(link)

    file2 = open('javascript_files.txt', 'r')
    js = file2.read()
    content2 = (js.split('\n'))

    # add .js to the end of each link

    for link in content2:
        print(link)
        down(link)
