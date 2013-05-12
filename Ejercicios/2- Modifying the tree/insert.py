# -*- coding: iso-8859-15 -*-
from bs4 import BeautifulSoup

'''

insert_before() a certain tag or element
 insert_after() same as above
insert() at the end of the parent's contents

'''

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
    
tag = soup.a
print tag.text
print tag.string
tag.string = "New link text."
