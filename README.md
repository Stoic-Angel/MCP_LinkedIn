# MCP LinkedIn Scraper

## ✨ Features

- **Automated LinkedIn Profile Scraping:**
  - Fetches rich profile data (skills, certifications, publications, honors, organizations, courses, projects, and more) for a pre-defined set of users.
  - Uses the official LinkedIn URLs for accuracy.
- **Easy Extensibility:**
  - Add or update target profiles by editing a single Python dictionary.
- **MCP Integration:**
  - Exposes the scraper as an MCP tool for Claude Desktop/Code automation.


---

## 🚀 Getting Started

### 1. **Clone the Repository**
```bash
git clone https://github.com/Stoic-Angel/MCP_LinkedIn
cd MCP\ LinkedIn\ Scraper
```

### 2. **Install Dependencies**
This project requires **Python 3.12**.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
uv pip3 install -r requirements.txt
```

Alternatively, use the dependencies listed in `pyproject.toml`.

### 3. **Set Up Environment Variables**
Create a `.env` file in the project root:

```
x-rapidapi-key=YOUR_RAPIDAPI_KEY
```


### 4. **Configure Target Profiles**
Edit `profile_urls.py` to add or remove LinkedIn profiles. The dictionary maps names to their LinkedIn URLs.

---

## 🛠️ Usage

### Run as an MCP Tool (Recommended)
The scraper is exposed as an MCP tool. You can run it via MCP CLI or through Claude Desktop/Code.


## ⚙️ Configuration
- **API Key:** Set `x-rapidapi-key` in your `.env` file.
- **Profiles:** Edit `profile_urls.py` to target different users.

---

## 📦 Dependencies
- `requests`
- `python-dotenv`
- `linkedin-scraper`
- `mcp[cli]`
- `httpx`

All dependencies are managed via `pyproject.toml` and locked in `uv.lock`
