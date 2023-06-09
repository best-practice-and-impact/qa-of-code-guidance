# Quality Assurance of Code for Analysis and Research

This document forms part of the Quality Guidance, published by the Quality and Improvement Division of Methods and Quality Directorate at the UK
[Office for National Statistics](https://www.ons.gov.uk).


## Contributing to this guidance

We welcome all constructive feedback and contributions.

To provide feedback or request new content, you can [create an issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues) on this book's repository.
Alternatively, you can always drop us an [email](mailto:ASAP@ons.gov.uk).

If you'd like to contribute, please also
[create or comment on an issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues)
to describe the changes that you'd like to make.
This will allow discussion around whether content is suitable for the book, before you put the hard work into implementing it.


### Getting started

Minor text edits can be submitted as a Pull Request using the "Suggest edit" button under the GitHub logo at the top of the page you would like to change.

For changes to anything other than lines of text, you should follow these steps to make the changes locally:

To start contributing, you'll need Python installed.
If you sit outside of Quality and Improvement Division, the you'll need to [create a Fork of this repository to make changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks).
Once forked, you should clone the fork repository to get a copy of the book. Then install its Python dependencies like so:

```{none}
git clone https://github.com/<your-username>/qa-of-code-guidance.git
cd qa-of-code-guidance
pip install -r requirements.txt
```

Great, now you should have the dependencies, including [jupyter-book](https://jupyterbook.org/intro.html), installed and be able to build the book locally using:

```{none}
jb build book
```

Jupyter book will write the book's `HTML` content to `book/_build/html/`, so you can open `index.html` from there to view the local build.
Run the build command after making a change to the text to update the HTML that you view here.

All content for the book is currently written in
[Markedly Structured Text](https://myst-parser.readthedocs.io/en/latest/),
which is based on standard Markdown (`.md`) but allows use of "directives" for generating content.

We also require developers to conform to a specific Markdown style.
You can do this by installing our pre-commit `pymarkdownlnt`:

```{none}
pip install -r dev-requirements.txt
pre-commit install
```

### Guidelines

When contributing to the book, please:

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

You should create a new branch to collect related changes that you make.
Once you're happy with any changes you've made to the book, you should raise a
[Pull Request (PR)](https://github.com/best-practice-and-impact/qa-of-code-guidance/pulls)
to the `main` branch of the main repository.
The source branch of this PR should be the fork and/or branch that you have commited changes to.

## Publishing changes

Internal contributors can trigger a new release of the book.

### Preparation

To create a new release and publish the `main` branch, you will need to install the development dependencies:

```{none}
pip install -r dev-requirements.txt
```

### Releasing

To create a new release, use the command line tool `bump2version`, which will be installed with the dev dependencies.
The version number references the current `year` and an incremental `build` count.

For a the first release of a year, provide the `year` as the command argument, otherwise provide `build`.

```{none}
bump2version build
```

`bumpversion` will create a new Git `tag` and `commit`.
If you're happy with the version increase, `push` these to the remote to trigger the publication, by running both:

```{none}
git push
git push --tags
```
