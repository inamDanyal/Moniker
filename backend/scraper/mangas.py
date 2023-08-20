from bs4 import BeautifulSoup
import requests

class GetMangas:
    def __init__(self):
        self.URLs = {
            "tcb" : "https://tcbscans.com"
        }
        self.mangaList = []
        self.mangaLinks = {}

    def getMangaList(self):
        """
        A function that will get the list of Mangas that are available to download and the links to each mangas
        chapter list
        :return:
        """

        # The URL thats being scraped
        mangaURL_one = f"{self.URLs['tcb']}/projects"

        # Getting the html of the page
        response = requests.get(mangaURL_one)
        soup = BeautifulSoup(response.content, "html.parser")

        # Searching the html for the manga titles
        for i in soup.select(
            "div.overflow-hidden > div.container > div.grid > div > div.bg-card > div.flex > div.flex-auto > div.flex > a"):
            self.mangaList.append(i.string)
            self.mangaLinks[i.string] = f"{self.URLs['tcb']}{i.get('href')}"