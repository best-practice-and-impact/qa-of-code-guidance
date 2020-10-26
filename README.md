# Quality Assurance of Code for Analysis and Research

This document forms part of the Quality Guidance, published by the Best Practice and Impact Division, ONS.


# Contributing to this guidance

We welcome all constructive feedback and contributions.

To provide feedback or request new content, you can [create an issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues) on this book's repository.
Alternatively, you can always drop us an [email](gsshelp@statistics.gov.uk).

If you'd like to contribute, please also [create or comment on an issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues) to describe the changes that you'd like to make.
This will allow discussion around whether content is suitable for this book, before you put the hard work into implementing it.


## Contributing


### Getting started

To start contributing, you'll need python installed.
You can take a copy of the book and install it's dependencies like so:

```
git clone https://github.com/best-practice-and-impact/qa-of-code-guidance.git
cd qa-of-code-guidance
pip install -r requirements.txt
```

Great, now you should have dependencies, including [jupyter-book](https://jupyterbook.org/intro.html), installed and be able to build the book locally using:

```
jb build book
```

The book output will be written to book/_build, so you can open the `.html` from there to view the local build.

All content for the book is currently written in [Markedly Structured Text](https://myst-parser.readthedocs.io/en/latest/), which is based on standard Markdown (`.md`) but allows use of "directives" for generating content.


### Guidelines

Please:
* Keep text as simple as possible
* Provide alt text for all images
* Explain informative image content in text, where possible
* Provide examples of good and/or bad practices to support your content
* Take on feedback from users and other developers


### Submitting contributions

Once you're happy with any changes you've made to the book, you should raise a [Pull Request](https://github.com/best-practice-and-impact/qa-of-code-guidance/pulls) to the `master` branch of the book's repository.

Please start your pull request title with a keyword to indicate the type of change(s):

* Add - Added entirely new content
* Improve - Improved existing content
* Fix - Fix typo's or other mistakes in existing content
* Document - Changes to the documentation of the project
