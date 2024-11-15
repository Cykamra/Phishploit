# Phishing URL Masking Tool

## Disclaimer

This tool is intended for **educational and research purposes only**. The creator, **Cykamra**, does not take responsibility for any misuse of this tool. Phishing is **illegal and unethical**. Always act responsibly and ensure your activities are lawful. The use of this tool to deceive or harm others is strongly discouraged.

## Overview
This tool allows you to craft a disguised URL that hides the original phishing link. It works by shortening the provided URL and masking it with a legitimate domain, making it look more convincing for social engineering purposes. This is just a simple automation tool for generating these disguised URLs.

## Features
- **URL Shortening**: Shortens a given URL to make it look less suspicious.
- **Domain Masking**: Allows you to mask the phishing URL with any legitimate domain of your choice (e.g., `https://google.com`).
- **Social Engineering Word Insertion**: Adds enticing words (such as `get-free-bitcoins` or `get-1million-followers-instantly`) to the URL for further deception.

## How It Works
1. **URL Validation**: The tool checks that the URL provided is in a valid format (starting with `http` or `https`).
2. **URL Shortening**: The tool shortens the provided phishing URL using a URL shortening service (`is.gd`).
3. **Domain Masking**: You can mask the shortened URL with any legitimate domain you choose (e.g., `https://google.com`).
4. **Social Engineering**: The tool allows you to add words to the URL to make it look more enticing and legitimate, improving the chances of tricking the target.

## Usage Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Cykamra/Phishploit.git
   cd phishploit 

