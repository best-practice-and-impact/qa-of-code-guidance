# Structuring your project

When you're designing your analysis it can be difficult to keep your thoughts tidy.
Analysis is often exploratory and subject to change.
This nature means that scripts and programs can become messy.
The messier the programs, the harder they are to maintain and change in future.

Good directory structure and file hygiene can go a long way to mitigate this.
It will help others to read your code more easily, and you will write better code into the bargain.
Some structures have been found to be generally quite effective through trial and error.
Others are more specific, and - as with all guidelines - should not be taken as mandatory.


## Scripts

As you begin developing your project it's a good idea to save your working code in a script file.
In R these are saved as `.R` files, and in Python as `.py`.
Scripts can be used within an Integrated Development Environment (IDE) like [Visual Studio Code](https://code.visualstudio.com/), [RStudio](https://rstudio.com/), or [PyCharm](https://www.jetbrains.com/pycharm/).
Inside an IDE you can usually run through your script line-by-line, or run the whole file at once.
This can be an easier workflow than running code in the Python or the R console and then rewriting the same code in a script later.

Scripts serve as the basic units of saved code.
Often, we like to define functions or reusable bits of code in one file and then use these in another file.
For example we may write a few functions that help us to calculate `mean`, `mode`, and `median` of our dataset in the `functions.R` file.
Then we can use those functions in our main script, saved in `main.R`.

Outside of an IDE you can also run your scripts using the Python or R interpreters from the command line.
This allows other programs to use your scripts.
For example you can use the `Rcmd <script-path>` command to run your R scripts or the `python <script-path>` command to run your Python scripts.

Running your analysis files from end to end ensures that your code is executed in the same order each time.
It also runs the code with a clean environment, not containing variables or other objects from previous runs that can be a common source of errors.


## Clean directories

As your analysis project grows it becomes more important to keep your project structure clean.
Every project is different and the right way to organise your project might differ from another project.
However, there are some principles that are useful to consider.

### Filenames

Much like names of elements in your code, good filenames inform you of the purpose of a file.
Within a project, you should follow a standard file naming convention.
Good naming practices improve your ability to locate and identify the contents of files.

Good naming conventions include:
* Consistency, above all else
* Short but descriptive and human readable names
* No spaces, for machine readability - underscores (`_`) or dashes (`-`) are preferred
* Use of consistent date formatting (e.g. [YYYY-MM-DD](https://en.wikipedia.org/wiki/ISO_8601))
* Padding the left side of numbers with zeros to maintain order -  e.g. `001` instead of `1`. The number of zeros should reflect the expected number of files.

When using dates or times to name files, start with the largest unit of time and work towards the smallest.  So we would use `2020-10-15_data_input`, and not `15-10-2020_data_input`.
This will ensure that the default ordering of these files is in chronological order.
This makes it much easier to find the earliest or latest files.

You should start filenames with numbers to order files, if ordering is logical and informative.
For example, where the `001_introduction` should come before `002_methodology` and `003_results`.


### Analysis is a DAG

Analysis can best be thought of as a Directed Acyclic Graph (DAG).
Don't let the name scare you off!
All we mean by this is that you start off with the input data, you finish with the output(s), and in between there are no lines that link backwards.

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Tred-G.svg/800px-Tred-G.svg.png
---
width: 50%
name: dag
alt: Analysis is a directed, acyclic graph that links the input data through a series of steps to the outputs.
---
Defining analysis as a DAG - linking the input data at (a) to the output at (e).
```

When thinking about how to structure your project it is useful to think in terms of what your project's DAG looks like.
Each project should be kept in its own folder, with a descriptive name.
Most analysis will have an ingest or input stage, a processing stage, and a reporting stage.
You should use folders within each project to separate raw data, documentation, source code (or `src`) and results.

A typical analytical project folder might look like:

```
|-- README.md
|-- requirements.txt
|-- data/
|   -- incident_counts.csv
|-- docs/
|   -- notebook.md
|   -- manuscript.md
|   -- changelog.md
|-- results/
|   -- incident_counts_by_age.csv
|   -- incidents_over_time.svg
|-- src/
|   -- data_cleaning.py
|   -- main_analysis.py
|   -- generate_plots.py
```

Where you have written code that is used by multiple projects, this code should reside in its own separate folder.
This will allow you to record changes to your code independent of other dependencies of each project.


### Raw data should be preserved

You should not alter raw data - treat it as read-only.
Even data cleaning should take place on a copy of the raw data, so that you can document which cleaning decisions have been made.

There must be an immutable store for raw data in your project structure.


### Outputs should be disposable

You should be able to dispose of your outputs, deleting them, without worrying.
If you are worried about deleting your outputs (i.e. results) then it is unlikely you have confidence in being able to reproduce your results.

It is good practice to delete and regenerate your outputs frequently when developing analysis.


## Modules and packages

Code that is more complex, high risk or reusable between projects can benefit from being structured into a package.
Modules are single files that contain one or more reusable units of code.
Multiple related modules are typically collected together within a package.

It's likely that you've already used a package written by somebody else as part of your analysis.
For example, installing additional functionality for Python using `pip install <package>` on the command line or running `install.packages("<package>")` in an R interpreter.

```{admonition} Key Learning
:class: admonition-learning

[The Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.io/) describes good packaging practices using the most up-to-date Python tools. While [the R Packages book](https://r-pkgs.org/) provides a comprehensive summary of packaging in R. [The rOpenSci packaging guide](https://devguide.ropensci.org/building.html) also contains useful tips for packaging in R.
```

See [](project_documentation.md) for a summary of common package and project documentation types.


## Project templates

Although project structure is flexible, you might recognise that many analysts choose to use similar structures for multiple projects.
Consistency in structure makes it easier to navigate unfamiliar projects.
It means that members of the team can quickly orient themselves when joining an existing project or starting a new one.

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a command-line tool that creates projects from templates (cookiecutters).
Using an existing cookiecutter, or creating one to meet your needs, can be a useful way to increase consistency in structure between your projects.
It can save time by creating common folder structures, laying out essential documentation or even starting off your code with a basic boilerplate.
Laying out a structure to include documentation and code testing encourages these good practices.

Useful cookiecutters include:
* The government data science [govcookiecutter](https://github.com/ukgovdatascience/govcookiecutter), including data security features.
* The comprehensive Python data science project template [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/).
* The Python package template [cookiecutter-pypackage](https://cookiecutter-pypackage.readthedocs.io/en/latest/).

Rstudio provides a standard template for R packages via `File > New Project... > New Directory > R Package`.  We have created some basic templates for an [R package](https://github.com/best-practice-and-impact/example-package-r) and a [Python package](https://github.com/best-practice-and-impact/example-package-python) that may be helpful.
R project structures can also be set up or extended, one component at a time, using the [`usethis` workflow package](https://usethis.r-lib.org/).
For example, `use_test()` will add the directories necessary for testing using `testthat` and generate basic test file templates for a given function name.


## Repositories

Repositories or 'repos' are typically project folders that are version controlled using Git or a similar version control system.
One repository usually contains a single project.
Developing your project using a version controlled repository has significant benefits for reproducibility.

See [](version_control.md) for more information.
