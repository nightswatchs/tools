#---coding: utf-8---
import feedparser
import codecs

feedlist=[line for line in file('/home/xing/文档/feedlist.txt')]
output = codecs.open('demo.txt','w','utf-8')

for item in feedlist:
    d = feedparser.parse(item)
    for e in d.entries:
        output.write(e.title)
        output.write('\n')
        output.write(e.summary_detail.value)
        output.write('\n')
