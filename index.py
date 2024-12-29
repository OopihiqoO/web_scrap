import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = '/users/lesdrova/Desktop/VS_python/pycharm/chromedriver'

options = Options()
options.headless = False
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

url = "https://oxylabs.io/blog"
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

results = []

for element in soup.find_all(attrs={"class": "blog-card__content-wrapper"}):
    name = element.find('h2')
    if name and name.text.strip() not in results:
        results.append(name.text.strip())

driver.quit()

df = pd.DataFrame({
    'Blog Post Titles': results
})
df.to_csv('blog_titles.csv', index=False, encoding='utf-8')

print(df)

other_results = []
for element in soup.find_all(attrs={"class": "blog-card__date-wrapper"}):
    date = element.find('p')
    if date:
        other_results.append(date.text.strip())

df['Date'] = other_results

df.to_csv('blog_titles_with_dates.csv', index=False, encoding='utf-8')
print(df)
print("Scraping done")

