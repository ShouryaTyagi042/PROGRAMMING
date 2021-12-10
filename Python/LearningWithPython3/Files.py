import urlib.request as urlib

fh = open("Friends.txt","r")
lines = fh.readlines()
fh.close()
lines.sort()
fh = open("Friends.txt","w")
for i in lines :
    fh.write(i)
fh.close()

def retirieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    socket = urlib.urlopen(url)
    dta =


