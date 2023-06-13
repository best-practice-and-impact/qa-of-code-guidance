# Tools

This section highlights tools that support reproducible analysis and research.
This includes tools for general software development and bespoke packages that have been developed for government analysis.
Those developed or contributed to within government are marked with the abbreviation (gov).

If you have developed a package for use in analysis or recommend any that are not included here, please add them to the list.
You can request a new tool to be added to the list by [creating an issue on GitHub](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/new/choose)
or [contacting us by email](mailto:ASAP@ons.gov.uk?subject=Duck%20Book%20Tools).
Alternatively, you can add it directly to the project by creating a Pull Request.
You can do this using the "Suggest edit" link under the GitHub logo at the top of this page.
Please include a link and brief description when requesting a new tool to be added.

The tools included on this page will in general follow the good quality assurance practices described in this guidance.
However, as with any software there is a chance that they may still contain bugs or limitations.
Please apply your own judgement when using them.
If you feel a tool should no longer be included in this list, please suggest an edit or get in touch.

## Data manipulation and analysis

Manipulating and analysing data.

### Python

* [pandas](https://pandas.pydata.org/) - common data analysis and manipulation
* [Polars](https://www.pola.rs/) - high performance data manipulation
* [PySpark](https://spark.apache.org/docs/latest/api/python/)  - data manipulation for distributed (large) data
* [Splink](https://moj-analytical-services.github.io/splink/) (gov) - probabilistic data linkage

### R

* [dplyr](https://dplyr.tidyverse.org/)  - common data analysis and manipulation
* [sparklyr](https://spark.rstudio.com/) - for distributed (large) data

## Publishing

* [Quarto](https://quarto.org/) - reproducible documents for Python and R
* [a11ytables (R only)](https://co-analysis.github.io/a11ytables/index.html) (gov) - creating reproducible, accessible spreadsheets
* [gptables (Python and R)](https://gptables.readthedocs.io/en/latest/index.html) (gov) - creating reproducible, accessible spreadsheets

## Testing

Tools for implementing automated code testing.

### Python

* [pytest](https://docs.pytest.org/en/stable/) - common testing framework
* [unittest](https://docs.python.org/3/library/unittest.html) - common testing framework
* [hypothesis](https://hypothesis.readthedocs.io/en/latest/) - property-based testing
* [chispa (PySpark)](https://pypi.org/project/chispa/) - helper for testing PySpark code
* [coverage](https://coverage.readthedocs.io/en/coverage-5.3/) - measuring test coverage


### R

* [testthat](https://testthat.r-lib.org/) - common testing framework
* [assertr](https://docs.ropensci.org/assertr/) - common testing framework
* [patrick](https://github.com/google/patrick) - parameterised testing extension for `testthat`
* [covr](https://covr.r-lib.org/) - measuring test coverage

## Dependency management

* [venv (Python)](https://docs.python.org/3/library/venv.html) - manage packages using virtual environments
* [pyenv (Python)](https://github.com/pyenv/pyenv) - manage independent Python versions for different projects
* [renv (R)](https://rstudio.github.io/renv/articles/renv.html) - virtual environments for managing packages
* [conda](https://docs.conda.io/en/latest/) - manage language versions and packages for most languages

## Version control

* [Git](https://git-scm.com/) - common open source version control system
* [pre-commit](https://pre-commit.com/) - trigger checks (e.g. linters and formatters) before Git commits are created

## Project templates

* [govcookiecutter (Python)](https://github.com/best-practice-and-impact/govcookiecutter) (gov) - template project for reproducible analysis
* [Rgovcookiecutter (R)](https://github.com/best-practice-and-impact/Rgovcookiecutter) (gov) - template project for reproducible analysis

## Code Linters

Analysing code for stylistic errors, and sometimes bugs.

### Python

* [pylint](https://www.pylint.org/) - check coding style and identify some logical errors
* [flake8](https://flake8.pycqa.org/en/latest/) - check code style
* [Bandit](https://bandit.readthedocs.io/en/latest/) - check for common security issues
* [mypy](https://mypy.readthedocs.io/en/stable/) - check static types
* [Radon](https://radon.readthedocs.io/en/latest/) - check code complexity

### R

* [lintr](https://github.com/jimhester/lintr) - check code style


## Code Formatters

Automated code formatters.
These check code style, like linters, but also actively make changes to your code to meet a particular style.


### Python

* [Black](https://black.readthedocs.io/en/stable/)
* [Isort](https://pycqa.github.io/isort/)


### R

* [formatR](https://yihui.org/formatr/)
* [styler](https://styler.r-lib.org/)


## Packaging Code

Creating and releasing code as a package.

### Python

* [twine](https://pypi.org/project/twine/) - utility for publishing Python packages to [the Python Package Index PyPI](https://pypi.org/)

### R

* [goodpractice](http://mangothecat.github.io/goodpractice/) - gives advice on the quality of your R packages
* [fusen](https://thinkr-open.github.io/fusen/) - builds R packages from Rmarkdown file specifications


## Pipeline Orchestration

* [Apache Airflow](https://airflow.apache.org/) - workflow management platform
* [targets (R)](https://wlandau.github.io/targets-manual/) - defining and executing pipelines in R


(CI-tools)=
## Continuous Integration Platforms

* [GitHub Actions](https://github.com/features/actions)
* [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
* [Travis](https://travis-ci.org/)
* [Jenkins](https://www.jenkins.io/)
* [Coveralls](https://coveralls.io/)
