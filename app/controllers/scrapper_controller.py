from ..services.scrapper_service import scrapperServiceInstance

"""
Created a singleton controller class
This can be extended with methods for parameters or body validation, response formation etc
"""

class ScrapperController:
    __instance = None

    def __init__(self):
        print("calling __init__ method of the singleton class: ScrapperController")
        if ScrapperController.__instance is not None:  
            raise Exception("This class is a singleton!")
        else:
            ScrapperController.__instance = self
      
    @staticmethod
    def get_instance():
        if ScrapperController.__instance is None:
            print("created a new Instance")
            ScrapperController()  
        return ScrapperController.__instance
    
    def postController(self, keyword:str):
        return scrapperServiceInstance.page_crawler(keyword=keyword)
        


scrapperControllerInstance = ScrapperController.get_instance()
