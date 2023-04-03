import requests
import json
from bs4 import BeautifulSoup
from task3.const import URL, PARSER
from task3.utils import count_symbols

if __name__ == "__main__":
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, PARSER)

    print(json.dumps(count_symbols(soup.stripped_strings), indent=4, ensure_ascii=False))
