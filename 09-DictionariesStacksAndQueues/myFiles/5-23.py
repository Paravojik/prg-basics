import requests
import json
# 1. Define the endpoint URL
url = "https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10"

# 2. Make the request
response = requests.get(url)

# 3. Check if it was successful (Status Code 200)
if response.status_code == 200:
    # 4. Convert the response JSON into a Python dictionary
    data = response.json()

    with open('./euro.json','w',encoding='utf-8') as file:
        json.dump(data,file,indent=2)
else:
    print(f"Error: {response.status_code}")



with open('./euro.json','r',encoding='utf-8') as file:
    data=(json.load(file)['rates'])
print('Date            Buying Rate     Selling Rate')
print('============================================')
for i in data:
    print(f'{i['effectiveDate']:<16}{i['bid']:<16}{i['ask']}')