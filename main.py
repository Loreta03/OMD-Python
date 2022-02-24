import random
import requests
from bs4 import BeautifulSoup
import json
import sys
import os.path

def GenerateList():
    url = 'https://www.empireonline.com/movies/features/best-movies-2/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    script_str = soup.find('script', attrs={'type':'application/json'})
    movies = []
    json_object = json.loads(script_str.contents[0])
    array = json_object['props']['pageProps']['data']['getArticleByFurl']['_layout'][7]['content']['images']

    for el in array:
        movie = {
            "name":"",
            "seen":False
            }
        if type(el['titleText']) is not None:
            movie['name']=str(el['titleText']).split(")")[1]
            movies.append(movie)
            
    movies.reverse()
    json_movies = json.dumps(movies)
    
    with open('movies.json', 'w') as file:
        file.write(json_movies)
        file.close()

def GetMovie():
    notSeen = []
    file = open('movies.json', 'r')
    movies = json.loads(file.read())
    for movie in movies:
        if movie['seen'] == False:
            notSeen.append(movie['name'])
    file.close()
    random_movie = random.choice(notSeen)
    print(random_movie)

def AddMovie():
    file = open('movies.json', 'r')
    movies = json.loads(file.read())
    file.close()
    new_movie_name = ""
    exists = False
    for i in range(2, len(sys.argv)):
        new_movie_name += " "+str(sys.argv[i])
    for movie in movies:
        if movie['name'] == new_movie_name:
            exists = True
    if exists == True:
        print("You already have that movie in your list")
    else:
        new_movie = {
            "name":new_movie_name,
            "seen":False
            }
        movies.append(new_movie)
        with open('movies.json', 'w') as file:
            js = json.dumps(movies)
            file.write(js)
            file.close()

def MarkMovieAsSeen():
    file = open('movies.json', 'r')
    movies = json.loads(file.read())
    file.close()
    seen_movie_name = ""
    exists = False
    for i in range(2, len(sys.argv)):
        seen_movie_name += " "+str(sys.argv[i])
    for movie in movies:
        if movie['name'] == seen_movie_name:
            movie['seen'] = True
            exists = True
    if exists == False:
        print("You do not have a movie with such name in your list")
    else:
        with open('movies.json', 'w') as file:
            js = json.dumps(movies)
            file.write(js)
            file.close()
        
if len(sys.argv)>1:
    if sys.argv[1] == '--generateList':  
        if os.path.isfile('movies.json'):
            print("You can not call --generateList two times, you already have a generated list")
            file = open('movies.json', 'r')
            print(file.read())
        else:
            GenerateList()
    elif sys.argv[1] == '--help':
        print('--generateList\n--getMovie\n--addMovie\n--markMovieAsSeen\n--help')
    elif sys.argv[1] == '--getMovie':
        GetMovie()
    elif sys.argv[1] == '--addMovie':
        if len(sys.argv)>2:
            AddMovie()
        else:
            print("Please enter the name of movie you wnat to add to your list")
    elif sys.argv[1] == '--markMovieAsSeen':
        if len(sys.argv)>2:
            MarkMovieAsSeen()
        else:
            print("Please enter the name of movie you want to mark as seen")
else:
    print("You must write a command that you want to do, try again. You can write --help to see all the commands")

