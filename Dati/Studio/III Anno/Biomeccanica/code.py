from BeautifulSoup import BeautifulSoup, Tag
import re

# Read the raw file into raw
f = open("BoP - APV - taggeds.html")
raw = f.read()
print '[*] Read raw text in'

# Construct a BeautifulSoup out of the raw HTML
soup = BeautifulSoup(raw)
print '[*] Constructed BeautifulSoup'

# Holds all our individual pages
pages = []

# Pull out all the text (with tags) between HR tags, which
# delineate the pages in the document
tag = soup.find("hr")

def textTillNextPage(t):
    s = ""
    while t != None and not (isinstance(t, Tag) and t.name == 'hr'):
        s += str(t)
        t = t.nextSibling
    return t, s

# Loop through the document until the end, and pull out each page
t = tag.nextSibling
while not (t == None):
    t, s = textTillNextPage(t)
    pages.append(s)
    if t != None:
        t = t.nextSibling

print '[*] Separated all the pages out'

#Create the relevant Regular Expressions
r = re.compile(r'PSALM&nbsp;([0-9]+)', re.I)
r2 = re.compile(ur"[#\xc5\xc3]", re.I)

def getTextOffPage(n):
    s = BeautifulSoup(pages[n])
    t = s.first()
    while t != None and not r.search(str(t)):
        t = t.nextSibling
    if t is None:
        return None, ''
    psalmNum = r.search(str(t)).groups()[0]
    p = BeautifulSoup()
    while t != None:
        nxt = t.nextSibling
        if not r2.search(str(t)):
            p.append(t)
        else:
            t = nxt
            while t != None and (r2.search(str(t)) or (isinstance(t, Tag) and t.name == 'br')):
                t = t.nextSibling
            nxt = t
        t = nxt
    return p, psalmNum

pageNum = 10
psalm = 1
while pageNum < 368:
    thisPsalm, psalm = getTextOffPage(pageNum)
    if psalm == None:
        pageNum = pageNum + 1
        continue
    pageNum = pageNum + 1
    nextPsalm = psalm
    while nextPsalm == psalm:
        nextPage, nextPsalm = getTextOffPage(pageNum)
        if nextPsalm == psalm:
            nextPage.first().extract() #Removes the title from the top of the page
            thisPsalm.append(nextPage)
            pageNum = pageNum + 1
    f = open('pages/psalm ' + psalm + '.html', 'w')
    f.write(str(thisPsalm))
    f.close()
    print '[*] Psalm ' + psalm
