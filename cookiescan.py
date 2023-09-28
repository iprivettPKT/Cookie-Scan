from playwright.sync_api import sync_playwright
from datetime import datetime

# ANSI Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"

def colored(text, color_code):
    return color_code + text + ENDC

def fetch_cookies_with_playwright(domain):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # Using a persistent context to mimic regular browser more closely
        context = browser.new_context(storage_state={})

        page = context.new_page()

        # Capture network responses for set-cookie headers
        def check_for_set_cookie(response):
            headers = response.headers
            if "set-cookie" in headers:
                # This means a cookie was set during this response
                pass  # Logic to handle this if necessary

        page.on("response", check_for_set_cookie)

        if not domain.startswith(('http://', 'https://')):
            domain = 'https://' + domain

        page.goto(domain, wait_until="networkidle")
        
        # Let's wait a bit more
        page.wait_for_timeout(1000)  # wait for 1 second

        # Simulate some user interactions (these are just examples, adapt as needed)
        page.press('body', 'PageDown') # Simulate a page scroll
        page.wait_for_timeout(1000)  # wait for 1 second after scroll

        cookies = context.cookies()
        browser.close()
        return cookies




def format_expiry(timestamp):
    if timestamp is None:
        return "Session"
    expiry_date = datetime.fromtimestamp(timestamp)
    if expiry_date < datetime.now():
        return "Session"
    return expiry_date.strftime('%Y-%m-%d %H:%M:%S')

def main():
    # Print ASCII Art
    print("""
  ______   ______     ______    __  ___  __   _______         _______.  ______     ___      .__   __. 
 /      | /  __  \   /  __  \  |  |/  / |  | |   ____|       /       | /      |   /   \     |  \ |  | 
|  ,----'|  |  |  | |  |  |  | |  '  /  |  | |  |__         |   (----`|  ,----'  /  ^  \    |   \|  | 
|  |     |  |  |  | |  |  |  | |    <   |  | |   __|         \   \    |  |      /  /_\  \   |  . `  | 
|  `----.|  `--'  | |  `--'  | |  .  \  |  | |  |____    .----)   |   |  `----./  _____  \  |  |\   | 
 \______| \______/   \______/  |__|\__\ |__| |_______|   |_______/     \______/__/     \__\ |__| \__| 
                                                                                                      
Developed by: Isaac Privett
Requires: playwright and datetime python libraries
   """)
    
    with open('domains.txt', 'r') as f:
        domains = [line.strip() for line in f.readlines() if line.strip()]

    # Print header
    print("+--------------------------------+----------------------+----------+----------+---------------------------+")
    print("| Domain                         | Cookie Name          |  Secure  | HttpOnly | Expiry                    |")
    print("+--------------------------------+----------------------+----------+----------+---------------------------+")

    for domain in domains:
        print(f"+---------------------------------------------------------------------------------------------------------+")
        print(f"| Processing domain: {colored(domain, GREEN):93} |")
        print(f"+--------------------------------+----------------------+----------+----------+---------------------------+")
        cookies = fetch_cookies_with_playwright(domain)
        for cookie in cookies:
            name = cookie.get("name")[:20]
            secure = colored("Yes".center(8), GREEN) if cookie.get("secure", False) else colored("No".center(8), RED)
            http_only = colored("Yes".center(8), GREEN) if cookie.get("httpOnly", False) else colored("No".center(8), RED)
            expires = str(format_expiry(cookie.get("expires"))).center(24)

            print(f"| {'':30} | {name:20} | {secure:^10} | {http_only:^10} | {expires:24} |")
        print("+--------------------------------+----------------------+----------+----------+--------------------------+")

    print("+--------------------------------+----------------------+----------+----------+--------------------------+")

if __name__ == "__main__":
    main()
