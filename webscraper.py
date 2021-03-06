import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from pprint import pprint
url_list = ["https://www.nytimes.com/2019/07/07/technology/preschool-online-waterford-upstart.html","https://nancyebailey.com/2019/04/16/what-preschool-isnt-waterford-upstart-and-any-other-online-program/","http://kutv.com/features/fresh-living/waterford-upstart-program","https://www.concordmonitor.com/Play-based-learning-and-Upstart-32644905","https://www.falloncountyextra.com/news/federal-grant-brings-early-education-option-to-rural-montana-/article_ceafe640-4ea2-11ea-bd61-7f260356840e.html","https://www.greatfallstribune.com/story/news/2020/02/13/early-education-opportunity-available-rural-montana-families-online-free-next-school-year/4726387002/","http://madisoniannews.com/schools/free-early-education-tool-madison-county","https://www.smartbrief.com/original/2020/03/build-early-learning-we-must-build-communities","https://www.deseret.com/opinion/2020/2/28/21153323/guest-opinion-early-childhood-development-matters-to-utah-leaders","https://www.kxnet.com/news/local-news/a-free-kindergarten-readiness-program-begins-second-year-in-nd/","https://www.kulr8.com/regional/federal-grant-helps-bring-early-education-to-rural-montana-families/article_5a8fa9cf-5e04-54be-9fe1-993be4a0d634.html","https://www.bowmanextra.com/community/families-across-rural-north-dakota-can-now-register-their-four/article_ef78c3fc-5455-11ea-b3bd-df2bc710e179.html","https://www.kotatv.com/content/news/Education-nonprofit-helping-rural-students-prepare-for-kindergarten-568555531.html","https://www.smartbrief.com/original/2020/02/getting-starting-line","https://www.abc4.com/news/education/waterford-upstart-provides-a-free-program-for-pre-k-education/"]
collective_summary = []
for i in url_list:
    url = i
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html5lib")

    p_tags = soup.find_all('p')
    # Get the text from each of the “p” tags and strip surrounding whitespace.
    p_tags_text = [tag.get_text().strip() for tag in p_tags]

    sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
    sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
    # Combine list items into string.
    article = ' '.join(sentence_list)

    summary = summarize(article, ratio=1)
    collective_summary.append(str(summary))

with open('output.txt','w') as f:
    f.writelines(collective_summary)

