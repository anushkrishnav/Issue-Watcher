# Rouge Spammers with a mission to disrupt the peace of the valley ? Fear not we will STOMP the Spammers

![](botinaction.jpeg)

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
        uses: anushkrishnav/Issue-Police@main
      - name: Run Action
        uses: ./
        with:
          token: ${{ secrets.GITHUB_TOKEN }} # default token in GitHub Workflow
          author: anushkrishnav
```
