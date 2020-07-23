# Documentation

## Introduction

This chapter covers a range of methods for documenting code and coding projects.

Key to the usefulness of all of these documentation types - when your code changes, you should ensure that all relevant documentation is also up-to-date.

## Code Documentation

### Comments ★☆☆☆☆

A common form of documentation is code comments, which are found throughout source code files.

Comments are useful for explaining the logic behind sections of your code.
However, excessive use of code comments often leads to redundancy and can ironically make reading your code more effortful.

````{tabs}

```{code-tab} py
# Set number_1 to 5
number_1 = 5

# Set number_2 to 9
number_2 = 9

# Set total to the sum of number_1 and number_2
total = number_1 + number_2
```

````

Comments that describe exactly **what** is occurring in the code, as above, are often not necessary.
They may be redundant, if [good naming practices](naming) are followed to self-document the steps that occur in your code.
A developer or user can read your code and other more appropriate forms of documentation (see [Docstrings]) for more detailed description of the logic behind your code.
If it is difficult to understand your code without comments, then this can be an indicator that your code is overly complex and might benefit from being refactored into smaller units.

Comments can used more effectively to explain **why** you might have used a particular method.
For example, explaining to other analysts/developers why a section of your code doesn't follow standard practices, perhaps because the typical method didn't work.
This type of comment may help to clarify your choice of logic, without needing to describe the individual steps taken.
Comments explaining **why** you made programming choices will help yourself and other developers to understand your intentions when writing the code.

````{tabs}

```{code-tab} py
# Insert demo of useful comments here


# Works around bug in function X
# TODO: Fix function x!

```

````

Another use of code comments, is to divide long sections of code into sub-sections that relate to their overall functionality.
For example, an analysis script might be broken down into sections that describe each part of the analysis process:

````{tabs}

```{code-tab} py
import pandas as pd
import matplotlib.pyplot as plt


## Get data
time_series = pd.read_csv("time_Series_data.csv")

## Filter data
ten_years = time_series.loc["2010:2020"]
ten_years_price = ten_years.loc[:, "price"]

## Analyse data
median_price = ten_years_price.median()
print("Median price: " + median_price)

## Produce figures
plt.plot(ten_years_price)
```

````

### Docstrings ★★☆☆☆

When your code is structured as functions or classes, these functional units can be efficiently documented using docstrings.
Docstrings are multi-line comments that appear at the start of a function definition.
Use of these comments keeps the documentation of your code closely associated with the relevant sections of code.
Docstrings commonly describe:

- what the function or class does
- what parameters the function or class takes as arguments
- what the code returns
- how to use section of code
- references to other functions or classes carry out similar tasks


````{tabs}

```{code-tab} py
def add_to_each_in_list(numbers, to_add):
    """
    Adds a number to each number in a list.

    Parameters
    ----------
    numbers : list
        Numbers to add `to_add` to.
    to_add : int or float
        Number to be added to each element of `numbers`.

    Raises
    ------
    TypeError
        if `numbers` is not a list.

    Returns
    -------
    new_numbers : list
       `numbers` with `to_add` added to each element.

    Examples
    --------
    >>> my_numbers = [2, 4, 6, 8]
    >>> add_to_each_in_list(my_numbers, 3)
    [5, 7, 9, 11]
    
    See Also
    --------
    add : Adds two numbers 
   """
   if not isinstance(numbers, list):
       raise TypeError("numbers must be a list")
   new_numbers = [number + to_add for number in numbers]
   return new numbers
```

```{code-tab} r
# Roxygen goes here!
```

````

In this typical example, the docstring starts with a brief description of the overall function.
It then lists the parameters that our function takes, along with the suggested type of each and a brief description.
It also tells us that the function will raise an error if the wrong type is provided for the first parameter.
Then there is a description of the object that is returned from the function, followed by an example of the function in use.
Finally, it references a similar related function.
This example follows the [numpydocs style](https://numpydoc.readthedocs.io/en/latest/format.html), which is particularly readable in code files.

You might find that writing function, class or package descriptions prior to writing their code helps you to focus on the desired task.
As documentation tends to be user-focussed, this approach also helps you to keep the user's needs in mind when developing code.


Other useful resource include:

- [Python docstring convention](https://www.python.org/dev/peps/pep-0257/)
- Guidance for [documenting objects and functions in R](http://r-pkgs.had.co.nz/man.html)


### Automatic Documentation Generation ★★☆☆☆

Sadly this section does not describe a tool that miraculously writes your documentation for you (though tools for [auto-completing your code](https://kite.com) do exist!).
It does, however, describe tools that automate generation of searchable, user-friendly HTML documentation.
You should ensure that the resulting documentation remains associated with the source code of your project.

Great, so you've embedded documentation into your code, in the form of docstrings (above).
These docstrings are ideal for technical users looking for a quick understanding of how to use your code.
However, this is not the nicest format to read documentation in and it may require users to navigate the files containing the code to find the relevant documentation.
Thankfully tools are available to extract this information from your code and reproduce it in HTML.

We recommend the python package [sphinx](https://www.sphinx-doc.org/en/master/) for generating HTML documentation.
Sphinx primarily uses the [reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) markup language.
Sphinx supports code highlighting for multiple programming languages within a project, however, other tools may be required to automatically collate documentation from code for some languages.
You can format your documentation using an [existing theme](https://www.writethedocs.org/guide/tools/sphinx-themes/), or design your own.

In addition to building elegant documentation from your code, these tools can also run examples that are found within docstrings (see example in [Docstrings]).
These examples test that your documentation is accurate and up-to-date, but may also flag when your code does not work as expected.
In sphinx, python code examples can be tested using the [doctest extension](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html).

Tools for automatic documentation generation:

- The python package [sphinx](https://www.sphinx-doc.org/en/master/)
- The R package [Roxygen2](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) - generate classic R documentation (.Rd files)
- The R package [pkgdown](https://pkgdown.r-lib.org/articles/pkgdown.html) - generate web-based R documentation, using roxygen-style documentation
- [Natural Docs](https://www.naturaldocs.org/) - open source tool that supports 20 different programming languages
- [Doxygen](http://www.doxygen.nl/)
- [JavaDoc](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html)

Be sure to read the documentation for these tools, as you may need to use a particular docstring style or format that your choice of tool can detect.


## Project Documentation

Whether you're developing a package or collaborating on a piece of analysis, documenting your project makes it much easier for others to understand your goal and ways of working.

### README ★☆☆☆☆

When working on a collaborative or open coding project, it's good practice to describe an overview of your project in a README file.
This allows users or developers to grasp the overall goal of your project.
As well as a description of the project, it might include examples using your code or references to other associated projects.
This file can be any text type, including `.txt`, `.md`, and `.rst`, and can be associated with your automated documentation.


### Dependencies ★☆☆☆☆

The simplest way to document which packages your code is dependent on, is to record them in a text file.
This is typically called `requirements.txt`.

Python packages record their dependencies within their `setup.py` file, via `setup(install_requires=...)`.
You can get a list of your installed python packages using `pip freeze` in the command line.

R packages and projects record their dependencies in a DESCRIPTION file.
Packages are listed under the `Imports` key.
You can get a list of your installed R packages using the `installed.packages()` function.

[Environment management] tools are very useful for keeping track of software and package versions used in a project.


### User Desk Instructions ★☆☆☆☆

If your project it very user focussed, for example developing a statistic production pipeline, it is very important that the code users understand how to appropriately use your code.

These instructions should include:

- How to set up an environment to run your code (including how to install dependencies)
- How to run your code
- What outputs (if any) your code or system produces and how these should be interpreted
- What quality assurance has been carried out and what further quality assurance of outputs is required


### Contributing Guidance ★☆☆☆☆

When collaborating, it is also useful to outline the standards used within your project.
This might include particular packages that should used for certain tasks and guidance on the [code style](code-style) used in the project.

For example, see the CONTRIBUTING file from our [gptables package](https://github.com/best-practice-and-impact/gptables/blob/master/CONTRIBUTING.md):

```
# Contributing

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with the owners of this
repository before making a change.

## Pull/merge request process

1. Branch from the `dev` branch. If you are implementing a feature name it
   `feature/name_of_feature`, if you are implementing a bugfix name it
   `bug/issue_name`.
1. Update the README.md and other documentation with details of major changes
   to the interface, this includes new environment variables, useful file
   locations and container parameters.
1. Once you are ready for review please open a pull/merge request to the
   `dev` branch.
1. You may merge the Pull/Merge Request in once you have the sign-off of two
   maintainers.
1. If you are merging `dev` to `master`, you must increment the version number
   in the VERSION file to the new version that this Pull/Merge Request would
   represent. The versioning scheme we use is [SemVer](http://semver.org/).


## Code style

- We name variables using few nouns in lowercase, e.g. `mapping_names`
  or `increment`.
- We name functions using verbs in lowercase, e.g. `map_variables_to_names` or
  `change_values`.
- We use the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
  format for documenting features using docstrings.

## Review process

1. When we want to release the package we will request a formal review for any
   non-minor changes.
2. The review process follows a similar process to ROpenSci.
3. Reviewers will be requested from associated communities.
4. Only once reviewers are satisfied, will the `dev` branch be released.
```

In this case we have outlined our standard practices for using version control on GitHub, the code style that we are using in the project and the review process that we follow.
We have used the [Markdown](https://daringfireball.net/projects/markdown/syntax) (`.md`) markup language for this document, which is formatted into HTML when viewed on our repository.


### Vignettes ★★☆☆☆

Vignettes are a form of supplementary documentation, containing applied examples that demonstrate the intended use of the code in your project or package.
Docstrings may contain examples applying individual functional units, while vignettes may show multiple units being used together.
The term vignette is usually used with reference to R packages, for example this introduction to the [{dplyr} package](https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html) for data manipulation.
However, the same long-form documentation is beneficial for projects in any programming language.

We've seen that docstrings can be used to describe individual functional code elements.
Vignettes provide a demonstration of the intended use for these classes and functions, in a realistic context.
This can help users to understand how different code elements interact, and how they might use your code in their own program.

Another good example is this vignette describing [how to design vignettes](http://r-pkgs.had.co.nz/vignettes.html) in Rmarkdown.
You can produce this type of documentation in any format, though Rmarkdown is particularly effectively at combining sections of code, code outputs and descriptive text.

You might also consider providing these examples in an interactive notebook, that users can run for themselves.


### Versioning ★★☆☆☆

[Semantic versioning](https://semver.org/) provides useful rules for versioning releases of your code.
Following these rules helps a user of your code to understand how changes in your code may affect their software.
Each level of version number indicates the extent of changes to the application programming interface (API) of your code, i.e. the code that a user interacts with directly.
Changes to the major version number indicate changes to the API that are not compatible with use of previous versions of the code.
While changes is the minor and patch numbers indicate changes that are either compatible or have no effect on the use of the code, respectively.


```{figure} ../_static/semantic_versioning.png
---
width: 70%
name: semantic_versioning
---
[Semantic versioning](https://semver.org/)
```


### Changelog ★★☆☆☆

A changelog records the major changes that have occurred to a project or package, between versioned releases of the code.

```
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2020-01-21
### Added
- `add_to_each_in_list()`
- online sphinx-generated documentation
- contribution guide

### Removed
- `subtract_to_each_in_list()`

### Changed
- Improved function documentation

### Fixed
- bug in `multiple_each_in_list()`, where output was not returned
```

Similarly to versioning, a changelog is useful for users to determine whether an update to your code is compatible with their work which may depend on your code.
It can also document which parts of your code will no longer be supported in future version and which bugs in your code have been addressed.
Your changelog can be in any format and should be associated with your code documentation, so that it is easy for users and other contributors to find.

[keep a changelog](https://keepachangelog.com/en/1.0.0/) provides a simple but effective template for recording changes to your code.


### Copyright and Licenses ★★☆☆☆

Copyright indicates ownership of work.
All material create by civil servants, ministers, government departments and their agencies are covered by [Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/).
It is not essential to include a copyright notice on your work, but doing so can help to avoid confusion around ownership.

Licences outline the conditions under which others may use, modify and/or redistribute your work.
As such, including a licence with your code, is important for users and developers alike.

In government, we [support and promote open source](https://www.gov.uk/service-manual/service-standard/point-12-make-new-source-code-open) whenever possible.
[Open source](https://opensource.com/resources/what-open-source) software is software with source code that anyone can freely inspect, modify and enhance.
As a government analyst, you should aim to make all new source code open, unless justification can provided for withholding part of your source code.

Benefits of open sourcing our code include:

* Transparency - it doesn't get much more open than publishing documented methods for our analyses
* Sharing value - others can benefit from our work, either through use or demonstration of good programming practices
* Sharing opportunity - others can contribute to and help to improve our approaches
* Feels good - we regularly benefit from open source software, so it's nice to give something back
* Attribution - open sourcing your code through public version control (e.g. GitHub) creates a public record of your contributions

Please see the [Government Data Service (GDS) guidance](https://www.gov.uk/government/publications/open-source-guidance/when-code-should-be-open-or-closed) for help deciding when code should be open or closed.
Additional security concerns for coding in the open are addressed in further [GDS guidance](https://www.gov.uk/government/publications/open-source-guidance/security-considerations-when-coding-in-the-open).

Choice of open source licence, depends largely on how you would like others to be able distribute modified versions of your work.
[Government Data Service guidelines](https://gds-way.cloudapps.digital/manuals/licensing.html#use-mit) suggest the MIT licence for code and the OGL (Open Government Licence) for documentation.
