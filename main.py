import requests
from bs4 import BeautifulSoup, Tag
import sys


TR_CLASS = "chartlist-row"  
BASE_URL = "https://www.last.fm"

def main(user):
    url = f"{BASE_URL}/user/{user}/library/artists?page=1"
    response = requests.get(url)
    response.raise_for_status()  

    soup = BeautifulSoup(response.text, "html.parser")


    tr_elements = soup.find_all("tr", class_=TR_CLASS)

    i = 1
    for tr in tr_elements:
        if isinstance(tr, Tag):  
            a_tags = tr.find_all("a", href=True)
            a = a_tags[1]
            a_scrobbles = a_tags[4]
            if a['href']:
                place = get_listeners_place(a['href'], user)
                if place:
                    print(f"Artist: {a['title']}")
                    print(f"Rank: {i} | {extract_scrobbles(a_scrobbles)}")
                    print(f"Place: {place}")
                    print("-" * 40)
        i += 1

def extract_scrobbles(soup):
    span = soup.find("span", attrs={"data-stat-value": True})
    if span:
        return span["data-stat-value"]
    return None

def get_listeners_place(url, user):
    response = requests.get(BASE_URL + url + "/+listeners")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    element = soup.find_all("ol", class_="top-listeners")[0]

    return get_user_place(element, user)


def get_user_place(soup, username):
    items = soup.find_all("li", class_="top-listeners-item-wrap")
    place = 1
    for item in items:
        h3 = item.find("h3", class_="top-listeners-item-name")
        if not h3:
            continue
        a = h3.find("a", class_="link-block-target")
        if not a:
            continue
        user = a.get_text(strip=True)
        if user.lower() == username.lower():
            return place
        place += 1
    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <lastfm_username>")
        sys.exit(1)
    main(sys.argv[1])
