import requests

url = "https://currencyapi.net/api/v1/rates?key=2s3nMXHymV7G0kLegEjKeXVTw4uKUxjpQDnX"



response = requests.get(url)

data = response.json()

for i in data.keys():
    if i=="rates":
        rates = data[i]
        for j in rates:
            if j != "ALL":
                print("{}:{}".format(j,rates[j]))

