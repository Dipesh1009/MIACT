from bs4 import BeautifulSoup
import requests


def get_oneplus9_specs():
    url = "https://www.oneplus.in/9/specs"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    section_labels = soup.find_all(
        "label",
        class_="params-item-key font-subheading-lg"
    )

    section_values = soup.find_all(
        "div",
        class_="des font-body-md"
    )

    specs = {}

    for label, value in zip(section_labels, section_values):
        key = label.text.strip()
        val = value.text.strip()

        if key in ["MRP", "Performance"]:
            specs[key] = val

    return specs
