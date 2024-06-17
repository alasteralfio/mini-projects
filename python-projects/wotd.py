# Word of the Day
# 8/6/2023

import requests
from bs4 import BeautifulSoup

def scrape_word_of_the_day():
    url = 'https://www.dictionary.com/e/word-of-the-day/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    word_element = soup.find('h1', class_='js-fit-text')
    if word_element is not None:
        word = word_element.text.strip()
        return word
    else:
        return None

# Example usage
word_of_the_day = scrape_word_of_the_day()
if word_of_the_day is not None:
    print("Word of the day:", word_of_the_day)
else:
    print("Failed to scrape word of the day.")