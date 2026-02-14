from bs4 import BeautifulSoup
import requests


def get_oneplus9_specs():
    url = "https://www.oneplus.in/9/specs"

    response = requests.get(url, timeout=10)
    response.encoding = response.apparent_encoding

    print("STATUS:", response.status_code)
    print("LENGTH:", len(response.text))
    
    soup = BeautifulSoup(response.text, "html.parser")

    keys = soup.find_all("label")
    print("LABEL COUNT:", len(keys))

    return {}
