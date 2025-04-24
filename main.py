from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import json
import os
import httpx
from bs4 import BeautifulSoup

load_dotenv()   

mcp = FastMCP("docs")

USER_AGENT = "docs-app/1.0"
SERPER_URL = "https://google.serper.dev/search"

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


async def search_web(query: str) -> dict |  None:
    payload = json.dumps({"q": query, "num": 2})

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SERPER_URL, headers=headers, data=payload, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            return {"organic": []}

async def fetch_url(url: str):
  async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Timeout error" 

@mcp.tool()
async def get_info(query: str, name: str):
    '''
    Reads the requested profile and answers questions accordingly.

    Args:
        query - the question itself
        name - the GDG member it concerns
    '''
    if name not in profiles_urls:
        return "Person not found"
    
    query = f"site:{profiles_urls[name]} {query}"
    results = await search_web(query)

    if not results or not results["organic"]:
        return "No results found"
    
    text = ""
    for result in results["organic"]:
        text += await fetch_url(result['link'])
    return text
    

if __name__ == "__main__":
    mcp.run(transport="stdio")
