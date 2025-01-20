import requests
# response=requests.get("https://api.github.com/repos/SkafteNicki/dtu_mlops")

# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )

response = requests.get('https://imgs.xkcd.com/comics/making_progress.png') # image
with open(r'img.png','wb') as f:
    f.write(response.content)
    

print(response.status_code)
# print(response.content) # type = byte
# print(response.json()) # more readable


pload = {'username':'Olivia','password':'123'}
response = requests.post('https://httpbin.org/post', data = pload)