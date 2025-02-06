import requests
from selectolax.parser import HTMLParser
def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None





def extract_main_content(html):
    tree = HTMLParser(html)
    
    # Remove non-content elements
    for tag in tree.css('script, style, nav, footer, header, aside'):
        tag.decompose()
    
    # Focus on content-rich elements
    content = []
    for node in tree.css('article, main, .content, p, div[itemprop="articleBody"]'):
        content.append(node.text(separator='\n'))
    
    return '\n\n'.join(content)

def get_content(url):
    html=get_html(url)
    if html==None:
        return None
    return extract_main_content(html)

