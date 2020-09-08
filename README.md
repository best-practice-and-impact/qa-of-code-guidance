# Quality Asssurance of Code Guidance

[![Travis build status](https://travis-ci.org/best-practice-and-impact/qa-of-coding-guidance.svg?branch=master)](https://travis-ci.org/best-practice-and-impact/qa-of-coding-guidance)


Guidance for the Quality Assurance of Code. This document forms part of the Quality Guidance, published by the Best Practice and Impact Division, ONS.


# Contributing to this guidance

We welcome all constructive feedback and contributions.

To provide feedback or request new content, you can [create an issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues) on this book's repository.
Alternatively, you can always drop us an [email](gsshelp@statistics.gov.uk).

If you'd like to contribute, please also [create or comment on an issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues) to describe the changes that you'd like to make.
This will allow discussion around whether content is suitable for this book, before you put the hard work into implementing it.


## Contributing


### Getting started

To start contributing, you'll first need python installed.
Then should take a copy of the book and install it's dependencies like so:

```
git clone https://github.com/best-practice-and-impact/qa-of-code-guidance.git
cd qa-of-code-guidance
pip install -r requirements.txt
```

Great, now you should have [jupyter-book](https://jupyterbook.org/intro.html) installed and be able to build the book locally using:

```
jb build book
```

The book output will be written to book/_build, so you can open the `.html` from there to view the local build.

All content for the book is written in [Markedly Structured Text](https://myst-parser.readthedocs.io/en/latest/), which is based on standard Markdown (`.md`) but allows use of "directives" for generating content.


### Submitting contributions

Once you're happy with any changes you've made to the book, you should raise a [Pull Request](https://github.com/best-practice-and-impact/qa-of-code-guidance/pulls) to the `master` branch of the book's repository.

Please start your pull request title with a keyword to indicate the type of change(s):

* Add - Added entirely new content
* Improve - Improved existing content
* Fix - Fix typo's or other mistakes in existing content
* Document - Changes to the documentation of the project
