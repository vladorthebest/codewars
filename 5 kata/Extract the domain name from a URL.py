def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    index = list(url)
    index = index.index('.')
    return url[:index]