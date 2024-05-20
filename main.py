import pandas
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

URL = "https://steamcommunity.com/stats/1245620/achievements/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

numbers = []
percentages = soup.find_all("div", class_="achievePercent")
for i in percentages:
  percent = float(i.text[0:-1])
  numbers.append(percent)

names = []
achievements = soup.find_all("div", class_="achieveTxt")
for i in achievements:
  a = i.text.strip().split("\n")[0]
  names.append(a)

data_dictionary = {
  "achievement": names,
  "percent": numbers
}

df = pandas.DataFrame(data_dictionary)

plt.figure(figsize=(12, 6))
plt.barh(df['achievement'], df['percent'], color='skyblue')
plt.xlabel('Percentage')
plt.ylabel('Achievement')
plt.title('Achievement Percentage Graph')
plt.gca().invert_yaxis()  

plt.tight_layout()
plt.show()

# https://matplotlib.org/stable/tutorials/pyplot.html