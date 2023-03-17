# Automating Code Quality Assurance

## Motivation

There are various tasks which can be automated to increase the quality of code and make development easier and less tedious. Automating the running of unit tests is especially important to ensuring trust in your pipeline or package, by ensuring that all unit tests pass before every merge.


(automate-tests)=
### Automate tests to reduce risk of errors

Tests should be run whenever you make changes to your project.
This ensures that changes do not break the existing, intended functionality of your code.
However, it is easy to forget to run your tests at regular intervals.

"Surely this could be automated too?"

Absolutely! Automatic testing, amongst other quality assurance measures, can be triggered when changes are made to your remote version control repository.
These tools can be used to ensure that all changes to a project are tested.
Additionally, it allows others, who are reviewing your code, to see the results of your tests.


(continuous-integration)=
## Commit small changes often

Committing small changes regularly is often referred to as Continuous Integration (CI).
This can be achieved easily through the use of [version control](version_control.md), such as Git.
\\ add something about frequency of commit and push

CI should be underpinned by automating routine code quality assurance tasks.
This quality assurance includes verifying that your code successfully builds or installs and that your [code tests](testing_code.md) run successfully.
these can be achieved in a number of ways such as use of Git hooks and workflows.


## Use Git hooks to encourage good practice

[Git hooks](https://git-scm.com/docs/githooks) are scripts that can be set to run locally at specific points in your Git workflow,
such as pre-commit, pre-push, etc.
They can be used to automate code quality assurance tasks, e.g. run tests, ensure style guides are followed, or enforce commit standards.

For example, we might set up a `pre-commit` or `pre-push` hook that runs our tests before we make each commit or push to the remote repository.
This might stop our commit/push if the tests fail, so that we don't push breaking changes to our remote repository.

```{note}
If your code is likely to be run on a range of software versions or operating systems, you might want to test on a variety of these. Tools exists to support local testing of combinations software versions and package dependency versions:

* [tox](https://tox.readthedocs.io/en/latest/) or [nox](https://nox.thea.codes/en/stable/) for Python
* [rhub](https://r-hub.github.io/rhub/) for R
```


(linters-formatters)=
### Linters and formatters

Style guides are important in the readability and clarity of your code and should form part of your quality assurance process.
However, as discussed in [](automate-style-checks), the process of checking and fixing code for style and formatting is tedious.
Automation can speed up this work, either by providing suggestions as the code is written or by reformatting your code to comply with your chosen style.

Two main types of tool exist for these tasks:

* Linters - these analyse your code to flag stylistic errors (and sometimes bugs or security issues too).
* Formatters - these not only detect when you have diverged from a style, but will automatically correct the formatting of your code to conform to a particular style.

```{list-table} Packages that can be used for linting or formatting in Python and R
:header-rows: 1
:name: linters

* - Language
  - Linters
  - Formatters
* - Python
  - `flake8`, `pylint`, `Bandit`
  - `Black`, `Isort`
* - R
  - `lintr`
  - `formatR`, `styler`
* - Markdown
  - `pymarkdownlnt`
  -
```

These tools can be used locally (in the command line) or as git pre-commit hooks.
As described above, using pre-commit hooks allows you to run these automatically every time there are changes,
thus reducing the burden on developers and reviewers in checking that code conforms to style guides. 

Be sure to read the documentation for any of these tools, to understand what they are checking or changing in your code.
Some can be configured to ignore or detect specific types of formatting error.
You can run multiple of these, to catch a broader range of stylistic or programmatic errors.

## Worflows

\\ add details

### Example use cases for GitHub Actions

The following examples are presented to support understanding of the topic discussed above.

#### Configure GitHub actions to automate tests

Below is an example configuration file, for use with GitHub actions. The `YAML` file format, used below, is common to a number of other CI tools.

```yaml
name: Test python package

on:
  push:
    branches:
      - master
  pull_request:

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.6, 3.7, 3.8, 3.9]

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest 
        pip install -r requirements.txt
        
    - name: Test with pytest
      run: |
        pytest
```

The first section of this example describes when our workflow should be run. In this case, we're running the CI workflow whenever code is `push`ed to the `master` branch or where any Pull Request is created. In the case of Pull Requests, the results of the CI workflow will be report on the request's page. If any of the workflow stages fail, this can block the merge of these changes onto a more stable branch. Subsequent commits to the source branch will trigger the CI workflow to run again.

Below `jobs`, we're defining what tasks we would like to run when our workflow is triggered. We define what operating system we would like to run our workflow on - the Linux operating system `ubuntu` here. The `matrix` section under `strategy` defines parameters for the workflow. The workflow will be repeated for each combination of parameters supplied here - in this case the 4 latest Python versions.

The individual stages of the workflow are defined under `steps`. `steps` typically have an informative name and run code to perform an action. Here `uses: actions/checkout@v2` references [existing code](https://github.com/actions/checkout) that will retrieve the code from our repo. The subsequent `steps` will use this code. The next step provides us with a specific Python version, as specified in the `matrix`. Then we install dependencies/requirements for our code and the `pytest` module. Finally, we run `pytest` to check that our code is working as expected.

This workflow will report whether our test code ran successfully for each of the specified Python versions.

#### Configure GitHub actions to build and deploy documentation

This book uses the following GitHub Actions configuration to build and deploy the HTML content:

```yaml
name: Build and deploy book

on:
  push:
    branches:
      - main
      - master
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Build the book
      run: |
        jb build book -W -v --keep-going && touch ./book/_build/html/.nojekyll

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: startsWith( github.ref, 'refs/tags/v')
    steps:
    - name: "Deploy book to GitHub Pages"
      uses: peaceiris/actions-gh-pages@v3.6.1
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./book/_build/html
```

This workflow runs whenever a pull request is create or changes are pushed directly to the main branch. It has two jobs - one that builds the book's HTML content and another that deploys the content to this website.

As with the previous example, we start the workflow by setting up an environment with Python. We install the dependencies for the project, which includes `jupyter-book` to build to the book.

Our workflow then builds the book's HTML content, where the workflow will fail if warnings or errors are raised.

In the second job, the book (including the new changes) is deployed to the site that you are reading now. This job needs the build job to have completed successfully before it will run. It will only run if a new Git tag has been created, to indicate a new version of the book. This allows us to accumulate changes on the main branch, before releasing a collection of changes in the next version. This deployment step requires authentication, which is managed by a secret/token that is accessed from the Action's environment.

You might use a similar approach to this to deploy your code's HTML documentation.

#### Comprehensive example

You can see a detailed example of CI in practice in the `jupyter-book` project. A recent version of the [`jupyter-book` CI workflow](https://github.com/executablebooks/jupyter-book/blob/6fb0cbe4abb5bc29e9081afbe24f71d864b40475/.github/workflows/tests.yml) includes:

* Checking code against style guidelines, using [pre-commit](https://pre-commit.com/)
* Running code tests over
  * a range of Python versions
  * multiple versions of specific dependencies (`sphinx` here)
  * multiple operating systems
* Reporting test coverage
* Checking that documentation builds successfully
* Deploying a new version of the `jupyter-book` package to [the python package index (PyPI)](https://pypi.org/)
