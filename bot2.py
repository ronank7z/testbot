import requests, json

def user_info(username):
    data = requests.get('https://api.github.com/users/{}'.format(username))
    res = json.loads(data.text)
    return res

username = user_info('ronank7z')['login']

def commit(username, repos):
    data = requests.get('https://api.github.com/repos/{}/{}/commits'.format(username, repos))
    res = json.loads(data.text)
    return res

res = user_info('ronank7z')
count_commit = len(commit('ronank7z','testbot'))

count = count_commit

print(res['login'])
count += count_commit
print(count_commit)