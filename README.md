# Hello Git (main)

## Creating a git repository
1. git init -> intialize a new repository
2. touch README.md -> create a "README.md" file
3. git branch -M main -> change branch name to main
4. git status -> check the status
5. git add -A -> add all changes in the working directory to the staging area
6. git commit -m "Message here" -> commit changes with a message
7. git push -u origin main -> push items to branch main

## Branches
1. git branch branch-name -> creates a branch with certain name
2. git checkout branch-name -> switch to that branch

### Merge branches
1. git checkout branch-name -> navigate to the branch you want to merge
2. git merge other-branch-name -> merge with another branch (make sure to fix conflicts)

## Cloning someone else's repository
1. Navigate to the folder you want to clone to
2. git clone <link> -> clones a repository with all branches into your folder
