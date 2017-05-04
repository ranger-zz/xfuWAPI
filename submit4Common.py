#!/usr/bin/python
#-*-coding:UTF-8-*-
import urllib,urllib2

file_path = raw_input("please input the file path:")
fo = open(file_path,"r")
line = fo.readline().strip()
#line = unicode(line,"gbk")
url = line
print(url)
line = fo.readline().strip()
i = 1;
while line:
    print (line)
    body_value = {}
    params = line.split(',')
    for parampare in params:
        #print (parampare)
        pp = parampare.split(':')
        key = pp[0]
        value = pp[1]
        #print(key)
        #print(value)
        body_value[key] = value
    body_value  = urllib.urlencode(body_value)
    request = urllib2.Request(url, body_value)
    print (request)
    result = urllib2.urlopen(request ).read()
    print (result)
    print ("\n")
    wi = "%d" % i
    fw = open("result","w")
    fw.write(wi)
    fw.close()
    i = i + 1
    line = fo.readline().strip()
    #line = unicode(line,"gbk")

fo.close()