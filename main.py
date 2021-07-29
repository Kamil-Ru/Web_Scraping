from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_link = soup.find_all("a", class_="storylink")[0].get_text()

articles = soup.find_all("a", class_="storylink")

article_tags = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_tags.append(text)

    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]


print(article_tags)
print(len(article_tags))

print(article_links)
print(len(article_links))

print(article_upvote)
print(len(article_upvote))

print(article_tags[10])


largest_number = max(article_upvote)
article_upvote_index = article_upvote.index(largest_number)
print(article_upvote_index)

print(f"Number: {article_upvote_index+1} Title: {article_tags[article_upvote_index]}\n "
      f"Vote: {article_upvote[article_upvote_index]} \nURL: {article_links[article_upvote_index]}")

#   with open("website.html", "r") as file:
#       contents = file.read()
#
#   soup = BeautifulSoup(contents, 'html.parser')
#
#   print(soup.p)
#
#   all_anchor_tags = soup.find_all(name="a")
#   print(all_anchor_tags)
#
#   for tag in all_anchor_tags:
#       print(tag.get("href"))
#
#   heading = soup.find(name="h1", id="name")
#
#   print(heading.get_text())
#
#   section_heading = soup.find(name="h3", class_="heading")
#   print(section_heading.get_text())
#
#   company_url = soup.select_one(selector="p a")
#   print(company_url)
#
#   name = soup.select_one(selector="#name")
#   print(name)
#
#   headings = soup.select_one(".heading")
#   print(headings)