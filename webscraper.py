import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from pprint import pprint
url_list = []
test_url = url_list[3]

page = requests.get(test_url).text
soup = BeautifulSoup(page, "html5lib")

headline = soup.find('h1').get_text()

p_tags = soup.find_all('p')
# Get the text from each of the “p” tags and strip surrounding whitespace.
p_tags_text = [tag.get_text().strip() for tag in p_tags]

sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
# Combine list items into string.
article = ' '.join(sentence_list)

summary = summarize(article, ratio=0.3)

with open('output.txt','w') as f:
    f.writelines(summary)
