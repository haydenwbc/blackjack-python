# blackjack-python
An exploratory python project weaving together machine learning, game design, computer networking, and GUI through the classic card game blackjack


Guide for Collaborators on the Blackjack Game Repository:
1. Cloning the Repository:
Before you start working, you'll need a local copy of the repository on your machine.

Open a terminal or command prompt.
Navigate to the directory where you want to store the project.
Run the command:
git clone git@github.com:haydenwbc/blackjack-python.git

2. Always Pull Before You Start Working:
To ensure you have the latest changes from the main branch:
git pull origin main


3. Creating a New Branch:
Instead of working directly on the main branch, create a new branch for the feature or bugfix you're working on. This helps keep the main branch stable.

To create and switch to a new branch:
git checkout -b [branch-name]
Replace [branch-name] with a descriptive name for your branch (e.g., add-hit-functionality).


4. Making Changes:
After you've made some changes to the code:

Stage your changes:
git add .

Commit your changes with a descriptive message:
git commit -m "Description of changes made"


5. Pushing Your Branch to GitHub:

Push your branch to the repository:
git push origin [branch-name]

6. Creating a Pull Request (PR):
Once you've pushed your branch and are ready to integrate your changes into the main branch:

Go to the GitHub repository page.
Click on 'Pull requests'.
Click 'New pull request'.
Select your branch from the dropdown.
Review the changes and click 'Create pull request'.

7. Merging the PR:
   
Click 'Merge pull request'.
Click 'Confirm merge'.
It's now safe to delete the feature branch both locally and remotely.

8. Deleting Branches:

To delete the local branch:
git branch -d [branch-name]

To delete the remote branch:
git push origin --delete [branch-name]


9. Switching Back to main and Pulling:
Before you start working on a new feature or bugfix, switch back to main and pull the latest changes.
git checkout main
git pull origin main
