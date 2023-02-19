import requests


user_input = input('Enter your request ')

payload = {'q': user_input}

resp = requests.get('https://api.giphy.com/v1/gifs/search?api_key=FAmnTqm6fR1mq6aHt7apyhqD9MBZiqRv&limit=25&offset=0&rating=g&lang=en', payload)

response = resp.json()

if "data" not in response:
    print('something went wrong')
    exit()

if resp.status_code != 200:
    print(response['meta']['msg'])
    exit()

response = response['data']

if len(response) == 0:
    print('It seems nothing to output')
    exit()

for obj in response:
    print(obj['url'])

