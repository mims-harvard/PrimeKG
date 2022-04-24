import pandas as pd
from bs4 import BeautifulSoup, NavigableString, Tag
import urllib.request
import csv


def parse(soup):
    out={}
    for header in soup.find_all('h2'):
        nextNode = header
        if len(nextNode.text) == 0:
            break
        if nextNode.text not in ['Symptoms', 'Causes', 'Risk factors', 'Complications', 'Prevention']:
            continue
        key = nextNode.text
        content = []
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                continue
            if isinstance(nextNode, Tag):
                if nextNode.name == "h2":
                    break
                if nextNode.name == "div": # skip pop-up window for illustration and alt-text
                    continue
                elif len(nextNode.get_text(strip=True).strip())!=0:
#                     print(nextNode.get_text(strip=False).strip(),'+++')
                    content.append(nextNode.get_text(strip=False).strip())
        out[key]= '\n'.join(content)
    if 'Symptoms' not in list(out.keys()):
        out['Symptoms'] = 'None'
    if 'Causes' not in list(out.keys()):
        out['Causes'] = 'None'
    if 'Risk factors' not in list(out.keys()):
        out['Risk factors'] = 'None'
    if 'Complications' not in list(out.keys()):
        out['Complications'] = 'None'
    if 'Prevention' not in list(out.keys()):
        out['Prevention'] = 'None'
#     print('Successfully parsed 1 item!')
    return out

df = pd.read_csv("diseases.csv")

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}

i = 0
with open('diseases_parsed.csv','w', encoding='utf8') as f:
    for url in df['link'].tolist():
        i += 1
        req = urllib.request.Request(url,headers=headers)
        resp = urllib.request.urlopen(req)
        soup = BeautifulSoup(resp.read(), 'html.parser')
        mydict = parse(soup)
        w = csv.DictWriter(f, mydict.keys())
        if i == 1:
            w.writeheader()
        w.writerow(mydict)
        if i % 100 == 0:
            print('Done: '+str(i))


parsed = pd.read_csv("diseases_parsed.csv")

df2 = df.merge(parsed, how='inner', left_index=True, right_index=True)

df2.to_csv('for_jingyi.csv')



