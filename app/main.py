from fastapi import FastAPI, Request
from .middleware import authMiddleware
from .controllers.scrapper_controller import scrapperControllerInstance

app = FastAPI()

@app.get('/')
def index():  
  return {"message": "Web Crawler Service is running"}


@app.middleware("http")
async def authenticationMiddlewares(request: Request, call_next):
    await authMiddleware.check_token(request)
    return await call_next(request)

"""
Endpoint for scrapping any webpage, 
Input: a keyword to search on the e commerce website, 
Proceessing: The targetted webpage data is crawled and the items and their details are extracted and saved in storage.json
Output: Give users the number of new items extracted and added in storage.json from target page
"""
@app.post('/scrape_data')
async def web_scrapper(keyword:str='electronics'):
  return scrapperControllerInstance.postController(keyword=keyword)

