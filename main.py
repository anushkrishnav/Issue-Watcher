import os
import github

# extracting all the input from environments
title = os.environ['INPUT_TITLE']
token = os.environ['INPUT_TOKEN']
author = os.environ['INPUT_AUTHOR']

# as I said GitHub expects labels and assignees as list but we supplied as string in yaml as list are not supposed i
# .yaml format
github = github.Github(token)
# GITHUB_REPOSITORY is the repo name in owner/name format in Github Workflow
repo = github.get_repo(os.environ['GITHUB_REPOSITORY'])

def close_issue(num):
    issue = repo.get_issue(num)
    issue.create_comment('bonk !! You cannont create more than 3 Issues at a time close your old issues to make a new one')
    issue.edit(state = 'closed')
repo.get_issue(100)
repo.edit()
# issue = repo.create_issue(
#     title=title,
#     body=body,
#     assignees=assignees,
#     labels=labels
# )