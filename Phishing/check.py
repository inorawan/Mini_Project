import requests

def check_url_reputation(url):
    api_key = "8d8fc0c98eab03f059ac4427465a4db1b4cb7c5d"
    endpoint = "https://endpoint.apivoid.com/urlrep/v1/pay-as-you-go/"
    
    params = {
        'key': api_key,
        'url': url
    }
    
    response = requests.get(endpoint, params=params)
    
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        
        # Checking if URL is suspicious based on risk score
        risk_score = data['data']['report']['risk_score']['result']
        if risk_score >= 70:
            print(f"URL: {url} has a high risk score ({risk_score}). It should be blocked.")
        else:
            print(f"URL: {url} has a low risk score ({risk_score}). It is safe to proceed.")
    else:
        print(f"Error occurred while fetching URL reputation for: {url}")

# Read API key from a file 
# with open('api_key.txt', 'r') as f:
#     api_key = f.read().strip()

# Read URLs from a text file
with open('hyperlinks.txt', 'r') as f:
    urls = f.readlines()

urls = [url.strip() for url in urls]

for url in urls:
    check_url_reputation(url)
