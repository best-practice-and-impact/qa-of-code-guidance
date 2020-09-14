# Version control




```{figure} https://imgs.xkcd.com/comics/documents.png
---
width: 30%
name: file_names
---
Documents, from [xkcd](https://xkcd.com/1459/)
```

In this chapter, we primarily discuss the benefits of using the [Git](https://git-scm.com/) version control system.


## Why do we need version control

As we mentioned in [](principles.md), 

It's important for us to be able to answer the following questions:
* What changes have been made to our project?
* Who made those changes?
* When were those changes made?
* What evidence directed these changes?

When used effectively, version control also allows us to identify changes that have negatively impacted our work and remove them.

Without version control, we commonly see:
* Duplicated effort across a team
* Multiple copies of each project
* Issues resolving multiple changes to the same files


## What should I version control





You shouldn't include the following in your code version control:
* passwords or keys
* configuration files that are environment-dependent
* code that contains sensitive information
  * for example, code that describes a method for fraud detection
  * or code that contains references to personally identifiable data
* data, except small example datasets



TODO: reference sections on data version control and logging


## Git



Git is a distributed version control system, which means that all users have access to a complete and self-contained history of changes to a given project.
This means that it can be used to record local changes, with the option of synchronising these changes with a central, remote repository.


The following sections describe useful concepts for using Git to version control your projects.
We use examples of Git commands throughout, but do not provide detailed examples on basic usage of Git.
If you're not yet familiar with using Git, you should first look into introductory training.
Useful resources for this are:
* The Learning Academy 
* The [Pro Git book](https://git-scm.com/book/en/v2) - starting with Git Basics
* Software Carpentry [Version Control with Git](https://swcarpentry.github.io/git-novice/) - an applied project
* Interactive online training with [Katacoda](https://www.katacoda.com/courses/git) or [Learn Git Branching](https://learngitbranching.js.org/)

### Git Commands

Git commands are run from the terminal, which is typically bash or a command prompt.

Commands have a very standard structure in Git, namely they always starts with `git` to run the command using the Git program.

Git commands are also made up of:
* a command name, which always follows `git` (e.g. `git status`)
* command arguments, which follow the command and can be put before or after any flags (e.g. `git clone https://github.com/pandas-dev/pandas.git`)
* optional flags
  * these can be long, starting with two dashes (e.g. `--no-edit`)
  * or short, starting with one dash (e.g. `-m`)
  * the `-h` flag can be used to get help for any command
* flag arguments, which follow any flags that take arguments (e.g. `git commit -m "my message"`)

You can use this handy [cheat-sheet](https://education.github.com/git-cheat-sheet-education.pdf) as a reference for the most common Git commands.


### Git versioning concepts


Repository
 - local vs remote

.gitignore

Commits
> Commit 

[A note about Git commit messages](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

HEAD
Branches
Merges
Conflicts

Don't panic

Don't change published history


### Releases (Tagging)

Regularly `commit`ing changes using Git helps us to create a continuous audit trail of changes to our project.
However, there may be discrete points in the history of the project that we want to mark for future reference.
For example, a particular model version or a new software version to be released.

Tags can be created in Git, to reference a specific point in the projects history.
By default, tags will reference the current position in history (i.e. the latest commit or HEAD).


```{code-block}
git tag -a v0.2.7 -m "Release version 0.2.7"
git push origin v0.2.7
```

You can also retrospectively tag an older commit, by providing that `commit`'s hash:

```{code-block}
git tag -a v0.1.0 -m "Release version 0.2.7" 9fceb02
```



## Beyond Git



### GitHub

GitHub is the world's leading software development platform.
It provides additional tools that support effective collaboration on coding projects


* Issues
* Project board
* Pull requests
* Continuous Integration
* Forking

