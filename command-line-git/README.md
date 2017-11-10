# Command Line Git

Git is a version control system often used by teams to manage project files. Github is a website built around Git on which hundreds of thousands of users manage projects and project files. Incorporating Git and Github into your workflow can save lots of time, can help you show the individuals responsible for different features of your projects, and can give you one of the fundamental skills required for a variety of technical enterprises.

This guide is intended for researchers with some exposure to GitHub. If you're totally new to GitHub, we recommend you try out GitHub's [visual introduction to Git](https://guides.github.com/activities/hello-world/) before continuing with the guide below.

# Installing Dependencies

To get started with Git on the command line, we need to install some system-level dependencies.

#### Installing Dependencies on OSX

To install the required dependencies on OSX, you should first open a terminal. The easiest way to do so is to hold COMMAND and press SPACE BAR, type "terminal" and hit enter.

Inside the terminal, type `git`. If Git is installed you'll get a response like this:

![git response on osx](./assets/git-osx.png)

Otherwise, you should be prompted to install xcode. If you're not prompted, you can run `xcode-select --install` to manually install xcode, which will install git for you.

Once that finishes downloading and installing, you should see the commands displayed in the screenshot above when you run `git`.

#### Installing Dependencies on Windows

If you use Windows, the easiest way to install the required dependencies is to download and install [Git Bash](https://git-scm.com/download/win), a Unix-like terminal for Windows. After clicking the link above, click on the installer and accept all defaults.

Once that installs, you should be able to click on the Windows icon in the lower-left-hand corner of your taskbar, search for "Git Bash", and click on the Git Bash icon:

![git bash in programs](./assets/git-bash.png)

That should bring up a terminal that's fully equipped with Git.

## Introduction to Git

Now that Git's installed, let's cover what Git does. Essentially, Git is a simple tool that keeps track of changes made to files. Git users can tell Git when to add, edit, or delete files in a folder, and how to handle cases where multiple people have edited the same file in different ways.

The core ideas of Git are simple. We start with some files in a <b>workspace</b> (a folder under Git control). We then add those files to a <b>staging area</b> (a representation of the changes we want to keep). Next we commit those changes to our <b>local repository</b> (the copy of our project's content on your machine). Finally, we push those changes from our local repository to our <b>remote repository</b> (the copy of our project's content on a remote server, e.g. on GitHub). Here's a visual representation of this workflow:

![simple git workflow](./assets/git-operations.png)

To contribute to a project using Git, we only need to `add` files to our staging area, `commit` the changes in our staging area, then `push` those changes up to our remote server. That's all it takes!

## Getting Set Up: Creating a Remote Repository

In order to practice this workflow, we'll need a <b>remote repository</b> to which we can push our changes. Let's go ahead and make that repository on GitHub. To do so, log into <a href='https://github.com'>GitHub</a> then navigate to `https://github.com/new`. This will display an interface that looks like this:

![new repository](./assets/new-repository.png)

Let's name our new repository 'learning-git', and let's type a short description that outlines the goal of our repository. Once we've filled out those fields, let's click the big green button that says "Create Repository". That will display a screen that looks like this:

![new repository created](./assets/new-repository-created.png)

The important line here is the one that says:

```
git remote add origin https://github.com/GITHUB_USERNAME/learning-git.git
```

We'll come back to that url in a moment, so keep this page open.

## Getting Set Up: Creating a Local Repository

In addition to a remote repository, we'll also need a local repository, or a copy of our project's code on our local machine. Our imaginary project doesn't have any content yet, so let's go ahead and make a directory on our machine in which we can store sample project files. To do so, you should be able to open a fresh terminal (on OSX) or Git Bash terminal (on Windows), and type:

```
cd Desktop
```

From there, you can create a new directory by typing:

```
mkdir learning-git
```

Then to move your terminal into that folder let's run:

```
cd learning-git
```

## Initializing a Git Repository

To tell Git that you want to carefully manage the files in a given directory (and its subdirectories), the first command to run is `git init`. That will return a line like the following, which confirms the current directory is ready for git commands:

![git init](./assets/git-init.png)

After initializing our current directory, let's run the most important Git command, `git status`. That command will return output that looks like this:

![git status](./assets/git-status.png)

This output tells us some important things:  
 * We're on the `master` branch (we'll discuss branches more below)  
 * We're preparing for our first commit (i.e. we haven't committed anything yet)  
 * There's nothing to "commit" in our directory--because it's empty!  

## Adding Files to Your Staging Area

Let's add a file to our working directory so we have something for Git to manage:

```
touch data.txt
```

That command will generate an empty text file named "data.txt" in your current working directory. After creating that file, let's re-run the `git status` command:

![git status after touch](./assets/git-status-after-touch.png)

Like above, this status informs us we're still on the master branch and are preparing to make our first commit. However, this git status output differs from the git status output above in one important way--we now have "untracked files"!

Untracked files are files that are present in a Git-enabled directory that have not been "added" to the directory's version control system yet To add a file to your directory's version control system, we can use the following command: `git add FILENAME`. For example, to add our data.txt file to our version control system, let's run:

```
git add data.txt
```

That command doesn't return anything on the terminal. To investigate the change we just made, let's run another `git status`. That returns:

![git status after add](./assets/git-status-after-add.png)

Here we see we have some "changes to be committed"--that is to say, we have some files in our Staging Area.

## Committing Changes to Your Local Repository

Once we have files in our staging area, we can "commit" to those changes and push those changes to our project repository. To commit our changes, we can run:

```
git commit -m 'add data file'
```

This command indicates that we wish to commit all changes in our staging area, and we wish to assign a <b>commit message</b> that says 'add data file'. The commit message is a brief note to yourself and your teammates that indicates what you changed in your commit. Once issued, that command returns the following output:

![git commit](./assets/git-commit.png)

## Pushing Your Local Repository to Your Remote Repository

After commiting your changes, you can push those changes to your remote repository to share the changes with your teammates. 

To do so, we first need to tell Git the address of our remote repository (i.e. the address of our GitHub repository). To do so, we can run the line that we copied above:

```
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/learning-git.git 
```

This line creates an alias named "origin" that points to the http address you specified (i.e. your github repository address). If you're curious, you can see where that alias is stored if you run `cat .git/config`, which will [display](./assets/git-config.png) your Git repository's internal configuration information in your terminal.

After creating an alias for your GitHub repository, you can push your changes to that repository by running:

```
git push origin master
```

This command indicates that you wish to push the `master` branch in your <b>local repository</b> to `origin`, an alias for your <b>remote repository</b> on GitHub.

If you then visit: `http://github.com/YOUR_USERNAME/learning-git` you should see your data file and your commit message:

![github after push](./assets/github-after-push.png)

Congratulations--you've just pushed some code to GitHub!

***
#### CHALLENGE

Given what we covered above, see if you can create a new file in your local repository, add that file to your staging area, commit your changes, and push your commit up to GitHub. Feel free to consult the notes above as you do so! 

***

## Understanding the Staging Area

In the example above, we added some files to our <b>staging area</b> by running `git add data.txt`. Let's further explore the <b>staging area</b> by changing our sample data file:

```
echo "hello git" > data.txt
```

If you now open data.txt in a text editor, you'll see that it now contains some content. If you run a `git status` command, you'll see that Git is aware your file changed:

![git status after modification](./assets/git-status-after-modification.png)

Let's add a new file as well:

```
touch secret.json
```

And run another `git status`:

![git status after add and modify](./assets/git-status-add-modify.png)

Here we see that we have made changes to our data.txt file, and have a new "untracked" file, secret.json. Let's add secret.json to our staging area:

```
git add secret.json
```

And run another `git status`:

![git status after add and modify](./assets/git-status-add-json.png)

Now let's suppose we want to remove secret.json from our staging area. To do so, we can use the `git reset` command:

```
git reset secret.json
```

And run another `git status`:

![git status after reset](./assets/git-status-after-reset.png)

As we can see, this removed secret.json from our staging area, which is now empty (hence the "no changes added to commit" in the git status response above).

This is just to say, we can add files to our staging area with `git add`, and can remove those files from our staging area with `git reset`.

***
#### CHALLENGE

Given what we covered above, see if you can add data.txt to your staging area, then see if you can remove it from your staging area. Once you're done, add all of your local files to your staging area and push them to GitHub.

***

## Pulling from a Remote Repository

So far we've made changes in our local respository and have then pushed those changes up to our remote repository on GitHub. Sometimes, however, your remote repository will have changes that are not present in your local repository. (For example, teammates could push changes to the remote repository, or you yourself might push changes to the remote repository from another machine.) In those situations, you'll want to "pull" those changes down to your local repository so that your local repository matches the remote repository.

Let's create some changes on your remote repository that aren't present in your local repository. To do so, let's navigate to `https://github.com/YOUR_USER_NAME/learning-git` and click the button that says "Create new file". Add a name and some content to your file then click the big green button at the bottom of the page that says "Commit new file". After doing so, you should see your new file in your repository.

If you run `ls` in your terminal, you'll note that that new file is not present in your local repository. Let's pull that file into your local repository. To do so, we can run:

```
git pull origin master
```

If you now run an `ls` in your directory, you'll see that it contains the file you added on GitHub:

![ls after pull](./assets/ls-after-pull.png)

Congratulations--you've just pulled content from your remote repository to your local repository!

***
#### CHALLENGE

Given what we covered above, see if you can add a file named README.md to your repository on GitHub, then see if you can pull that file into your local repository using Git.

***

## Getting Started With Branches

Each time we've run `git status` so far, the returned output has indicated that we're on the "master" branch. It's now time for us to discuss what this means.

Each "branch" in a Git repository is a separate representation of the data in the given repository. Different branches can have radically different ideas about what the given repository contains, and by switching between those branches, you can change the content that's displayed on the filesystem within the given repository.

To explore branches, let's create our first custom branch. We can do so by running:

```
git checkout -b my-new-branch
```

If you now run `git status`, you'll see that you're on a branch named "my-new-branch". Let's add some files to this branch:

```
touch a.txt b.txt c.txt
```

If you now run another `git status`, you'll see your new untracked files:

![new branch content](./assets/new-branch-content.png)

Let's add all those files to our staging area with a nice Git shorthand, then commit them all:

```
git add .
git commit -m 'add additional sample files'
```

After commiting those files, let's change back to the master branch and check the files present on the master branch:

```
git checkout master
ls
```

After running that `ls` command, you'll see that your new files (a.txt, b.txt, and c.txt) are missing! That's because you added them inside the branch named `my-new-branch`, not the `master` branch. Let's checkout to the branch with the files and show that they're still there:

```
git checkout my-new-branch
ls
```

That should show the files are indeed still present. Try toggling back and forth a few times between the "master" branch and the branch named "my-new-branch". Run some `ls` commands as you do so in order to investigate the content in each branch:

![changing branches](./assets/changing-branches.gif)

As we can see, each branch contains a distinct representation of the project content. That's important, because it allows you to keep one polished version of your codebase in your master branch, and allows you to experiment with new features in other branches without fear of ruining your master branch code.

## Merging Branches in Your Local Repository

There are two ways to combine content from branches. The first is to use the `merge` command:

```
git checkout master
git merge my-feature-branch
```

This will return output similar to the following:

![merge results](./assets/merge-results.png)

This response indicates that three new files were created in our master branch. Those files come from "my-new-branch" of course. By "merging" that branch into master, we ask Git to automatically combine the files in the two branches. Often times Git can do so without any trouble, as it is the case above. If Git can't automatically merge your branches, you will need to manually resolve any "merge conflicts" (see [here](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/) for a brief guide).

## Merging Branches on GitHub

Another way to merge branches is to push your new branch up to GitHub, then use GitHub to merge your new branch. Let's practice this technique.

First, let's make a new branch, make some changes in that branch, and commit those changes:

```
git checkout -b awesome-feature
touch server.js
git add server.js
git commit -m 'initial commit of server'
```

Now let's push that branch up to GitHub:

```
git push origin awesome-feature
```

The structure of this command is as follows:

```
git push DESTINATION BRANCH_TO_PUSH
```

After running that command, let's go back to your repository on GitHub. On your user page you should see a little yellow box with your new branch:

![new branch on github](./assets/new-branch-on-github.png)

Let's click the big green button that says "Compare & pull request". On the next page, click the big green button that says "Create pull request", and on the subsequent page, click the green button that says "Merge pull request". Congrats--you've just merged some branches!

***
#### CHALLENGE

Given what we covered above, see if you can add a file named README.md to your repository on GitHub, then see if you can pull that file into your local repository using Git.

***

# Group Activity: Building a Collaborative Madlib on GitHub

Finally, we come to our last task: contributing to open source projects on GitHub. The Open Source community is built around voluntary contributions individuals make to code repositories. In your futures as developers, you may want to contribute to these projects. Let's discuss how you can do so.

Earlier we practiced merging changes in a repository that you created. In what follows we'll discuss merging changes into repositories that you didn't create. To get started, you'll first want to "fork" a repository to which you wish to contribute. For the sake of this exercise, let's fork the repository that hosts this README.md file by navigating to https://github.com/YaleDHLab/lab-workshops:

![preparing to fork](./assets/preparing-to-fork.png)

Once there, click the icon in the upper right-hand-corner that says "Fork". Forking a repository makes a copy of that repository in your username's account. To see the repository you forked, click on your user's icon in the upper-right-hand corner of the navigation bar. If you then click the "Repositories" tab, you should see the forked repo.

After forking the repository, let's "clone" the forked repository down to your local machine. To "clone" a repository is simply to copy that repository from one server to another. In this case we'll clone the repository from a GitHub server to your local machine:

```
cd ..
git clone https://github.com/YOUR_USERNAME/lab-workshops
cd lab-workshops
```

If you run an `ls` inside lab-workshops, you'll see all the content of the repository you cloned. Our task from here is to make some changes to a particular set of files in the repository. There's a catch, though! Those files are located in a branch named `gh-pages` of the lab-workshops repository. Let's checkout into that branch:

```
git checkout gh-pages
```

Once we're on the "gh-pages" branch, let's change into the directory of interest:

```
cd command-line-git/parts-of-speech/
```

If you run an `ls` command in that branch, you'll see three JSON files: `adjectives.json`, `nouns.json`, and `verbs.json`, each of which contains a list of examples of the given part of speech. For example, here are the contents of the `nouns.json` file:

```
[
  "banker",
  "Irishman",
  "princess",
  "taxi driver"
]
```

Your mission is to modify the contents of one of those files. Make sure the list of items you write match the given filename's part of speech. Once you're done, validate that your final file is indeed valid JSON by pasting your updated file [here](https://jsonlint.com/). Once you have validated your updated file, add and commit your changes:

```
git add .
git commit -m 'write a commit message here'
```

Then push your branch up to GitHub by running:

```
git push origin gh-pages
```

After pushing your branch, go back to the "lab-workshops" repository within your user account. If you click the "branches" icon on that page, you should see the "gh-pages" branch you just updated. Let's click "New pull request", then once again click "Create pull request" on the next page:

![creating a pull request](./assets/creating-pull-request.gif)

Now within the [repository](https://github.com/YaleDHLab/lab-workshops) you originally forked, we see a new pull request:

![new pull request](./assets/new-pull-request.png)

If the owners of that repository decide they like your proposed changes, they'll merge them into their repository.

In our case, the pull requests we're making will update the data fed into a [simple madlibs website](http://yaledhlab.github.io/lab-workshops/command-line-git/):

![ls after pull](./assets/madlibs.png)

As we merge your changes, we'll see the terms you added on the webpage :tada: :monkey: :thumbsup:

Congratulations--you're now a contributor on an Open Source project!

# Going Further with Git

The following notes are meant to help resolve problems you might encounter in your future with Git.

#### Storing Your GitHub User Information

Rather than type out your GitHub username and password when pushing code to GitHub, it's helpful to save this information on your system. To do so, you can run:

```
git config --global user.name "YOUR_GITHUB_USERNAME"
git config --global user.email "YOUR_GITHUB_PASSWORD"
```

#### Multiple Git Users on One Machine

If there are multiple Git users on one machine, you can use the following syntax to explicitly state the username and password of the user who will perform a push or pull action:

```
git push https://YOUR_GITHUB_USERNAME:YOUR_GITHUB_PASSWORD@github.com/YOUR_USER_NAME/lab-workshops gh-pages
```

#### Reviewing Your Git History

To review all commits made in your repository and their associated commit messages, we can run `git log`:

![git log](./assets/git-log.png)

To exit that view, just hit `q`.

#### Cleaning Up Old Branches

To list all branches in your repository, you can run:

```
git branch -a
```

To delete a given branch, you can run:

```
git branch -D BRANCH_NAME
```

To delete all merged branches, you can run the following (make sure you undstand the command before you run it!):

```
git branch --merged | egrep -v "(^\*|master|gh-pages)" | xargs git branch -d
```

# Questions? Difficulties?

If you have questions about Git or programming more generally, or would like help with your programming tasks, please feel free to stop by Yale's Digital Humanities Lab in Sterling Memorial Library, 316 during office hours--Tuesdays and Wednesdays 2-4.