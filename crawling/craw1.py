import requests
from bs4 import BeautifulSoup
import re

# using BeautifulSoup HTML parser

class WebCrawling:
    def __init__(self, url):
        self.url = url

    def doHtmlCrawling(self):
        self.webpage = requests.get(self.url)
        self.soup = BeautifulSoup(self.webpage.content, "html.parser")

        print(self.soup)

    def print_Ptag(self):
        print("______P tag______")
        print(self.soup.p)
        print(self.soup.p.string)

    def print_H1tag(self):
        print("______H1 tag______")
        print(self.soup.h1)

    def print_ULtag_children_list(self):
        print("______UL children list tag______")
        for item in self.soup.ul.children:
            print(item)

    def print_ULtag_parent_list(self):
        print("______UL parent list tag______")
        for item in self.soup.ul.parents:
            print(item)

    def print_DIVtag_children_list(self):
        print("______DIV children list tag______")
        for item in self.soup.div.children:
            print(item)

#find_all
    def find_tag(self, tag):
        print("______find_all list tag______")
        print(type(self.soup.find_all(tag)))
        for item in self.soup.find_all(tag):
            print(item)

    def find_OL_and_UL_tag(self):
        print("______find_all ol and ul list tag______")
        for item in self.soup.find_all(re.compile("[ou]l")):
            print(item)

    def find_HXtag(self):
        print("______find_all HX list tag______")
        for item in self.soup.find_all(re.compile("h[1-9]")):
            print(item)

    def find_attr1(self, attrVal):
        print("______find_all attr______")
        for item in self.soup.find_all(attrs=attrVal):
            print(item)

# read from css
    def find_from_CSSClass(self):
        print("______find_all CSS Class______")
        print(self.soup.select(".card-region-name"))


if __name__ == "__main__":
    webC = WebCrawling("https://www.daangn.com/hot_articles")
    webC.doHtmlCrawling()

    webC.print_Ptag()
    webC.print_H1tag()
    webC.print_ULtag_children_list()
    webC.print_ULtag_parent_list()
    webC.print_DIVtag_children_list()

    webC.find_tag("h2")
    webC.find_OL_and_UL_tag()
    webC.find_HXtag()

    webC.find_attr1({'class':'card-title'})

    webC.find_from_CSSClass()



