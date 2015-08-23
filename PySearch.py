import webbrowser
import os

#the beginning urls for three search engines
gUrl = "www.google.com/search?q="
yUrl =  "search.yahoo.com/search?p="
bUrl =  "www.bing.com/search?q="

urls = [gUrl,yUrl,bUrl]

new = 2 # open in new tab if an obtion
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


#x = webbrowser.get('chromium-browser') #make an instance of chromium browser pos add a schoose option
#x.open("www.google.com/search?q=mlb scores ",new=new) # google search uses q =
#x.open("www.bing.com/search?q=mlb scores ",new=new) # bing search uses q =
#x.open("search.yahoo.com/search?p=mlb scores",new=new) # yahoo search uses p =
def goSearch(browser,searchString):
    #take the browser and the search string and serch all engines in urls
    for searcher in urls:
        webbrowser.get(browser).open(searcher + searchString)
if __name__=="__main__":
    AvBrowser = getAvailableBrowser()
    try:
        os.system('clear')
    except:
        pass
    y = 0
    for x in AvBrowser:
        print str(y) + ". " + x
        y = y + 1

    browser = raw_input("please enter the number to your browser: ")
    searchString = raw_input("please input search: ")
    goSearch(AvBrowser[int(browser)],searchString)