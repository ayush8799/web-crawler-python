from bs4 import BeautifulSoup as Soup
from typing import Any
from ..utils.retryRequestUtil import retry_requests
from ..database.queries import db_query_instance

"""
Created a singleton service class
This is extended and divided into service processing methods
"""

class ScrapperService:
    __instance = None

    __base_url: str = ''  

    def __init__(self):
        print("calling __init__ method of the singleton class: ScrapperService")
        if ScrapperService.__instance is not None:  
            raise Exception("This class is a singleton!")
        else:
            ScrapperService.__instance = self
            ScrapperService.__base_url = 'https://www.snapdeal.com' # scrapping data from snapdeal.com

    def __extractData(self, keyword: str, ) -> dict[Any]:
      try:
        full_url=f'{self.__base_url}/search?keyword={keyword}'
        response = self.__scrape_url(full_url)
        if not response:
          print(response)
          raise Exception('Error in scrapping the link', response)
        html = Soup(response.content, 'html.parser')
        sections = html.find_all('div', {'class': 'product-tuple-listing'})
        data = []
        for (index, section) in enumerate(sections):
          image = section.find('img', {'class': 'product-image'})
          price = section.find('span', {'class': 'product-price'})
          title = section.find('p', {'class': 'product-title'})
          image_url = image.get('src') or image.get('data-src')
          data.append({ 'tag': keyword, 'title': title.text, "image": image_url, 'price': price.text})

        return data
      except Exception as e:
        return e
      
    def __scrape_url(self,url: str):
      try:
        session = retry_requests(3, 0.5)
        response = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'})
        print('scrape response :: ', response)
        return response
      except Exception as e:
        print(f'Error :: scrape_url : {e}')
        return e

    @staticmethod
    def get_instance():
        if ScrapperService.__instance is None:
            print("created a new Instance")
            ScrapperService()  
        return ScrapperService.__instance

    def page_crawler(self, keyword:str):
        print("calling page_crawler method of the singleton class")
        try: 
          data = self.__extractData(keyword)
          if not data:
            raise Exception(data)
          if data and len(data):
            print('Saving Data generated ')
            db_query_instance.save_data_to_json(data)
          else: 
            print("No Data Found")
          return {'result': 'success', 'message': f'added {len(data)} new records for searchKey {keyword}'}
        except Exception as e:
          print('Error :: route:/extractData :: ', e)
          return e


scrapperServiceInstance = ScrapperService.get_instance()
