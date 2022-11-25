import webbrowser
url="http://www.baidu.com/"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"))
webbrowser.get('firefox').open(url)
