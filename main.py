import os
import github
from script import count_issues

numb = os.environ['INPUT_NUMBER']
token = os.environ['INPUT_TOKEN']
author = os.environ['INPUT_AUTHOR']

def close_issue(num):
    issue = repo.get_issue(num)
    issue.create_comment('bonk !! You cannont create more than 3 Issues at a time close your old issues to make a new one')
    issue.edit(state = 'closed')

github = github.Github(token)
repo = github.get_repo(os.environ['GITHUB_REPOSITORY'])
count_issues(name=author,token=token)
if count_issues >= 4:
    close_issue(numb)
