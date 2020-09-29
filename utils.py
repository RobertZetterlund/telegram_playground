from urllib.request import urlopen


def getHtmlFromURL(url):
    page = urlopen(url)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")