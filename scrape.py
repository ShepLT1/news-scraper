import requests
from bs4 import BeautifulSoup
import pprint
import sys


def main(pages):
    hnList = []
    url = "https://news.ycombinator.com/news"
    for num in range(int(pages)):
        if num > 0:
            url += f"?p={str(num + 1)}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.select(".titleline > a")
        subtext = soup.select(".subtext")
        hnList += create_custom_hn(links, subtext)
    return sort_stories_by_votes(hnList)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href")
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return hn


if __name__ == "__main__":
    sys.exit(pprint.pprint(main(sys.argv[1])))
