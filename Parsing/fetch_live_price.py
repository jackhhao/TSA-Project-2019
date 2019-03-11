import requests
import lxml.html

def getData(code):
    print(code)
    html = requests.get('https://finance.yahoo.com/quote/' + code + "/")
    doc = lxml.html.fromstring(html.content)

    new_releases = doc.xpath('//div[@class="My(6px) Pos(r) smartphone_Mt(6px)"]')[0]
    print(new_releases.text_content())

    data = [new_releases.text_content()[0:new_releases.text_content().index(".")+3],new_releases.text_content()[new_releases.text_content().index(".")+3:]]
    data.extend(data[1].split(" ("))
    del data[1]
    data.extend(data[2].split(")"))
    del data[2]
    print(data)
