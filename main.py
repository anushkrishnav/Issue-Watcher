import os
import requests
import github
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def count_issues(name, token, repo):
    author = name
    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw=(r.json())
    return raw['total_count']

def get_latest_issue(name,token, repo):
    author = name
    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw=(r.json())
    k = raw['items']
    k = k[0]
    return k['number']

def close_issue(num,repo):
    issue = repo.get_issue(num)
    issue.create_comment('# STOMP !! <br> \
        ![](https://i.imgflip.com/urmgl.jpg) <br> \
        You cannot have more than 3 issues open, kindly close or finish your current issues before you make a new one.')
    issue.edit(state = 'closed')
    return


token = os.environ['INPUT_TOKEN']
author = os.environ['INPUT_AUTHOR']
repourl = os.environ['INPUT_REPO']


github = github.Github(token)
print(token)
repo = github.get_repo(repourl)

count = count_issues(name=author, token=token, repo=repourl)

numb = get_latest_issue(name=author, token=token, repo=repourl)
if count >= 4:
    close_issue(numb,repo)

