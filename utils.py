import re
import requests

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_business_email(email):
    free_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
    domain = email.split('@')[-1]
    return domain not in free_domains

def is_website_live(url):
    # If URL missing scheme, prepend
    if not url.lower().startswith(("http://", "https://")):
        url = "http://" + url
    try:
        resp = requests.get(url, timeout=5)
        # consider any 2xx or 3xx as “live”
        return 200 <= resp.status_code < 400
    except:
        return False

def has_linkedin(link):
    return isinstance(link, str) and "linkedin.com" in link.lower()

def calculate_score(row):
    score = 0
    if row['Valid Email']:
        score += 25
    if row['Business Email']:
        score += 25
    if row['Website Live']:
        score += 25
    if row['LinkedIn Present']:
        score += 25
    return score
