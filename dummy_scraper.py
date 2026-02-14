from bs4 import BeautifulSoup
import requests


def get_oneplus9_specs():
    url = "https://www.oneplus.in/9/specs"

    response = requests.get(url, timeout=10)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    keys = soup.find_all("label", class_="params-item-key font-body-md")
    values = soup.find_all("div", class_="params-item-value font-body-md")

    specs = {}

    for key, value in zip(keys, values):
        specs[key.text.strip()] = value.text.strip()

    return specs
