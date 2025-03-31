import requests
from bs4 import BeautifulSoup

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# URL = "https://www.billboard.com/charts/hot-100/" + date

# response = requests.get(url=URL, headers=header)

URL = "https://www.armadamusic.com/news/the-100-best-vocal-trance-classics-1997-2011"
response = requests.get(URL)
hot_100 = response.text
soup = BeautifulSoup(hot_100, 'html.parser')

songs = soup.find_all(name='strong', )
song_titles = [song.getText() for song in songs]

print(song_titles)

# songs = soup.find_all(name='h3', class_='a-no-trucate')
# song_titles = [song.getText().strip() for song in songs]
# # song_titles = song_titles[::-1]
# artists = soup.find_all(name='span', class_='a-no-trucate')
# artist_names = [artist.getText().strip() for artist in artists]
# # artist_names = artist_names[::-1]

# print(artist_names)

with open('songs.txt', mode='w') as file:
    for song in song_titles:
        file.write(f"{song}\n")
# with open('artists.txt', mode='w') as file:
#     for artist in artist_names:
#         file.write(f"{artist}\n")
        
        
