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



profiles_urls = {
  "Vaani Pathariya": "https://www.linkedin.com/in/vaani-pathariya/",
  "Aayush Jain": "https://www.linkedin.com/in/aayush-jain-builds",
  "Rishita Jayant": "https://www.linkedin.com/in/rishita-jayant/",
  "Sparsh Rathore": "https://www.linkedin.com/in/sparsh-rathore/",
  "Shagun Chahar": "https://www.linkedin.com/in/shagun-chahar?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
  "Udbhav Patel": "https://www.linkedin.com/in/thisisudbhavv/",
  "Piyush Gupta": "https://www.linkedin.com/in/piyushg07/",
  "Swapnil Singh": "https://www.linkedin.com/in/hereisSwapnil",
  "Harsh Sharma": "https://www.linkedin.com/in/harshsharma0801?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
  "Aryan Kushwaha": "https://linkedin.com/in/funinkina",
  "Prakhar Sharma": "https://www.linkedin.com/in/sprakhar07/",
  "Anubhav Pal": "https://www.linkedin.com/in/anubhavpal",
  "Bhavya Mittal": "https://www.linkedin.com/in/mittalbhavya1729/",
  "Ojas Mishra": "https://www.linkedin.com/in/ojas-mishra-768982260",
  "Deepanshu Pandey": "https://www.linkedin.com/in/deepanshu-pandey-a16155233/",
  "Om Gupta": "https://www.linkedin.com/in/om-gupta-1219b2223/",
  "Abhishek Sharma": "https://www.linkedin.com/in/abhishek-sharma-2a3764252/",
  "Vedant Goyal": "https://www.linkedin.com/in/vedant-goyal-985a74212/",
  "Shiven Upadhyay": "https://www.linkedin.com/in/nevish302",
  "Ramit Vishwakarma": "https://www.linkedin.com/in/ramitvishwakarma",
  "Ashish Kushwaha": "https://linkedin.com/in/ashishkingdom",
  "Kanak Goel": "https://www.linkedin.com/in/kanakgoel03",
  "Ayush Agrawal": "https://www.linkedin.com/in/its-ayushh-here",
  "Vrishhti Goel": "https://www.linkedin.com/in/vrishhti-goel-58aa1b218?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
  "Shubhransh Bhaskar": "https://www.linkedin.com/in/iamshubhransh/",
  "Yash Tiwari": "https://www.linkedin.com/in/yasharrived"
}



url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

                                      
@mcp.tool()
def scrape(name:str): 
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
