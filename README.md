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

The book output will be written to `book/_build/html/`, so you can open `index.html` from there to view the local build.

All content for the book is currently written in [Markedly Structured Text](https://myst-parser.readthedocs.io/en/latest/), which is based on standard Markdown (`.md`) but allows use of "directives" for generating content.


### Guidelines

Please:
* Keep text as simple as possible
* Provide alt text for all images
* Explain informative image content in text, where possible
* Attach hyperlinks to informative anchor text (e.g. 'blog post on reproducibility' instead of 'this link')
* Provide examples of good and/or bad practices to support your content
* Take on feedback from users and other developers

Any content that is in early development, should be kept under the `early_development/` directory.
While content that is ready for publication belongs under `book/`.
All pages in `book/` must be referenced in `_toc.yml` or a warning will be raised and the changes will not be published.


### Submitting contributions

If you are not a member of BPI and would like to contribute, please create a fork of the repository.
You should create a new branch to collect related changes that you make.
Once you're happy with any changes you've made to the book, you should raise a [Pull Request](https://github.com/best-practice-and-impact/qa-of-code-guidance/pulls) to the `master` branch of the book's repository.

## Publishing changes

Internal contributors can trigger a new release of the book.

### Preparation

To create a new release and publish the `master` branch, you will need to install the development dependencies:

```
pip install -r dev-requirements.txt
```

### Releasing

To create a new release, use the command line tool `bump2version`, which will be installed with the dev dependencies.
The version number references the current `year` and an incremental `build` count.

For a the first release of a year, provide the `year` as the command argument, otherwise provide `build`:

```
bump2version build
```

`bump2version` will create a new Git `tag` and `commit`.
If you're happy with the version increase, `push` these to the remote to trigger the publication, by running both:

```
git push
git push --tags
```
