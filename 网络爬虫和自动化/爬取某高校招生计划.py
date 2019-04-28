import requests
import re
from bs4 import BeautifulSoup

allUniv = []


def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = 'utf-8'
		return r.text
	except:
		return ""


def fillUnivList(soup):
	data = soup.find_all('tr')
	for tr in data:
		ltd = tr.find_all('td')
		if len(ltd) == 0:
			continue
		singleUniv = []
		for td in ltd:
			singleUniv.append(td.string)
		allUniv.append(singleUniv)


def getUrl():
	url1 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=1'  # 一本院校列表
	url2 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=2'  # 二本院校列表
	url3 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=5'  # 高职(专科)列表
	front = 'http://124.117.250.18/ptjh/y_jhqr/'
	urlList = []
	urlText = getHTMLText(url3)  # 选择抓取的批次
	soupp = BeautifulSoup(urlText, "html.parser")
	for urldata in soupp.find_all('a'):
		urlList.append(front + urldata['href'])
	print(urlList)


getUrl()
# def main(num):
# 	url = 'http://124.117.250.18/ptjh/y_jhqr/g_gbjhyxjh.php?yzdm=01&pcdm=2&yxdh=1052&yxmc=1052上海海关学院'
# 	html = getHTMLText(url)
# 	soup = BeautifulSoup(html, "html.parser")
# 	fillUnivList(soup)
# 	# ls = re.findall()replace( / (^ \s *) | (\s * $) / g, "")
# 	print(allUniv)


# printUnivList(num)

# main(10)
