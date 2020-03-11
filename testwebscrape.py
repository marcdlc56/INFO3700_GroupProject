from bs4 import BeautifulSoup as BS
import requests
import pandas as pd

url_list = ["https://www.nytimes.com/2019/07/07/technology/preschool-online-waterford-upstart.html","https://nancyebailey.com/2019/04/16/what-preschool-isnt-waterford-upstart-and-any-other-online-program/","http://kutv.com/features/fresh-living/waterford-upstart-program","https://www.concordmonitor.com/Play-based-learning-and-Upstart-32644905","https://www.falloncountyextra.com/news/federal-grant-brings-early-education-option-to-rural-montana-/article_ceafe640-4ea2-11ea-bd61-7f260356840e.html","https://www.greatfallstribune.com/story/news/2020/02/13/early-education-opportunity-available-rural-montana-families-online-free-next-school-year/4726387002/","http://madisoniannews.com/schools/free-early-education-tool-madison-county","https://www.smartbrief.com/original/2020/03/build-early-learning-we-must-build-communities","https://www.deseret.com/opinion/2020/2/28/21153323/guest-opinion-early-childhood-development-matters-to-utah-leaders","https://www.kxnet.com/news/local-news/a-free-kindergarten-readiness-program-begins-second-year-in-nd/","https://www.kulr8.com/regional/federal-grant-helps-bring-early-education-to-rural-montana-families/article_5a8fa9cf-5e04-54be-9fe1-993be4a0d634.html","https://www.bowmanextra.com/community/families-across-rural-north-dakota-can-now-register-their-four/article_ef78c3fc-5455-11ea-b3bd-df2bc710e179.html","https://www.kotatv.com/content/news/Education-nonprofit-helping-rural-students-prepare-for-kindergarten-568555531.html","https://www.smartbrief.com/original/2020/02/getting-starting-line","https://www.abc4.com/news/education/waterford-upstart-provides-a-free-program-for-pre-k-education/"]



res=[] #placing res outside of loop
for link in url_list:
    r = requests.get(link)
    r.encoding = 'utf-8'

    html_content = r.text
    soup = BS(html_content, 'html5lib')


    table = soup.find('table', class_='bigborder')
    if not table:
        continue

    trs = table.find_all('tr')

    if not trs:
        continue #if trs are not found, then starting next iteration with other link


    headers = trs[0]
    headers_list=[]
    for td in headers.find_all('td'):
        headers_list.append(td.text)
    headers_list+=['Season']
    headers_list.insert(19,'pseudocol1')
    headers_list.insert(20,'pseudocol2')
    headers_list.insert(21,'pseudocol3')

    row = []
    season = ''
    for tr in trs[1:]:
        if 'Season' in tr.text:
            season = tr.text

        else:
            tds = tr.find_all('td')
            for td in tds:
                row.append(td.text.strip('\n').strip('\r').strip('\t').strip('"').strip())
            row.append(season.strip())
            res.append(row)
            row=[]

res = [i for i in res if i[0]!=''] #outside of loop

df=pd.DataFrame(res, columns=headers_list) #outside of loop
del df['pseudocol1'],df['pseudocol2'],df['pseudocol3']
del df['VideoReplay']

df.to_csv('tables.csv') #outside of loopername/'+str(url_list.index(link))+'.csv')