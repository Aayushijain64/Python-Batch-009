import requests
import matplotlib.pyplot as plt

def get_pokemon_data(name = "pikachu"):
    url ="https://api.pokemontcg.io/v1/cards?name={}".format(name)
    response = requests.get(url)
    return response.json()

pokemon = input("Enter name of Pokemon: ")
result = get_pokemon_data(pokemon)
print(result['cards'])

url_image = requests.get(result['cards'][0]['imageUrl'])
#print(url_image)   : image can not be printed, we need to download it

#File Handling
with open('./image.png','wb') as f :
    for i in url_image.iter_content(1024):
        f.write(i)

image = plt.imread("image.png")
plt.imshow(image)
plt.show()

import urllib.request

opener = urllib.request.build_opener()
opener .addheaders = [('User-agent','Mozilla/5.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(result['cards'][1]['imageUrl'],"image1.png")

image1 = plt.imread("image1.png")
plt.imshow(image1)
plt.show()