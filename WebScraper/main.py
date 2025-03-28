from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.find_all(name='span', class_='titleline')
articles_texts = []
articles_links = []

for article in articles:
    article_text = article.a.get_text()
    articles_texts.append(article_text)
    article_link = article.a.get('href')
    articles_links.append(article_link)
    
articles_upvotes = [int(score.getText().split()[0]) for score  in soup.find_all(name='span', class_='score')]
index = articles_upvotes.index(max(articles_upvotes))

print(articles_texts[index])
print(articles_links[index])
print(articles_upvotes[index])








# with open('website.html') as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.find_all(name='p'))


