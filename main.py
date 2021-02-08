from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")
website = res.text

soup = BeautifulSoup(website, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
most_popular = max(article_upvotes)
most_poplar_index = article_upvotes.index(most_popular)

print(article_texts[most_poplar_index])
print(article_links[most_poplar_index])