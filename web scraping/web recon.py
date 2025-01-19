import mechanize
import http.cookiejar
##############                  LEARN HOW TO USE REQUEST MODULE FOR THESE SAME TASKS

# Initialize the 'Browser' class of mechanize
br = mechanize.Browser()
# Use the 'open' method to access a url
# Use the read method to view the source code of an 'opened' url
page = br.open('https://www.useragentstring.com/pages/Chrome/')
source_code = page.read()

print(source_code)



"""     TO MAKE SEARCHES ANONYMOUS:"""
# Use the 'set_proxies' method to set a proxy for a specific site(manual VPN)
# This changes the ip address you access the site with.
# br.set_proxies({'protocol':'protocol://ip_address:port_number'})
'''
br.set_proxies({'http':'http://43.153.208.148:3128'})
'''
# change the user agent also, else some sites may block access
# https://free-proxy-list.net/      -offers free proxies. test the protocols


# The next step would be to alter the user agent header we are recognized by:
# This is important because the mechanize library uses a default user agent
#   which sites block because it is rightfully identified as a robot
# This operation will be done using the 'addheaders' method of mechanize
# Create a recognizable user agent, or get one from: "https://www.useragentstring.com/pages/useragentstring.php"
# It should look like this:
"""
userAgent = [('User-agent','Mozilla/5.0 (X11; U; '+\
'Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01')]
"""
# Alter the user agent with:
'''
br.addheaders = useragent
'''


# The next step would be to delete cookies saved by the scraped website.
# This will be achieved with the 'http.cookiejar' module  -- read on 'http.cookies'
"""
cookiejar = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cookiejar)
"""


