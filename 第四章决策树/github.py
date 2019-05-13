from urllib.request import urlopen
from urllib.request import Request
import datetime
import json

def get_results(username,headers):
    url = 'https://api.github.com/users/{}/repos'.format(username)
    req = Request(url,headers=headers,method='GET')
    response = urlopen(req).read()
    result = json.loads(response.decode())
    return result
def delete_repo(username,repo_name,headers):
    url = 'https://api.github.com/repos/{}/{}'.format(username,repo_name)
    req = Request(url,headers=headers,method='DELETE')
    response = urlopen(req).read()
    print(response)
def confirm(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False
if __name__ == '__main__':
    token = input('please input you token,if not,creat first!\n token: ')
    username = "phunsuke"
    headers = {'User-Agent':'Mozilla/5.0',
               'Authorization': 'token {}'.format(token),
               'Content-Type':'application/json',
               'Accept':'application/json'
               }
    repo = get_results(username,headers)
    print("you have {} repositories on your github.".format(len(repo)))
    for item in repo:
        name = item['name']
        if confirm(name):
            print('yes')
            delete_repo(username,name,headers)
        else:
            print('no')