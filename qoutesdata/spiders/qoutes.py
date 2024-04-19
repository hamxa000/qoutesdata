# import scrapy
# from pathlib import Path
# from pymongo import MongoClient
# import datetime

# client = MongoClient("mongodb+srv://hamxaxyz:123456789$$$@cluster0.gfpaxza.mongodb.net/")
# db = client.scrapy

# def insertTosb(page,saying,author,aboutauthor,tags):
#     collection = db[page]
#     doc = {"saying":saying,"author":author,"aboutauthor":aboutauthor,"tags":tags,
#     "date": datetime.datetime.now(tz=datetime.timezone.utc),
#     }
#     inserted = collection.insert_one(doc).inserted_id
    



# class QoutesSpider(scrapy.Spider):
#     name = "qoutes"
#     allowed_domains = ["toscrape.com"]
#     start_urls = ["https://toscrape.com"]
    
#     def start_requests(self):
        
#         urls = [
#             "https://quotes.toscrape.com/",
#             "https://quotes.toscrape.com/page/2/",
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f"quotes-{page}.html"
#         Path(filename).write_bytes(response.body)
#         # self.log(f"Saved file {filename}")

#         details = response.css(".quote")
#         # print(details)

       

#                                 #   {{{ Lets parse the data in class quote and then store in mongodb}}}

#         cards  = response.css(".quote")
#         for card in cards:
#             saying = card.css("span.text::text").get()
#             print(saying)
#             author = card.css(".author::text").get()
#             print(author)
#             aboutauthor = card.css(".quote a")
#             aboutauthor = aboutauthor.attrib['href']
#             print(aboutauthor) 
#             tags = card.css("div.tags a.tag::text").getall()
#             print(tags)


#             insertTosb(page,saying,author,aboutauthor,tags)

        




















