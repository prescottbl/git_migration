
## Purpose

---

To be used for migrating from BitBucket to GitHub. Account issues with the BitBucket has forced us to move up our timeline to switch over to GitHub.
This script will clone/pull from a repo in BitBucket and push changes to GitHub. This will be used to migrate and to keep repos synced so we can make the transition
from BitBucket to GitHub as seamless as possible. 

## Usage

---

Before running make sure that the `root_directory` in `git_info.yaml` exists and navigate to the directory where this script is stored. <br>
The `root_directory` should be a directory where you would like to temporily clone all repos that are to be moved. 

Under `git_repos` in `git_info.yaml` use the following format: <br>
```
  bitbucket_repo_name:
    bb_url: <ssh url for bitbucket>
    gh_url: <ssh url for GitHub>
```
<br>
NOTE: The `bitbucket_repo_name` should be the same as the directory that will be created when running `git clone` on that repo.
<br> To run the script:
`python3 git_migration.py`

#### Report a problem

---

To report a problem, contact blake.prescott@lexisnexisrisk.com or @prescottb on Teams.


