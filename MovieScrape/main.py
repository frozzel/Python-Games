import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movies_100 = response.text

soup = BeautifulSoup(movies_100, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
movies_titles = [movie.getText() for movie in movies]
movies_titles = movies_titles[::-1]

with open('movies.txt', mode='w') as file:
    for movie in movies_titles:
        file.write(f"{movie}\n")
        
        
