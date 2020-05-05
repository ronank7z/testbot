import requests, json

def user_info(username):
    data = requests.get('https://api.github.com/users/{}'.format(username))
    return data.text


res = json.loads(user_info('ronank7z'))

print(res['login'])