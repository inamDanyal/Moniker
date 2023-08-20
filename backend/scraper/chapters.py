from bs4 import BeautifulSoup
import requests
from mangas import GetMangas


class Chapters(GetMangas):

    def __init__(self):
        super().__init__()

    def getChapters(self, manga):
        """
        A function that will retreive the number of chapters a manga has
        :param manga: The manga thats been selected for download
        :return:
        """

        chapters = {}
        chapters[manga] = {}

        temp_chap = []

        # Getting the chapters page
        response = requests.get(self.mangaLinks[manga])
        soup = BeautifulSoup(response.content, "html.parser")

        # Searching the chapters page for the elemement that contains the link to the chapters
        selection = soup.select(
            "div.overflow-hidden > div.container > div.grid > div.col-span-2 > a"
        )

        # Putting all the links into a list
        for i in selection:
            temp_chap.append(f"{self.URLs['tcb']}{i.get('href')}")

        # reversing the list
        temp_chap = temp_chap[::-1]

        x = 0
        for i in range(len(temp_chap)):
            x += 1
            chapters[manga][x] = temp_chap[x - 1]

        print(chapters)


    def downloadChapters(self, manga : str, chapters : list):
        """
        A funtion that will download the selected manga
        :param manga: The manga thats been selected for download
        :param chapters: The chapters that've been selected for download
        :return: None
        """