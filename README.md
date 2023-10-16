# blackjack-python
An exploratory python project weaving together machine learning, game design, computer networking, and GUI through the classic card game blackjack


Guide for Collaborators on the Blackjack Game Repository:
1. Cloning the Repository:
Before you start working, you'll need a local copy of the repository on your machine.

Open a terminal or command prompt.
Navigate to the directory where you want to store the project.
Run the command:
bash
Copy code
git clone [URL]
Replace [URL] with the repository URL.
2. Always Pull Before You Start Working:
To ensure you have the latest changes from the main branch:

css
Copy code
git pull origin main
3. Creating a New Branch:
Instead of working directly on the main branch, create a new branch for the feature or bugfix you're working on. This helps keep the main branch stable.

To create and switch to a new branch:
css
Copy code
git checkout -b [branch-name]
Replace [branch-name] with a descriptive name for your branch (e.g., add-hit-functionality).
4. Making Changes:
After you've made some changes to the code:

Stage your changes:
csharp
Copy code
git add .
Commit your changes with a descriptive message:
sql
Copy code
git commit -m "Description of changes made"
5. Pushing Your Branch to GitHub:

Push your branch to the repository:
css
Copy code
git push origin [branch-name]
6. Creating a Pull Request (PR):
Once you've pushed your branch and are ready to integrate your changes into the main branch:

Go to the GitHub repository page.
Click on 'Pull requests'.
Click 'New pull request'.
Select your branch from the dropdown.
Review the changes and click 'Create pull request'.
Add a title and description explaining your changes.
Wait for someone to review your PR. It's good practice for another developer to review and merge your changes, ensuring quality and preventing mistakes.
7. Merging the PR:
If the reviewer agrees with your changes and there are no conflicts:

Click 'Merge pull request'.
Click 'Confirm merge'.
It's now safe to delete the feature branch both locally and remotely.
8. Deleting Branches:

To delete the local branch:
css
Copy code
git branch -d [branch-name]
To delete the remote branch:
css
Copy code
git push origin --delete [branch-name]
9. Switching Back to main and Pulling:
Before you start working on a new feature or bugfix, switch back to main and pull the latest changes.

css
Copy code
git checkout main
git pull origin main
