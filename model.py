import requests as r
from bs4 import BeautifulSoup as bs

url = "https://www.ifcg.ru/kb/tnved/search/"



def predict(descript):
    page = r.get(url, params={"q": descript})
    page = bs(page.content, 'lxml')
    if page.find("div", class_="alert-danger"):
        while len(descript.split(" ")) > 0 and page.find("div", class_="alert-danger"):
            descript = " ".join(descript.split(" ")[:-1])
            page = r.get(url, params={"q": descript})
            page = bs(page.content, 'lxml')
    if len(descript) == 0:
        return "Некорректные данные"
    classification = page.find_all("div", class_="clarification")
    if not classification:
        pass
    name = list()
    count = list()
    for i in classification:
        name.append(i.find("span", title="Товарная позиция").text)
        count.append(int(i.find("a").text))
    count = [i / sum(count) * 100 for i in count]
    predict = list()
    if page.find("h2", id="result--tree"):
        if page.find("h2", class_="result--note"):
            for i in page.find("h2", class_="result--note").find_all_previous("div", class_="row row-in mt10"):
                code = i.find("a").text.replace(" ", "")
                if code != "":
                    predict.append(code)
        elif page.find("h2", class_="result--stat"):
            for i in page.find("h2", class_="result--stat").find_all_previous("div", class_="row row-in mt10"):
                code = i.find("a").text.replace(" ", "")
                if code != "" and len(code) == 10:
                    predict.append(code)
    return (name, count), predict

