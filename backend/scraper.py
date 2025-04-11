import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import json
from trafilatura import fetch_url, extract, html2txt

def scrape_page(url):
    try:
        raw_data = fetch_url(url)
        text = extract(raw_data)
        return text
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

def scrape_urls_to_files(urls, output_dir="backend/data"):
    file_path = Path('output.json')

    for url in urls:
        content = scrape_page(url)

        if not file_path.exists():
            with open(file_path, mode='w', encoding='utf-8') as f:
                json.dump([], f)

        with open(file_path, "r") as file:
            data = json.load(file)
    
        new_entry = {"url": url, "content": content}
        data.append(new_entry)
    
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    url_list = [
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/gen-template-info/overview.html?tocpath=Messaging%7CTemplates%7CGeneral%20Template%20Information%7C_____1",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/gen-template-info/template-list-page.html?tocpath=Messaging%7CTemplates%7CGeneral%20Template%20Information%7C_____2",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/gen-template-info/track-clicks-google.html?tocpath=Messaging%7CTemplates%7CGeneral%20Template%20Information%7C_____3",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/gen-template-info/accessibility.html?tocpath=Messaging%7CTemplates%7CGeneral%20Template%20Information%7C_____4",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/gen-template-info/img-lib.htm?tocpath=Messaging%7CTemplates%7CGeneral%20Template%20Information%7C_____5",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/overview.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____1",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/template-settings.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____2",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/structures-blocks.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____3",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/emco-modes.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____4",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/personalize-data-feeds.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____5",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/emco-best-prac.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____6",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/google-promo-tab.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____7",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/grow.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____8",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/liveintent-tags.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____9",
        "https://getstarted.meetmarigold.com/engagebysailthru/Content/messaging/email/emco-templates/ai-assistant.html?tocpath=Messaging%7CTemplates%7CEmail%20Composer%20Templates%7C_____10",
    ]
    scrape_urls_to_files(url_list)
