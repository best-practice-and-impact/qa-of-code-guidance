# Version control

In this chapter, we primarily discuss the benefits of using the [Git](https://git-scm.com/) version control system.

## Why version control?

Manually versioning files is not appropriate or sufficient for development at pace or with input from multiple individuals.

Without automated version control, we commonly see:
* Multiple copies of files or the entire project
* Issues in resolving multiple changes to the same file
* Duplicated effort
* Difficulty understanding where changes have been made and by whom
* Difficulty understanding the order that changes have occurred in
* Difficulty identifying changes that have introduced errors
* Problems in trying to roll back changes to get code working again quickly

```{figure} https://imgs.xkcd.com/comics/documents.png
---
width: 30%
name: file_names
alt: Comic demonstrating poor file naming, like "Untitled 138 Copy.docx".
---
Documents, from [xkcd](https://xkcd.com/1459/)
```

As discussed in [](principles.md), an audit trail is essential for quality analysis.

It's important for us to be able to answer the following questions about our analysis:
* What changes have been made to our project?
* When were those changes made?
* Why were those changes made?
* Who made those changes?

Version control software, like Git, records the answers to these questions throughout the development of a project. Using a remote Git repository maintains a single source of truth, despite multiple individuals working on a project. It helps us to record and combine changes from multiple developers. When used effectively, it also allows us to more easily identify changes that have negatively impacted our work and remove them. Most importantly, it allows us to refer to specific versions of our code that have been used to produce specific outputs.


## What should I version control?

Ideally, you should include any code that is required to run your system.
In a public repository, you may need to omit confidential or sensitive code.

```{caution}

You should **not** include the following in your code repository:
* passwords, credentials or keys
* configuration files that are environment-dependent
* code that contains sensitive information
  * for example, code that describes a method for fraud detection
  * or code that contains references to personally identifiable data
  * or code that might compromise security protocols
* data, except for small example datasets
```

See [](excluding-from-git) for details on how to mitigate the risk of including sensitive information in a Git repository.

You might include example configuration files, or documentation describing how configuration is applied. However, the exact configuration for a particular run of your code should be recorded by logging for reproducibility purposes.

The data we use for analysis is often unreleased or sensitive. Unpublished, sensitive or disclosive data should never be shared in a code repository. As a rule of thumb, only small dummy/example datasets should be include. It is still important to version the data that we use for our analyses, but this can be done more appropriately using databases.


## Git

Git is a distributed version control system. All users have access to a complete and self-contained history of changes to a given project. It can be used to record local changes, with the option of then synchronising these changes with a central, remote repository. Remote repositories are typically on a platform like GitHub or GitLab.

The following sections describe useful concepts for using Git to version control your analysis. We use examples of Git commands throughout, but do not provide detailed descriptions of Git usage. If you're not yet familiar with using Git, you should first look into [introductory training](git-learning).


### Good branching

Branches are independent copies of a project's history, copied from the state of the parent branch at a specific point in that branches history. They help to support development of multiple changes to a project in parallel.

The `main` or `master` branch is the default highest level branch. This branch commonly reflects the code that is in production and should be considered as the most stable branch. Stability here, means that the code on this branch builds and functions as expected.

Needs to be proportional to complexity and number of collaborators.


Depth of branches generally match the level of stability in the code. As code becomes more stable, it is merged onto higher level branches.

As code is refined, it becomes safer to merge it onto a higher level branch. For example, when the code seems to work and has been suitably tested, we don't expect it to break the code on the next branch up.


### Commit standards

Commits are collections of changes to one or more files in a repository. Every commit is attributed to the author of the changes, providing an audit trail. Each commit has a unique hash - or identifier - associated with it, which has a long (e.g. `121b5b4f18231e4ee32c9c61f6754429f9572743`) and short version (e.g. `121b5b4`). These hashes allow us to refer to specific changes, but each commit also has an associated message that is used to describe the changes.

Most commit messages are short and informative, but in some cases you may want to provide more detail. Common standards follow this model commit message from ["A note about Git commit messages"](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html):

```{code-block} text
Capitalized, short (50 chars or less) summary

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of an email and the rest of the text as the body. The blank
line separating the summary from the body is critical (unless you omit
the body entirely); tools like rebase can get confused if you run the
two together.

Write your commit message in the imperative: "Fix bug" and not "Fixed bug"
or "Fixes bug". This convention matches up with commit messages generated
by commands like git merge and git revert.

Further paragraphs come after blank lines.

- Bullet points are okay, too

- Typically a hyphen or asterisk is used for the bullet, followed by a
  single space, with blank lines in between, but conventions vary here

- Use a hanging indent
```
(excluding-from-git)=
### Avoid commiting sensitive information to Git repositories

Code itself is very rarely sensitive, so we should be open to sharing it.
However, analysts may often want to use sensitive information in their analysis.
This might be in the form of credentials, used to access a service, or data that contains personally identifiable information.

In these cases, we need to minimise the risk of inadvertently sharing this information with our code.
This subsection suggests how you might mitigate this risk in your analysis.


#### .gitignore files

As mentioned above, you may not want to include all of the files associated with your project in a Git repository.
A `.gitignore` file allows you to exclude folders or files from being tracked by Git.
Within this file, you provide a list of text patterns.
If a folder matches one of your `.gitignore` file patterns, none of the files or folder below that folder will be tracked.
If an individual file matches one of the patterns, this file will not be tracked.

Given this example `.gitignore` file:

```
secrets.yaml
sandpit/
*.csv
```

The first pattern tells Git to ignore any file with the exact name `secrets.yaml`.
The second will ignore all files within a folder named `sandpit/`.
Note that if there are multiple folders in the project named `sandpit/`, they will all be excluded.
You should make the pattern more specific if you want to exclude particular directories.
The third pattern will exclude all `.csv` files, regardless of which folder or sub-folder they are in.

```{caution}
Files that are already being tracked by Git will not be excluded when you add new patterns to your `.gitignore` file.
Ensure that you set up your `.gitignore` before adding files to be tracked in your repository.
```

Please see the [Git documentation for `.gitignore`](https://git-scm.com/docs/gitignore) for more details.

While we may not want to share files containing credentials, configuration and data, it can be useful to provide dummy examples of these files.
Demonstrating the format of these files can help others to reuse your code, without sharing sensitive information.


#### Using environmental variables

If your code depends on credentials of some kind, these should not be explicitly written in your code.
They can be stored in configuration files, which should be excluded from version control, or better still in local environment variables.

Environment variables are variables which are available in a particular environment.
In this context, our environment is the user environment that we are running our code from.

In Unix systems (e.g. Linux and Mac), environment variables can be set in the terminal using `export` and deleted using `unset`:

```
export SECRET_KEY="mysupersecretpassword"
unset SECRET_KEY
```

In Windows, the equivalent to this is:

```
setx SECRET_KEY "mysupersecretpassword"
reg delete HKCU\Environment /F /V SECRET_KEY
```

Once stored in environmental variables, these variables will remain available on your machine until they are removed.
You can access this variable in your code like so:

````{tabs}

```{code-tab} py
import os

my_key = os.environ.get("SECRET_KEY")
```

```{code-tab} r R
my_key <- Sys.getenv("SECRET_KEY")
```

````

Note that you may need to open a new terminal to show that a variable has been removed.


#### Excluding `.Rdata` and `.Rhistory` files

R saves objects from your workspace (working environment) into an `.RData` file at the end of your session.
This can save time when reloading large objects into R, when returning to a project.
Depending on your settings, it may prompt you to ask if you would like to save them or it may do this automatically.
If you have read sensitive information into R during the session, this information may be saved to the `.RData` file.
As such, we must be careful not to include this information in commits to remote repositories.

Similarly, R stores a record of all commands executed in your session in a `.Rhistory` file.
If you have referenced sensitive information directly in your R commands, then this information will be written to the `.Rhistory` file.

To handle this, we can exclude these files (via `.gitignore`) or prevent R from generating them.
If you do not use these files, it is safest not to generate them in the first place.

In Rstudio, you can disable writing of these files via `Tools > Global options`:

* Under Workspace, select `Never` for `Save workspace to .RData on exit:`.
* Under History, deselect `Always save history`.


#### Jupyter Notebooks

By default, Jupyter Notebooks save a copy of the data that is used to create cell outputs.
For example, the data used to generate a chart, table or print a section of a dataframe.
This can be useful for sharing your code outputs without others needing to re-execute the code cells.

If you work with sensitive datasets in notebooks, this means that your notebooks may store sensitive data to display cell outputs.
If these notebooks are subsequently shared in code repositories, you may be making sensitive data available to unauthorised individuals.

It is [not currently possible to prevent the notebooks from retaining cell outputs](https://github.com/ipython/ipython/issues/1280).

The best way to handle this situation is to clear the outputs from your notebooks before commiting them to Git repositories.
This can be done from the notebook itself, by going to the menu `Cell > All > Output > Clear` and then saving your notebook.
Alternatively, this can be done from the command line, by running this command with your notebook file path:

```
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace <notebook_file_path>
```

This approach is quite laborious and could easily be forgotten.
As such, we advise you to automate the cell clearing using [Git filter](https://git-scm.com/docs/gitattributes/#_filter) as follows.
First, we tell Git to set an attribute on our notebook files by creating a `.gitattributes` file in the root of our repo:

```
*.ipynb filter=jupyternotebook
```

We can then define our cleaning instructions in a `.gitconfig` configuration file:

```
[filter "jupyternotebook"]
    clean = jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace %f
    required
```

You can add this to your global `.gitconfig` or create a local `.gitconfig` file in the root of your repo.
If you create a new config in your repo, you must run the following in that repo:

```
git config --local include.path ../.gitconfig
```

This configuration will now run the notebook output cleaning command every time a change to an `.ipynb` file is added to your local repo.
You will need to then `git add` the file a second time to add the changes from the cleaning.
This should prevent notebook outputs from being included in commits to this repository.

If you adjust the filter at any point, you should run this command to apply the changes to existing files:

```
git add --renormalize .
```

This approach has been borrowed from [this blog post by Yury Zhauniarovich](https://zhauniarovich.com/post/2020/2020-10-clearing-jupyter-output-p3/).



### Versioning large files


### Handling data breaches via Git

If unauthorised individuals may access sensitive information through their accidental inclusion in a remote repository, this is a data breach.
For example, pushing credentials or sensitive data to a remote public GitHub repository.

To handle a data breach, you should:

1. Prevent further access to the information.
   * Restrict access of the repository to only those who should have access to the information. For example, make a public repository private.
   * Remove the offending files from the **commit history** of the repository. Note that commiting the deletion of the information alone will not suffice.
   * If credentials (passwords or keys) have been revealed, you should change these credentials.
   * Ask anyone that you know has access to the repository to delete their local copy and re-clone the cleaned remote repository.
2. Report the incident.
   * Record roughly how long the information was available for and the potential impact of releasing this information.
   * Inform the data owner of the breach.
   * Discuss the breach with the Data Protection Officer in your department. They should be able to advise you on the steps you should take to, according to your departments data security policy.
   * If the breach includes pre-publication statistics, you must also report the breach to the [Office for Statistics Regulation](https://osr.statisticsauthority.gov.uk/).

The [Pro Git book section on rewriting history](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) details methods for editing and deleting files from your repository's commit history.
The [BFG repo-cleaner tool](https://rtyley.github.io/bfg-repo-cleaner/) can be a simpler alternative to standard Git commands.


### Releases (tagging)

Regularly `commit`ing changes using Git helps us to create a thorough audit trail of changes to our project.
However, there may be discrete points in the history of the project that we want to mark for easy future reference.
Let's face it, hashes like `121b5b4` don't exactly roll off of the tongue.

Tags can be created in Git, to reference a specific point in the projects history.
A tag essentially acts as an alias for a commit hash.
You might use tags, for example, to mark a particular model version or a new software version to be released.
By default, tags will reference the current position in history (i.e. the latest commit or `HEAD`).

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


## GitHub


### Benefits


### Forking


### Making the most of Pull Requests

Pull requests support good branching. They provide an opportunity for review, before code is merged onto a more stable branch. This further reduces the likelihood of merging breaking changes onto our higher level branches.


### Efficient use of issues

### Other GitHub features