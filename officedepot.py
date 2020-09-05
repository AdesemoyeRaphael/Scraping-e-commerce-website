import scrapy
# from scrapy.crawler import CrawlerProcess
import pandas as pd
import numpy as np
import re

# FIRST PROCESS: Getting all the pens,pencils and markers from the website saving it as links.csv


# class dw(scrapy.Spider):
# 	name = 'dw'
# 	start_urls = ['https://www.officedepot.com/a/browse/pens-pencils-and-markers/N=5+4367&viewAllSkus=true&recordsPerPageNumber=24&No=0/']
# 	page_no = 24

# 	def parse(self,response):

# 		link = response.css("div.desc_text a::attr(href)").extract()

# 		yield{'Links':link}


# 		next_page = 'https://www.officedepot.com/a/browse/pens-pencils-and-markers/N=5+4367&viewAllSkus=true&recordsPerPageNumber=24&No='+ str(dw.page_no) + '/'
# 		if dw.page_no < 3073:
# 			dw.page_no += 24

# 			yield response.follow(next_page, callback=self.parse)






# STEP2: Extracting the product name, price and details saving it to scrapyresult.csv

# data = pd.read_csv("links.csv")
# # print(data)

# ball =[]
# for x in data['Links']:
# 	x = x.split(",")
# 	# ball.append(x[0])
# 	# x=x[0].split(',')
# 	for y in x:
# 		y = y.split(";")
# 		ball.append(y[0])
# l=len(ball)
# # print(l)

# # print(ball[1644])
# # print(ball)


# class dw(scrapy.Spider):
# 	name = 'dw'
# 	page = ball
# 	start_urls = ['https://www.officedepot.com/a/products/200879/Sharpie-Fine-Point-Retractable-Markers-Fine/']
# 	# products_details =[]
# 	x = 1645
# 	p = 0

# 	def parse(self,response):

# 		name = response.css(".fn::text").extract()
# 		try:
# 			price = response.css(".lg .right::text").extract()
# 			if price == []:
# 				price = response.css(".border_bottom .red_price .right::text").extract()
# 			elif price ==[]:
# 				price = response.css(".red_price .right::text").extract()
# 			elif price ==[]:
# 				price = response.css(".right::text").extract()
# 		except AttributeError:
# 			price = np.nan
# 		# table = response.css('table.data tabDetails gw9').extract()
# 		# div = response.css("div.sku_det tbody tr td::text").extract()
# 		products_details =[]
# 		for row in response.css("div.sku_det tbody tr"):
# 			key = row.css("td::text")[0].extract()
# 			value = row.css("td::text")[1].extract()
# 			details = key + ':' + value
# 			products_details.append(details)
			


# 		yield { 'Name':name,
# 				'Price':price,
# 				'Product Details':products_details}

# 		next_page = 'https://www.officedepot.com'+dw.page[dw.x]
# 		if dw.x < l :
# 			dw.x +=1
# 			yield response.follow(next_page, callback=self.parse)


# # process = CrawlerProcess({
# # 	'DOWNLOADER_MIDDLEWARES': {
# #    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
# #    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,}

# # 	})

# # process.crawl(dw)
# # process.start()








#Step 3: Cleaning the extracted datas to make it readable in the csv file and saving it as Pens_Pencils_Markers.csv

# data = pd.read_csv('fe.csv')

# name =[]
# for x in data['Name']:
# 	x = x.strip()
# 	x = re.sub('\s+','' ,x)
# 	name.append(x)
# # print(name)
# def rewrite(text,there=re.compile(re.escape(', ')+'*')):
# 	return there.sub(' ',text)

# names=[]
# for x in name:
# 	b=rewrite(x)
# 	b=b.strip()
# 	names.append(b)
# # print(names)
# # print(names)

# data['Name'] = names

# # key =[]
# # # print(data['key'])
# # for y in data['key']:
# # 	y = y.replace("#","")
# # 	# y = y.replace("Item","UPCs")
# # 	y = y.strip()
# # 	key.append(y)

# # data['key'] = key
# # # print(data['key'])

# review =[]
# for x in data['Product Details']:
# 	try:
# 		x = x.replace("#","")
# 		try:
# 			x = re.sub('\s+',' ',x)
# 		except TypeError:
# 			x='(0)'

# 		review.append(x)
# 	except AttributeError:
# 		review.append(x)

# # print(review)

# def rewrite(text,there=re.compile(re.escape(', , , , , , , , , , ')+'*')):
# 	return there.sub('',text)
# review1=[]
# for x in review:
# 	b=rewrite(str(x))
# 	b=b.strip()
# 	review1.append(b)
# # print(review1)

# data['Product Details'] = review1

# print(data['Product Details'])

# data.to_csv('fee.csv',index=False)
# # print(review1)







data = pd.read_csv('fe.csv')
# print(data)

data2 = pd.read_csv("scrapyresult.csv")
# print(data2)


df = pd.concat([data,data2],ignore_index= True)
print(df)

df.to_csv("scrapy.csv",index=False)




















# class dw(scrapy.Spider):
# 	name = 'dw'
# 	page = ball
# 	start_urls = ['https://www.officedepot.com/a/products/203349/Sharpie-Fine-Point-Permanent-Markers-Gray/']
# 	Key =[]
# 	Value = []
# 	x = 1
# 	p = 0

# 	def parse(self,response):

# 		name = response.css(".fn::text").extract()
# 		try:
# 			price = response.css(".lg .right::text").extract()
# 			if price == []:
# 				price = response.css(".border_bottom .red_price .right::text").extract()
# 			elif price ==[]:
# 				price = response.css(".red_price .right::text").extract()
# 		except AttributeError:
# 			price = np.nan
# 		# table = response.css('table.data tabDetails gw9').extract()
# 		# div = response.css("div.sku_det tbody tr td::text").extract()
# 		for row in response.css("div.sku_det tbody tr"):
# 			key = row.css("td::text")[0].extract()
# 			dw.Key.append(key)
# 			value = row.css("td::text")[1].extract()
# 			dw.Value.append(value)


# 		yield { 'Name':name,
# 				'Price':price,
# 				'key':dw.Key,
# 				'value':dw.Value}

# 		next_page = 'https://www.officedepot.com'+dw.page[dw.x]
# 		if dw.x < l :
# 			dw.x +=1
# 			yield response.follow(next_page, callback=self.parse)


# data = pd.read_csv('scrapyresult.csv')

# name =[]
# for x in data['Name']:
# 	x = x.strip()
# 	x = re.sub('\s+','' ,x)
# 	name.append(x)
# # print(name)
# def rewrite(text,there=re.compile(re.escape(', ')+'*')):
# 	return there.sub(' ',text)

# names=[]
# for x in name:
# 	b=rewrite(x)
# 	b=b.strip()
# 	names.append(b)
# # print(names)

# data['Name'] = name

# key =[]
# # print(data['key'])
# for y in data['key']:
# 	y = y.replace("#","")
# 	# y = y.replace("Item","UPCs")
# 	y = y.strip()
# 	key.append(y)

# data['key'] = key
# # print(data['key'])

# review =[]
# for x in data['value']:
# 	try:
# 		x = re.sub('\s+',' ',x)
# 	except TypeError:
# 		x='(0)'

# 	review.append(x)

# def rewrite(text,there=re.compile(re.escape(', , , , , , , , , , ')+'*')):
# 	return there.sub('',text)
# review1=[]
# for x in review:
# 	b=rewrite(x)
# 	b=b.strip()
# 	review1.append(b)
# # print(review1)

# data['value'] = review1
# # print(data['value'].T)

# df1 = data.assign(Product_details_Value=data.value.str.split(","),key=data.key.str.split(",")).explode('Product_details_Value')
# df2 = data.assign(Product_details_Key=data.key.str.split(","),key=data.key.str.split(",")).explode('Product_details_Key')
# # print(df1)

# # print(df2)

# df1['key'] = df2['Product_details_Key']

# df1['Product_details_Key'] = df1['key']

# # print(df1['key'])

# df1 = df1.drop('value',1)
# df1 = df1.drop('key',1)

# df1 = df1[['Name','Price','Product_details_Key','Product_details_Value']]
# print('df1')

# df1.to_csv('Result1.csv',index=False)