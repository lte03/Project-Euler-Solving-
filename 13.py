from bs4 import BeautifulSoup
import requests

url = "https://projecteuler.net/minimal=13"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content,"lxml")

num_text = soup.find("div")

text = num_text.get_text().splitlines()

text.remove("")

numbers = [int(text[i]) for i in range(len(text))]

result = str(sum(numbers))[:10]
print(result)
