import requests
import json
import pandas as pd
import bs4

#Steps to do :
#movieid using pandas and make list : done
#movie id is send as a parameter , web scrape the movie id detail
#Dictionary form printing of all the parameters

def get_id(num):
    data = pd.read_csv("links.csv") 
    start = 0
    end = start + num
    list_of_movies = list(data.imdbId)
    return list_of_movies[start : end+1]

def scrape_id(list_of_movies) :
    url = "https://www.imdb.com/title/tt{}/".format(str(list_of_movies).zfill(7))
    response = requests.get(url)
    html_parse = bs4.BeautifulSoup(response.text,"html.parser")
    current_page_json = html_parse.find("script", attrs = {"type" : "application/ld+json"})
    current_page_json = str(current_page_json)[str(current_page_json).find('{'):-9]
    return current_page_json

def collect_movie_parameters(list_of_movies) :
    json_dict = json.loads(scrape_id(list_of_movies))
    movie = {
        "name" : json_dict['name'],
        "genre" : json_dict['genre'],
        "image" : json_dict['image']
    }
    print(movie["name"])
    return movie 

def show_movie(movie_per_page = 20):
    ids = get_id(movie_per_page)
    scrape_results = {"movies" : []}
    for i in ids :
        scrape_results["movies"].append(collect_movie_parameters(i))
        return scrape_results



ids = get_id(10)
for i in ids:
    print(collect_movie_parameters(i))
