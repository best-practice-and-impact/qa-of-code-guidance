# Version control

In this chapter, we primarily discuss the benefits of using the [Git](https://git-scm.com/) version control system.


## Why do we need version control

Manually versioning files is not appropriate for development at pace or with input from multiple individuals.

Without automated version control, we commonly see:
* Multiple copies of files or the entire project
* Issues resolving multiple changes to the same file
* Duplicated effort
* Difficulty understanding the order that changes have occurred in
* Difficulty identifying changes that have introduced errors

```{figure} https://imgs.xkcd.com/comics/documents.png
---
width: 30%
name: file_names
---
Documents, from [xkcd](https://xkcd.com/1459/)
```

As discussed in [](principles.md), an effective audit trail is essential for reproducibility.

It's important for us to be able to answer the following questions about our analysis:
* What changes have been made to our project?
* When were those changes made?
* What evidence directed these changes?
* Who made those changes?

Version control software, like Git, records the answers to these questions through the development of a project.
Using a remote Git repository maintains a single source of truth, despite multiple individuals working on a project.
It helps us to record and combine changes from multiple developers.
When used effectively, it also allows us to more easily identify changes that have negatively impacted our work and remove them.
Most importantly, it allows us to refer to specific versions of our code that have been used to produce specific outputs.


## What should I version control

You should include any code that is required to run your system, but that is not sensitive.

You shouldn't include the following in your code repository:
* passwords, credentials or keys
* configuration files that are environment-dependent
* code that contains sensitive information
  * for example, code that describes a method for fraud detection
  * or code that contains references to personally identifiable data
* data, except for small example datasets

You might include example configuration files, or documentation describing how configuration is applied.
However, the exact configuration of a system for a particular run of your code should be recorded by logging.

The data we use for analysis is often unreleased or sensitive, so should not be shared in a code repository.
It is still important to version the data that we use for our analyses, but this can be done more appropriately using databases.


## Git

Git is a distributed version control system, which means that all users have access to a complete and self-contained history of changes to a given project.
This means that it can be used to record local changes, with the option of synchronising these changes with a central, remote repository.

The following sections describe useful concepts for using Git to version control your projects.
We use examples of Git commands throughout, but do not provide detailed descriptions of Git usage.
If you're not yet familiar with using Git, you should first look into introductory training.

Useful training resources for this are:
* [Intro to Git](https://learninghub.ons.gov.uk/course/view.php?id=532) - the GSS Analytical Learning course (GSS members only)
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
  *  note that the `-h` flag can be used to get help for any command
* flag arguments, which follow some flags that take arguments (e.g. `git commit -m "my message"`)

You can use this [cheat-sheet](https://education.github.com/git-cheat-sheet-education.pdf) as a reference for the most common Git commands.


### Git versioning concepts


A repository (often shortened to repo) is a collection files that are being versioned by Git.
* created by `init`ialising a new repo or `clone`ing an existing one
* a local repository is your self-contained copy of the project
* a remote repository is a centralised copy of a project that is often used as the truth

A `.gitignore` tells git not to version specific patterns of file names.
* useful for excluding configuration files, data and other files 

Commits are collections of changes to one or more files.
* are attributed to the author of these changes
* also have an associated message that is used to describe the changes
* most effective when they c
* each commit has a unique hash associated to it, which has a long (e.g. `121b5b4f18231e4ee32c9c61f6754429f9572743` ) and short version (e.g. `121b5b4`)


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


```{figure} https://i.stack.imgur.com/yRIIc.png
---
width: 80%
name: release_image
---
From [Imgur](https://i.stack.imgur.com/yRIIc.png)
```

Tags can be created in Git, to reference a specific point in the projects history.
A tag essentially acts as an alias for a commit hash.
By default, tags will reference the current position in history (i.e. the latest commit or HEAD).

An annotated tag might be created for a new software version like so:

```{code-block}
git tag -a v0.2.7 -m "Release version 0.2.7"
git push origin v0.2.7
```

You can also retrospectively tag an older commit, by providing that `commit`'s hash:

```{code-block}
git tag -a v0.1.0 -m "Release version 0.2.7" 9fceb02
git push origin v0.1.0
```

Once tags have been created, these locations in history can be easily recovered by either checking out:

```{code-block}
git fetch --all
git checkout tags/v0.1.0 -b new_branch_name
```

or cloning the tag:

```{code-block}
git clone https://github.com/<user>/<repo>.git --branch=v0.1.0
```


## Beyond Git - GitHub

A number of platforms extend the functionality of Git, to further improve collaborative working.

Here we describe some of the beneficial features supported by GitHub, the world's leading software development platform.
GitHub provides additional tools for collaborative workflows, including:
* Access management for viewing and contributing
* Issues
* Project board
* Pull requests
* Continuous Integration
* Forking

