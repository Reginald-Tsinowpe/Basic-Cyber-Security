# An anonymous object-oriented web scraper with the mechanize library


import mechanize
from http.cookiejar import LWPCookieJar


class AnonymousBrowser():
    def __init__(self, url, user_agent, proxies):
        self.site_url = url
        self.browser_useragent = user_agent
        self.browser_proxies = proxies

        self.cookies = LWPCookieJar()
        self.br = mechanize.Browser()
        self.Change_userAgent()
        self.Change_proxies()
        self.Clear_cookies()
        self.Open_url()


    def Open_url(self):
        opened = self.br.open(self.site_url)
        opened.read()
        print(self.cookies)
        print('working')

    def Change_userAgent(self):
        self.br.addheaders = self.browser_useragent


    def Change_proxies(self):
        self.br.set_proxies(self.browser_proxies)

    def Clear_cookies(self):
        self.br.set_cookiejar(self.cookies)





man_user_agent = [('User-agent', "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/41.0.2226.0 Safari/537.36")]
man_proxy = ({'http':'http://217.112.80.252:80'})

br = AnonymousBrowser("http://www.youtube.com", man_user_agent, man_proxy)
