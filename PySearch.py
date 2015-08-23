__author__ = 'randy'

import webbrowser
new = 2 # open in new tab if an obtion
x = webbrowser.get('chromium-browser')
x.open("www.google.com/search?q=mlb scores ",new=new)


print "test"