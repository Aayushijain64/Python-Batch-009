#Joke API calling
import requests

url = "https://sv443.net/jokeapi/v2/joke/Any?category"


response = requests.get(url)

print(response)

data = response.json()

for i in data.keys():
    if i!= "error" :
        print("{} : {}".format(i,data[i]))
