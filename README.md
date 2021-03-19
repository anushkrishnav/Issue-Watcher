<p align="center">
<img src="img/White and Green Gaming Badge Logo.png" height = "400px">
</p> <br>

# Rouge Spammers with a mission to disrupt the peace of the valley ? Fear not we will STOMP the Spammers
## New Update : adding 'on-review' tag on an issue will stop it from being closed by the Bot allowing contributors to create more than the limited count
This tool was created to helps you to protect your project  from being spammed. 
<br> You can customise the ``` maxIssue```  to set the maximum count of active issue a contributor can have. <br>
The project is currently a work in progress might have bugs if you do find bugs please report it [here](https://TesseractCoding/Issue_Watcher/issues) <br>
<img src="img/sample.jpeg" height = "500px">
![]()

### Example workflow

```yaml
name: check
 
on:
  issues:
    types: [opened]

jobs:
  first-job:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
        uses: actions/checkout@main
    - name: Action
        uses: TesseractCoding/Issue_Watcher@main
        with:
          token: ${{ secrets.GITHUB_TOKEN }} # default token in GitHub Workflow
          author: '${{github.actor}}'
          repo: {owner}/{repo} # your repo
          maxIssue: {any integer} #default is set as 2

```
## Contributing Guidelines

- **Plagiarism is strictly not allowed**. Any work that is found to be suspicious of plagiarized work will not be merged.
- Issues will be assigned on a _first come, first serve_ basis. You just have to comment on the issue, asking to be assigned, and it will be done if found fit.
- Preferably, you cannot work on any issue that is not assigned to you.
- In case you want to submit an improvement , we prefer that you create an issue, describing in details your improvement. This will help others to analyze your contribution. You can use the [templates](.github/ISSUE_TEMPLATE/proposal.md) that we have provided :)
- If you have anything else in mind, create an issue and please wait for it to be assigned to you. You can then start working on it and create a PR.
- All PRs must be made from a Branch. Create a separate branch for every Issue you are working upon and once found fit, make a PR.
- If you have no idea what are issues or PRs, please do refer to [this link](https://github.com/TesseractCoding/NeoAlgo/wiki/What-is-a-Pull-Request-and-how-to-do-it%3F)

Make sure your code works before submitting it and always write test for every new function that you create or improve:D

## Our Contributors

[CONTRIBUTORS.md]()

## Code of Conduct

You can find our Code of Conduct [here](/CODE_OF_CONDUCT.md).

# Note
This project is a WIP.
If you find a security threat or bug please feel free to open up an issue and we will get to it shortly

### Created by [Anush Krishna](https://github.com/anushkrishnav)

# Uses

### [PyGithub](https://github.com/PyGithub/PyGithub) - Awesome package that made this action possible <br>
### [actions/container-action](https://github.com/actions/container-action) - Container Action Template
### [jacobtomlinson/python-container-actionTemplate](https://github.com/jacobtomlinson/python-container-action) -  amazing starter template

# License
MIT licensed. See the bundled [LICENSE](LICENSE) file for more details.
