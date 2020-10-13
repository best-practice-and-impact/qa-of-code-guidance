# Structuring your project

When you're designing your analysis it can often be difficult to keep your thoughts tidy.
Analysis is often exploratory and subject to change.
This nature means that scripts and programs can become messy.
The messier the programs, the harder they are to maintain and change in future.

Good directory structure and file hygiene can go a long way to mitigate this.
Not only will it help others read your code easier but you will write better code.
Some structures have been found to be pretty general through trial and error.
Others are more specific, and - as with all guidelines - should not be taken as mandatory.


## Scripts ★☆☆☆☆

As you begin developing your project it's a good idea to save your working code in a script file.
In R these are saved as `.R` files, and in Python as `.py`.
Scripts can be used within an IDE (integrated development environment) like [Visual Studio Code](https://code.visualstudio.com/), [RStudio](https://rstudio.com/), or [PyCharm](https://www.jetbrains.com/pycharm/).
Inside an IDE you can usually run through your script line-by-line, or run the whole file at once.
This can be an easier workflow than running code in the Python or R console and then rewriting the same code in a script later.

Scripts serve as the basic units of saved code.
Often, we like to define functions or reusable bits of code in one file and then use these in another file.
For example we may write a few functions that help us to calculate `mean`, `mode`, and `median` of our dataset in the `functions.R` file.
Then we can use those functions in our main script, saved in `main.R`.

Outside of an IDE you can also run your scripts using the Python or R interpreters from the command line.
This allows other programs to use your scripts.
For example you can use the `Rcmd <script-path>` command to run your R scripts or the `python <script-path>` command to run your Python scripts.

Running your analysis files from end to end, ensures that your code is executed in the same order each time.
It also runs the code with a clean environment, not containing variables or other objects from previous runs that can be a common source of errors.


## Clean directories ★☆☆☆☆

```{todo}
Content for clean directories
```


### Analysis is a DAG


### Raw data should be preserved


### Outputs should be disposable


## Modules and packages ★★☆☆☆

Code that is more complex, high risk or reusable between projects can benefit from being structured into a package.
Modules are single files that contain one or more reusable units of code.
Multiple modules might be collected together into a package.

It's likely that you've used another package as part of your analysis.
For example, installing them for Python using `pip install <package>` on the command line or running `install.packages(<package>)` in an R interpreter.

```{admonition} Key Learning
:class: admonition-learning

The [Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.io/) describes good packaging practices using the most up-to-date Python tools.
[R Packages](https://r-pkgs.org/) provides a comprehensive summary of packaging in R.
This [step by step guide to creating R package](http://web.mit.edu/insong/www/pdf/rpackage_instructions.pdf) from MIT might also be useful.
```

See [](project_documentation.md) for a summary of common package and project documentation types.


## Project templates ★★☆☆☆

Although project structure is flexible, you might recognise that many analysts choose to use similar structures between projects.
Consistency in structure makes it easier to navigate unfamiliar projects.

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a command-line tool that creates projects from templates (cookicutters).
Using an existing cookiecutter, or creating one to meet your needs, can be a useful way to increase consistency in structure between your projects.
It can save time by creating common folder structures, laying out essential documentation or even starting off your code with basic boilerplate.
Layout out a structure to include documentation and code testing encourages these good practices.

Useful cookiecutters include:
* The comprehensive Python data science project template [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/)
* The Python package template [cookiecutter-pypackage](https://cookiecutter-pypackage.readthedocs.io/en/latest/)

Rstudio provides a standard template for R packages via `File > New Project... > New Directory > R Package`.
R project structures can also be set up or extended, one component at a time, using the [`usethis` workflow package](https://usethis.r-lib.org/).
For example, `use_test()` will add the directories necessary for testing using `testthat` and generate basic test file templates for a given function name.


## Repositories ★★☆☆☆

Repositories or "repos" are typically project folders that are version controlled using Git or a similar version control system.
One repository usually contains a single project.

See [](vsetion_control.md) for more information.

```{todo}
Alex, any more expected here?
```
