# Project documentation

Whether you're developing a package or collaborating on a piece of analysis, documenting your project will makes it much easier for others to understand your goal and ways of working.


## README

When working on a collaborative or open coding project, it's good practice to describe an overview of your project in a README file.
This allows users or developers to grasp the overall goal of your project.
As well as a description of the project, it might include examples using your code or references to other associated projects.
This file can be any text type, including `.txt`, `.md`, and `.rst`, and can be associated with your automated documentation.

We suggest the following for a good README:
  
- Short statement of intent
- Longer description describing the problem that your project solves and how it solves it
- Basic installation instructions or link to installation guide
- Example usage
- Screenshot if your project has a graphical user interface
- Links to related projects


## Contributing guidance

When collaborating, it is also useful to outline the standards used within your project.
This might include particular packages that should used for certain tasks and guidance on the [code style](code-style) used in the project.
If you plan to have contributors from outside your organisation it is useful to include a code of conduct too.
Please [see GitHub](https://docs.github.com/en/github/building-a-strong-community/adding-a-code-of-conduct-to-your-project) for advice on creating a code of conduct.

For an example, see the CONTRIBUTING file from our [gptables package](https://github.com/best-practice-and-impact/gptables/blob/master/CONTRIBUTING.md):

`````{tabs}

````{tab} Markdown

```{code-block}
# Contributing

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with the owners before making a change.

## Pull/merge request process

1. Branch from the `dev` branch. If you are implementing a feature name it
`feature/name_of_feature`, if you are implementing a bugfix name it
`bug/issue_name`.
2. Update the README.md and other documentation with details of major changes
to the interface, this includes new environment variables, useful file
locations and container parameters.
3. Once you are ready for review please open a pull/merge request to the
`dev` branch.
4. You may merge the Pull/Merge Request in once you have the sign-off of two
maintainers.
5. If you are merging `dev` to `master`, you must increment the version number
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

````

````{tab} HTML

<h1>Contributing</h1>

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with the owners of this
repository before making a change.

<h2>Pull/merge request process</h2>

1. Branch from the `dev` branch. If you are implementing a feature name it
`feature/name_of_feature`, if you are implementing a bugfix name it
`bug/issue_name`.
2. Update the README.md and other documentation with details of major changes
to the interface, this includes new environment variables, useful file
locations and container parameters.
3. Once you are ready for review please open a pull/merge request to the
`dev` branch.
4. You may merge the Pull/Merge Request in once you have the sign-off of two
maintainers.
5. If you are merging `dev` to `master`, you must increment the version number
in the VERSION file to the new version that this Pull/Merge Request would
represent. The versioning scheme we use is [SemVer](http://semver.org/).


<h2>Code style</h2>

- We name variables using few nouns in lowercase, e.g. `mapping_names`
or `increment`.
- We name functions using verbs in lowercase, e.g. `map_variables_to_names` or
`change_values`.
- We use the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
format for documenting features using docstrings.

<h2>Review process</h2>

1. When we want to release the package we will request a formal review for any
non-minor changes.
2. The review process follows a similar process to ROpenSci.
3. Reviewers will be requested from associated communities.
4. Only once reviewers are satisfied, will the `dev` branch be released.
````

`````

In this case we have outlined our standard practices for using version control on GitHub, the code style that we are using in the project and the review process that we follow.
We have used the [Markdown](https://daringfireball.net/projects/markdown/syntax) (`.md`) markup language for this document, which is formatted into HTML when viewed on our repository.


## User desk instructions

If your project is very user focussed for one particular task, for example developing a statistic production pipeline for other analysts to execute, it is very important that the code users understand how to appropriately run your code.

These instructions should include:
  
- How to set up an environment to run your code (including how to install dependencies)
- How to run your code
- What outputs (if any) your code or system produces and how these should be interpreted
- What quality assurance has been carried out and what further quality assurance of outputs is required
- How to maintain your project (including how to update data sources)


## Dependencies

The environment that your code runs in includes the machine, the operating system (Windows, Mac, Linux...), the programming language, and any external packages.
It is important to record this information to ensure reproducibility.

The simplest way to document which packages your code is dependent on, is to record them in a text file.
This is typically called `requirements.txt`.

Python packages record their dependencies within their `setup.py` file, via `setup(install_requires=...)`.
You can get a list of your installed python packages using `pip freeze` in the command line.

[R packages](https://r-pkgs.org/) and projects record their dependencies in a [DESCRIPTION](https://r-pkgs.org/description.html) file.
Packages are listed under the `Imports` key.
You can get a list of your installed R packages using the `installed.packages()` function.

Environment management tools, such as [`renv`](https://rstudio.github.io/renv/articles/renv.html) for R or [`pyenv`](https://github.com/pyenv/pyenv) for python, are very useful for keeping track of software and package versions used in a project.


## Citation

For research or analytical code that is likely to be referenced by others, it can be helpful to provide a citation template.
This can be included in your code repository as a `CITATION` file or part of your `README`.
For example, the R package `ggplot2` provides the following:

```
 To cite ggplot2 in publications, please use:

 H. Wickham. ggplot2: elegant graphics for data analysis. Springer New York,
 2009.

A BibTeX entry for LaTeX users is

@Book{,
   author = {Hadley Wickham},
   title = {ggplot2: elegant graphics for data analysis},
   publisher = {Springer New York},
   year = {2009},
   isbn = {978-0-387-98140-6},
   url = {http://had.co.nz/ggplot2/book},
 }
```

This might include multiple citations, if your project includes multiple datasets, pieces of code or outputs with their own [DOI's](https://en.wikipedia.org/wiki/Digital_object_identifier).

See this [GitHub guide for more information on making your public code citable](https://guides.github.com/activities/citable-code/).


## Vignettes

Vignettes are a form of supplementary documentation, containing applied examples that demonstrate the intended use of the code in your project or package.
Docstrings may contain examples applying individual functional units, while vignettes may show multiple units being used together.
The term vignette is usually used with reference to R packages, for example this introduction to the [`dplyr` package](https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html) for data manipulation.
However, the same long-form documentation is beneficial for projects in any programming language - for instance the [`pandas` basics guide](https://pandas.pydata.org/docs/user_guide/basics.html).

We've seen that [docstrings](docstrings) can be used to describe individual functional code elements.
Vignettes provide a demonstration of the intended use for these classes and functions, in a realistic context.
This can help users to understand how different code elements interact, and how they might use your code in their own program.

Another good example is this vignette describing [how to design vignettes](http://r-pkgs.had.co.nz/vignettes.html) in Rmarkdown.
You can produce this type of documentation in any format, though Rmarkdown is particularly effectively at combining sections of code, code outputs and descriptive text.

You might also consider providing examples in an interactive notebook, that users can run for themselves.


## Versioning

Documenting the version of your code provides distinct points of reference in the code's development.
Recording the version of code used for analysis is important for reproducing your work.
When used in combination with [](version_control.md), versioning allows you to recover the exact code used to run your analysis and thus reproduce the same results.

[Semantic versioning](https://semver.org/) provides useful rules for versioning releases of your code.
Following these rules also helps other users of your code to understand how changes in your code may affect their software.
Each level of version number indicates the extent of changes to the application programming interface (API) of your code, i.e. the part of the code that a user interacts with directly.
Changes to the major version number indicate changes to the API that are not compatible with use of previous versions of the code.
While changes is the minor and patch numbers indicate changes that are either compatible or have no effect on the use of the code, respectively.


```{figure} ./_static/semantic_versioning.png
---
width: 70%
name: semantic_versioning
---
[Semantic versioning](https://semver.org/)
```

You'll see this, or a similar version numbering, on packages that you install for Python and R.

Changes to this book don't cause backwards-compatibility issues in the same sense as code.
We've chosen to use a form of calender versioning ([CalVer](https://calver.org/)).
You'll see the current version below the site's table of contents, where the first four digits represent the year that latest changes were made.
The incremental number following the full stop indicates how many versions of the guidance have been published in that year.
As this guidance will change over time, this version number provides users with a reference for citing a specific state of the guidance.


## Changelog

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

Similarly to versioning, a changelog is useful for users to determine whether an update to your code is compatible with their work, which may depend on your code.
It can also document which parts of your code will no longer be supported in future version and which bugs in your code have been addressed.
Your changelog can be in any format and should be associated with your code documentation, so that it is easy for users and other contributors to find.

[keep a changelog](https://keepachangelog.com/en/1.0.0/) provides a simple but effective template for recording changes to your code.


## Copyright and Licenses

Copyright indicates ownership of work.
All material created by civil servants, ministers, government departments and their agencies are covered by [Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/).
It is not essential to include a copyright notice on your work, but doing so can help to avoid confusion around ownership.

Licences outline the conditions under which others may use, modify and/or redistribute your work.
As such, including a licence with code is important for users and other developers alike.
This [online tool](https://choosealicense.com/) might help you to choose an appropriate license for your project.
The Government Digital Service generally recommends using the [MIT license](https://opensource.org/licenses/MIT) for code and the [Open Government License (OGL)](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) for documentation.

Both copyright and license are usually placed in a LICENSE file in your project.
For example, an MIT LICENSE file might look like:

> Copyright 2020, Crown copyright
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Open source your code

In government, we [support and promote open source](https://www.gov.uk/service-manual/service-standard/point-12-make-new-source-code-open) whenever possible.
[Open source](https://opensource.com/resources/what-open-source) software is software with source code that anyone can freely inspect, modify and enhance.
As a government analyst, you should aim to make all new source code open, unless justification can be provided for withholding part of your source code.

Open sourcing code benefits yourself, other government analysts and the public.

Personal benefits from open sourcing include:

* Attribution - coding in the open creates a public record of your contributions to analysis and software.
* Collaboration - you can gain experience working with analysts in other departments.
* Review - peers and experts in the field can provide advice on improving your analysis and coding.
* Feels good - we regularly benefit from open source software, so it's nice to give something back.

While the public benefit from:

* Transparency - stakeholders can understand and reproduce our analysis, which is a core element of the [Statistics Code of Practice](https://code.statisticsauthority.gov.uk/).
* Sharing value - others can benefit from our work, either through reuse or demonstration of good practices.
* Sharing opportunity - others can gain insight and experience from reading and possibly contributing to  your code.

Please see the [Government Data Service (GDS) guidance](https://www.gov.uk/government/publications/open-source-guidance/when-code-should-be-open-or-closed) for help deciding when code should be open or closed.
Security concerns for coding in the open are also addressed in further [GDS guidance](https://www.gov.uk/government/publications/open-source-guidance/security-considerations-when-coding-in-the-open).
