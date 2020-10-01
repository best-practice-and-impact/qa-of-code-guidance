# Version control

In this chapter, we primarily discuss the benefits of using the [Git](https://git-scm.com/) version control system.


## Rationale

### Why do we need version control

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


### What should I version control

You should include any code that is required to run your system, but that is not sensitive.

You shouldn't include the following in your code repository:
* passwords, credentials or keys
* configuration files that are environment-dependent
* code that contains sensitive information
  * for example, code that describes a method for fraud detection
  * or code that contains references to personally identifiable data
* data, except for small example datasets

You might include example configuration files, or documentation describing how configuration is applied.
However, the exact configuration of a system for a particular run of your code should be recorded by logging for reproducibility purposes.

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

A `.gitignore` file tells git not to version specific patterns of file names.
* useful for ensuring that specific files or types are not included. Such as configuration files or data.

Commits are collections of changes to one or more files.
* are attributed to the author of these changes
* each commit has a unique hash associated to it, which has a long (e.g. `121b5b4f18231e4ee32c9c61f6754429f9572743`) and short version (e.g. `121b5b4`)
* also have an associated message that is used to describe the changes - this is a key part of the audit trail

See this model commit message from [A note about Git commit messages](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html):

``` {code-block}
Capitalized, short (50 chars or less) summary

More detailed explanatory text, if necessary.  Wrap it to about 72
characters or so.  In some contexts, the first line is treated as the
subject of an email and the rest of the text as the body.  The blank
line separating the summary from the body is critical (unless you omit
the body entirely); tools like rebase can get confused if you run the
two together.

Write your commit message in the imperative: "Fix bug" and not "Fixed bug"
or "Fixes bug."  This convention matches up with commit messages generated
by commands like git merge and git revert.

Further paragraphs come after blank lines.

- Bullet points are okay, too

- Typically a hyphen or asterisk is used for the bullet, followed by a
  single space, with blank lines in between, but conventions vary here

- Use a hanging indent
```

Branches
* independent copies of a project's history, copied from the state of the parent branch at a specific point in that branches history
* help to support multiple changes to a project that are developed in parallel
* `master` is the default name for the original branch of a repository, however, some platforms are changing this default to `main`

`HEAD`
* refers to the current state of the current branch
* usually indicates the last commit that was created or checked out
* `HEAD` and other references are described in more detail in [References section of the Git book](https://git-scm.com/book/en/v2/Git-Internals-Git-References)

Merge
* recreating changes from one branch on another
* can be done using a few different methods, including fast-forward and rebasing

Conflicts
* when multiple changes have been made to the same part of a file
* you must indicate which change (or combination of changes) should be retained

Don't panic
* it's easy to make mistakes, but thankfully Git's audit trail means that we can always revert back to working versions
* [stackoverflow](https://stackoverflow.com/) is your friend

Don't change published (i.e. `remote`) history
* otherwise you might need to panic
* causes issues across versions of the repo, as other developer's local copies may no longer contain the same history
* consider this before force pushing changes to a remote repository
* instead create new commits that resolve or revert to fix the problem

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

Once tags have been created, these locations in the projects history can be easily recovered by either checking out:

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
* Project boards
* Forking
* Pull requests
* Continuous Integration

Many of these project management tools are also discussed on the [GitHub features page](https://github.com/features/project-management/).

### Access management

GitHub repositories have a [visibility setting](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/setting-repository-visibility) that represents whether the a repo can be viewed publicly or only by owners of the project,
Note that some GitHub features are limited or are not available for private repos on free GitHub accounts.

Organizations provide an area for collating multiple repos that are associated with a particular team or department.
Within Organizations, Teams can be also created to manage view and contribution permissions for projects within the Organization.
External collaborators can also be added to projects, to allow direct contribution from those outside of the Organization.

Despite the visibility status of a repo, only Organization members and collaborators may make direct contributions to the code in the repo.
Others can contribute by Pull Request.

Detailed setup and management of Organizations and Teams are described in the [relevant section of the GitHub Docs](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-organizations-and-teams).


### Forking

Forking a repo takes a complete copy of a project's current state, including all existing branches and tags.
You can then make modifications on this copy, without affecting the original repo.

You might want to do this because you:
* Would like to contribute to a repository, but are not added to the repo as a collaborator
* Would like to make changes to the project for your own use

```{figure} https://camo.githubusercontent.com/0d56371e0d1dd02c072aa6c782275bdddedfa179/687474703a2f2f692e696d6775722e636f6d2f6833757477494b2e706e67
---
width: 30%
name: fork
---
Fork me on GitHub banner, commonly seen on project documentation
```

Note that forks do not automatically synchronise with the original repo.
This means that changes to the original repo after you create a fork need to be manually synchronised if you want to include them in your repo.
When you would like to offer to contribute your changes to the project (see Pull requests below), you should ensure that you synchronise your branch with any new changes first.

See the GitHub Docs for [instructions on forking a repo and keeping your fork up to date](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) with the project and also [working with forks](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/working-with-forks).


### Issues

Issues offer a method for requesting tasks, including enhancements and bugs in your project.

The basic elements of an issue are the:
* Title and description, provided by the person that submitted the issue
* Labels to categorise issues (e.g. bug)
* Comments, where others can discuss the issue
* Assignees that are working on resolving the issue

Issues can be linked to specific Pull Requests (below) that resolve or help to solve the issue.
They can also reference other related issues (e.g. `#12`), both within the repo and between repos.

Issues are useful for discussing bugs and new features within the team, but can also be added by users.
This is often the case with open source projects, providing users with a platform to highlight what would be most useful for them.

[Setting issue templates](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/configuring-issue-templates-for-your-repository) for your project can be an effective way of encouraging collaborators to use informative descriptions.
For example, a bug issue should include simple instructions to help maintainers reproduce the problem.
While feature requests might include information on how the user expects the new feature to work or details what problem it will help them to overcome.

Issues are a useful soundboard for requesting changes, but the implementation of changes are handled by Pull Requests (below).


### Pull requests

A Pull request lets you describe changes that you have made to a repo.
The request is based on the difference between a target branch (usually `dev` or `master`) and a source branch, where you have implemented changes.
The source branch can the in the same repository, or might be in a Fork (below) of the repository if you are not a member of the project.

Pull requests create an interface for discussion and review of your changes.
Once a project maintainer is happy with your changes, they can merge them onto the target branch.
After merging, pull requests preserve a record of the changes and associated discussion.

You can label pull requests a draft to indicate they are still a work in progress.
This prevents them from being merged prematurely.
This can be useful when you would like to request advice or early feedback on the changes you are making.

Like issues, pull requests can have assignees that are working on them.
You can also assign reviewers and tag (`@`) project collaborators as part of the discussion.


### Project boards

Project boards offer project management features through a [Kanban board](https://en.wikipedia.org/wiki/Kanban_board) interface.

These boards can be used to track assignment and progress of specific tasks.
This is aided by linking tasks to specific issues and pull requests.

### Continuous integration and continuous deployment

Continuous integration (CI) and deployment (CD) services help to automate repetitive tasks in development and operations (DevOps).

GitHub provides this service via [GitHub Actions](https://github.com/features/actions).
However, many other CI/CD provides can be integrated with GitHub projects.
Other commonly used services include:
* Jenkins
* Travis
* CircleCI
* AppVeyor

You can see a detailed example of CI/CI in practice in the `jupyter-book` project.
A recent version of the [`jupyter-book` CI configuration](https://github.com/executablebooks/jupyter-book/blob/6fb0cbe4abb5bc29e9081afbe24f71d864b40475/.github/workflows/tests.yml) includes:
* Checking code against style guidelines, using [pre-commit](https://pre-commit.com/)
* Running code tests over
  * a range of Python versions
  * multiple versions of specific dependencies (`sphinx` here)
  * multiple operating systems
* Reporting test coverage
* Check that documentation builds successfully
* Deploy a new version of the `jupyter-book` package to [PyPI](https://pypi.org/)

## Workflows

Adopting a particular workflow for Git can help to keep work consistent within a project.

Here we suggest a couple of workflows that might be used to version your analytical work.
You might not benefit from following these patterns to the the word, but should choose aspects of these to adopt a consistent workflow in your team.

These workflows are especially useful when working in a team, as they embed peer review into your workflow.

### Gitflow

In this workflow:
1. A development branch is created from the main branch.
2. All changes are reviewed as they are merged from individual feature branches onto this development branch.
3. Larger collections of changes are then merged from the development branch onto the main branch. These merges usually reflect a new version of functioning code.

We recommend that you use pull requests (or equivalents) to review changes that are merged onto the development and master branches.
This mode of release provides an extra opportunity for discussion and quality assurance, before changes are added to the most stable branch.

```{figure} https://wac-cdn.atlassian.com/dam/jcr:b5259cce-6245-49f2-b89b-9871f9ee3fa4/03%20(2).svg?cdnVersion=1273
---
width: 75%
name: gitflow
---
Branching diagram to demonstrate gitflow, from [Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).
```

This [Gitflow guide](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) from Atlassian describes the workflow, with useful images to depict branching.


### GitHub flow

In this workflow:
1. Feature branches are created directly from the main branch.
2. Pull requests (or equivalent) are used to review and discuss changes in this new branch.
3. Once reviewed, the feature branch can be deployed for user testing.
4. Once satisfied that the code works as required, the feature branch is merged onto the main branch.

This workflow might be more suited to projects with rapid development cycles.

```{figure} https://files.programster.org/tutorials/git/flows/github-flow.png
---
width: 75%
name: github_flow
---
Branching diagram to demonstrate GitHub, from [Programster's blog post of git workflows](https://blog.programster.org/git-workflows).
```

This simple guide from GitHub also outlines [GitHub flow](https://guides.github.com/introduction/flow/#:~:text=GitHub%20flow%20is%20a%20lightweight,Created%20with%20Snap).

## Other resources

* [GitHub's Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [GitHub Git Handbook](https://guides.github.com/introduction/git-handbook/)
* [Atlassian's Learn Git](https://www.atlassian.com/git)