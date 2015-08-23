__author__ = 'randy'

import webbrowser


def getAvailableBrowser():
    #using the browsers in webbwoser determine which ones are availabe on the system
    posBrowser = ['mozilla','firefox','netscape','galeon','epiphany','skipstone','kfmclient',
              'konqueror','kfm','mosaic','opera','grail','links','elinks','lynx','w3m',
              'windows-default','macosx''safari','google-chrome','chrome','chromium','chromium-browser']

    availableBrowsers = []
    for x in posBrowser:
        try:
            webbrowser.get(x)
            availableBrowsers.append(x)
        except:
            pass
    return availableBrowsers
new = 2 # open in new tab if an obtion
#x = webbrowser.get('chromium-browser') #make an instance of chromium browser pos add a schoose option
#x.open("www.google.com/search?q=mlb scores ",new=new) # google search uses q =

#x.open("search.yahoo.com/search?p=mlb scores",new=new) # yahoo search uses p =

AvBrowser = getAvailableBrowser()

print AvBrowser