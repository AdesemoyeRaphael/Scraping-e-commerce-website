import scrapy
import pandas as pd
import numpy as np
import re

# STEP 1: Getting all the pens,pencils and markers from the website saving it as links.csv


class dw(scrapy.Spider):
	name = 'dw'
	start_urls = ['https://www.officedepot.com/a/browse/pens-pencils-and-markers/N=5+4367&viewAllSkus=true&recordsPerPageNumber=24&No=0/']
	page_no = 24

	def parse(self,response):

		link = response.css("div.desc_text a::attr(href)").extract()

		yield{'Links':link}


		next_page = 'https://www.officedepot.com/a/browse/pens-pencils-and-markers/N=5+4367&viewAllSkus=true&recordsPerPageNumber=24&No='+ str(dw.page_no) + '/'
		if dw.page_no < 3073:
			dw.page_no += 24

			yield response.follow(next_page, callback=self.parse)






# STEP 2: Extracting the product name, price and details saving it to scrapyresult.csv

data = pd.read_csv("links.csv")
# print(data)

ball =[]
for x in data['Links']:
	x = x.split(",")
	for y in x:
		y = y.split(";")
		ball.append(y[0])
l=len(ball)



class dw(scrapy.Spider):
	name = 'dw'
	page = ball
	start_urls = ['https://www.officedepot.com/a/products/200879/Sharpie-Fine-Point-Retractable-Markers-Fine/']
	x = 1645
	p = 0

	def parse(self,response):

		name = response.css(".fn::text").extract()
		try:
			price = response.css(".lg .right::text").extract()
			if price == []:
				price = response.css(".border_bottom .red_price .right::text").extract()
			elif price ==[]:
				price = response.css(".red_price .right::text").extract()
			elif price ==[]:
				price = response.css(".right::text").extract()
		except AttributeError:
			price = np.nan
			
		products_details =[]
		for row in response.css("div.sku_det tbody tr"):
			key = row.css("td::text")[0].extract()
			value = row.css("td::text")[1].extract()
			details = key + ':' + value
			products_details.append(details)
			


		yield { 'Name':name,
			'Price':price,
			'Product Details':products_details}

		next_page = 'https://www.officedepot.com'+dw.page[dw.x]
		if dw.x < l :
			dw.x +=1
			yield response.follow(next_page, callback=self.parse)










#Step 3: Cleaning the extracted datas to make it readable in the csv file and saving it as Pens_Pencils_Markers.csv

data = pd.read_csv('scrapyresult.csv')

name =[]
for x in data['Name']:
	x = x.strip()
	x = re.sub('\s+','' ,x)
	name.append(x)
# print(name)
def rewrite(text,there=re.compile(re.escape(', ')+'*')):
	return there.sub(' ',text)

names=[]
for x in name:
	b=rewrite(x)
	b=b.strip()
	names.append(b)
# print(names)
data['Name'] = names



review =[]
for x in data['Product Details']:
	try:
		x = x.replace("#","")
		try:
			x = re.sub('\s+',' ',x)
		except TypeError:
			x='(0)'

		review.append(x)
	except AttributeError:
		review.append(x)

# # print(review)

def rewrite(text,there=re.compile(re.escape(', , , , , , , , , , ')+'*')):
	return there.sub('',text)
review1=[]
for x in review:
	b=rewrite(str(x))
	b=b.strip()
	review1.append(b)
# print(review1)

data['Product Details'] = review1

# print(data['Product Details'])

data.to_csv('Pens_Pencils_Markers.csv',index=False)

