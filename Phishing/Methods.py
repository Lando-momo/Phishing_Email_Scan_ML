def url_from_origin_url(url,domain):
    #url = url.removeprefix("https://").removeprefix("http://").removeprefix("www.")
    parsed_url = urlparse(url)