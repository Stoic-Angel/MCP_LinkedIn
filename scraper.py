import os
import json
import time
from dotenv import load_dotenv
from linkedin_scraper import Person, actions
from mcp.server.fastmcp import FastMCP
import requests


load_dotenv()
headers = {"x-rapidapi-key": os.getenv('x-rapidapi-key')}



mcp = FastMCP("scraper")


url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

from profile_urls import profiles_urls                          
@mcp.tool()
def scrape(name:str): 
    '''
    Scrapes user data from LinkedIn based on the name. GDG only.
    '''

    print(f"Scraping profile for: {name}")
    linkurl = profiles_urls[name]
    querystring = {
        "linkedin_url": linkurl,
        "include_skills":"true",
        "include_certifications":"true",
        "include_publications":"true",
        "include_honors":"true",
        "include_company_public_url":"true",
        "include_organizations":"true",
        "include_courses":"true",
        "include_projects":"true"
    }
    person = requests.request("GET", url , headers=headers, params= querystring)


    print("\nScraping complete.")
    return person.text

if __name__ == "__main__":
    mcp.run(transport = 'stdio') 
