from flask import Flask
from flask_restful import Api, Resource
import requests
import bs4

app = Flask(__name__)
api = Api(app)


class Parser:
    titles = []
    hrefs = []
    url = 'https://www.hackerearth.com/challenges/'
    r = requests.get(url)
    not_found = requests.head(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    def parse_title(self):
        title = self.soup.find_all("span", class_="challenge-list-title")
        for t in title:
            self.titles.append(t.text)
        return self.titles

    def parse_hrefs(self):
        href = self.soup.findAll("a", {'class': ['anon-hiring-register-button', 'anon-sprint-register-button',
                                                 'anon-non-hiring-register-button']})
        for h in href:
            self.hrefs.append(h['modal-redirect'])
        return self.hrefs

    def live_contests_count(self):
        return len(self.soup.find_all("div", class_='countdown'))


class Contests(Resource):
    def get(self):
        response = dict()
        parser = Parser()
        hrefs = parser.parse_hrefs()
        titles = parser.parse_title()
        print(titles)
        print(hrefs)
        for i in range(len(hrefs)):
            if "https://www.hackerearth.com" not in hrefs[i]:
                hrefs[i] = "https://www.hackerearth.com" + hrefs[i]
            response[titles[i]] = hrefs[i]
        return response


class Count(Resource):
    def get(self):
        parser = Parser()
        live_count = parser.live_contests_count()
        response = {"live": live_count, "upcoming": (len(parser.parse_hrefs()) - live_count)}
        return response


api.add_resource(Contests, '/contests')
api.add_resource(Count, '/contests/count')

if __name__ == '__main__':
    app.run()
