import requests
import bs4

url = "https://github.com/psf/requests"

response = requests.get(url)
#print(response.text)

#Conversion into HTML form
webpage = bs4.BeautifulSoup(requests.get(url).text,"lxml")
webpage


#HTML : Frontend Designer
#OL : Ordered List [1,2,3,4] and UL :Unordered list ( through Bullet) 
#Subpart of a webpage
#sub_webpage = webpage.find_all(name = "ul", attrs={"class" : "numbers-summary"})
#print(sub_webpage)