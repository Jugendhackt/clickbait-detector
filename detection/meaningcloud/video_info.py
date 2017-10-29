#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Created on 28.10.2017

@author: 
'''



class video_info():
	def __init__(self):
		pass

	def get_info_form_url(self,url):
		import urllib2
		response = urllib2.urlopen(url)
		html = response.read()
		#print html
		title_tag2= '">'
		title_tag='<meta itemprop="name" content="'
		title_index= html.find(title_tag)
		title_index2= html[title_index:].find(title_tag2)
		return html[title_index+len(title_tag):title_index2+title_index]



if __name__ == "__main__":
	print "start"
	vid_i=video_info()
	video_title=vid_i.get_info_form_url("https://www.youtube.com/watch?v=GxF6b0rrOug")
	print "video_title",video_title
	print "fertig"
