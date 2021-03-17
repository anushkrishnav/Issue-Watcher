import os
import requests
import github
from pprint import pprint
# required to run the script locally
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


def count_issues(author, token, repo):
    r'''
    A function to count the number of open Issues created by a contributor
    of the project.
    author : Github id of the contributor
    token : Github Token
    repo : Reository for which we are retriving the count
    '''

    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw = (r.json())
    return raw['total_count']


def get_latest_issue(author, token, repo):
    r'''
    A function to get a contributor's latest Open Issue.
    author : Github id of the contributor
    token : Github Token
    repo : Reository for which we are retriving the count
    '''
    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw = (r.json())
    k = raw['items']
    k = k[0]

    if len(k['labels']) != 0 and 'on-review' in k['labels'][0]['name']:
        return None
    return k['number']


def close_issue(num, repo, maxi):
    r'''
    A function to close the issue number num
    and add a comment to the issue stating the reason.
    num : number of the issue that has to be closed
    repo : Reository for which we are retriving the count
    maxi : Maximium count of open Issue a contributor can have
    '''
    issue = repo.get_issue(num)
    issue.create_comment('''## STOMP !! <br>        ![](https://pbs.twimg.com/media/EWQM1qRUEAAEVdh.jpg)<br>
### Sorry but You cannot have more than ''' + str(maxi) + '''  issues open, kindly close or finish your current issues before you make a new one.
### <br> if you feel the issue is Important please tag a maintainers. <br>
### This action is being deployed to prevent spamming of Issues,      <br>   If you are not spamming then You are doing great work Keep it up !!''')
    issue.edit(state='closed')
    return


token = os.environ['INPUT_TOKEN']
author = os.environ['INPUT_AUTHOR']
repourl = os.environ['INPUT_REPO']
maxi = os.environ['INPUT_MAXISSUE']

if maxi is None:
    maxi = 2
else:
    maxi = int(maxi)

github = github.Github(token)
repo = github.get_repo(repourl)

count = count_issues(author=author, token=token, repo=repourl)

numb = get_latest_issue(author=author, token=token, repo=repourl)
if numb is not None:
    if count >= maxi+1:
        close_issue(numb, repo, maxi)
