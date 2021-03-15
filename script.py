import requests

def count_issues(name, token):
    owner = name
    repo = "Issue-spam-blocker"
    author = name
    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{owner}/{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw=(r.json())
    return raw['total_count']

def get_latest_issue(name,token):
    owner = name
    repo = "Issue-spam-blocker"
    author = name
    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{owner}/{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw=(r.json())
    k = raw['items']
    k = k[0]
    return k['number']