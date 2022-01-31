import requests
import fake_useragent
from bs4 import BeautifulSoup

user_agent = fake_useragent.UserAgent().random
header = {'user-agent': user_agent}

url = requests.get('https://www.pracuj.pl/praca/programista%20python;kw/warszawa;wp?rd=30', headers=header)

soup = BeautifulSoup(url.text, 'html.parser')

paginator = soup.find('div', {'class': 'pagination'})

pages = paginator.find_all('a')

print(pages)