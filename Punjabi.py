import os
import urllib
import datetime
from bs4 import BeautifulSoup
from urlparse import urlparse, parse_qs

def return_params(query, attribute):
    return query.get(attribute)[0]

f = open('word_list.txt', 'w')



base_url = "http://dsalsrv02.uchicago.edu/cgi-bin/philologic/getobject.pl?p."

for letter in range(0,4):
    for index in range (0,400):
         program_url =  base_url+str(letter)+":"+str(index)+".singh"
         x = urllib.urlopen(program_url).read()
         soup = BeautifulSoup(x)
         span = soup.findAll('div2' , {"type" : "article"})
	 for allspan in span:
               print >> f , allspan.text.encode('utf8')	

f.close()
