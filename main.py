import requests
from fake_headers import Headers
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']


site_name = 'https://habr.com'
url = 'https://habr.com/ru/articles'
response = requests.get(url,
                        headers=Headers(browser='chrome', os='mac').generate())

soup = bs4.BeautifulSoup(response.text, features='lxml')
article_list = soup.find_all('article', class_='tm-articles-list__item')

for article in article_list:
    article_title_link = article.find('a', class_='tm-title__link')
    article_date = article.find('a', class_='tm-article-datetime-published '
                                'tm-article-datetime-published_link').find('time')['datetime'].strip()
    article_publications = article.find_all('a', class_='tm-publication-hub__link')
    article_publications_text = ''

    for article_publication in article_publications:
        article_publications_text +=' ' + article_publication.text

    article_paragraphs = article.find_all('p')
    article_text = ''

    for paragraph in article_paragraphs:
        article_text += paragraph.text.strip()

    for keyword in KEYWORDS:
        if (keyword in article_title_link.text.strip().lower() or
            keyword in article_text.strip().lower() or
            keyword in article_publications_text.strip().lower()):
            print(f'{article_date} - {article_title_link.text} - '
                  f'{site_name + article_title_link['href']}')