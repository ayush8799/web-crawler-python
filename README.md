# Web Scrapper 
This is a web scrapper server built using python fastapi and uvicorn.

# Project Structure
1. Entry point is index.py at the root directory. It consists of the server start command using `uvicorn`
2. All the source code is written in `app` directory.
3. Source code is structured into `controllers`, `database`, `middlewares`, `services`, `utils`, and `main.py` file
4. All the files contains the classes for repective jobs with a singleton instance. 
5. `Util` consists of retry mechanism utility to be reused for any api calls.
6. Database consist of Singletone Query class and a json file for storage. (It is for demo purpose only, it can also be extended to a persistent database).

# Endpoint
Endpoint `scrape_data?keyword=laptop` is response for crawling the targetted webpage and extracting the items along with their details and save it to the database `storage.json`. The newly extracted items are appended at the last in the json file. 

# Set Up
1. Create your own virtual environment by running `python3 -m venv .venv`
2. Install all the library dependency mentioned in `requirements.txt` file by running `pip install -r requirements.txt`
3. Now, the server can be started by running `python3 index.py`

# Assumption
The assignment is made assuming
1. Targetted website for crawling is snapdeal.com


