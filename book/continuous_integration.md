# Continuous Integration

## Introduction


## Run tests whenever you make changes to your project

Tests should be run whenever you make changes to your project.
This ensures that changes do not break the existing, intended functionality of your code.
Where tests fail, fix these before adding changes to a stable or production version of your code.

If you have altered the functionality of your code, this will likely break existing tests.
Failing tests here are a good reminder that your should update your documentation and tests to reflect the new functionality.

If your collection of tests runs quickly, it's simplest to run them all often.
If some tests take longer to run, you might want to run these less often - perhaps only when relevant changes have been made.
Otherwise, running the entire collection of tests has the added benefit of capturing unexpected side-effects of your changes.
For example, you might pick up an unexpected failure in part of your code that you have not directly changed.

It's not easy to remember to run your tests at regular intervals.
You're already putting effort into `commit`ing your changes to a version control system regularly.
And you're right to think "surely this could be automated too?"
[Continuous integration](continuous-integration) can be used to automate testing, amongst other quality assurance measures, and can be triggered when changes are made to your remote version control repository.
These tools can be used to ensure that all changes to a particular project are tested.
Additionally, it allows others that are reviewing your code to see the results of your tests.

An alternative to continuous integration, is using a Git hook.
[Git hooks](https://git-scm.com/docs/githooks) are scripts that can be set to run locally at specific points in your Git workflow.
For example, we might set up a `pre-commit` or `pre-push` hook that runs our tests before we make each commit or push to the remote repository.
This might stop our commit/push if the tests fail, so that we don't push breaking changes to our remote repository.

```{note}
If your code is likely to be run on a range of software versions or operating systems, you might want to test on a variety of these. Tools exists to support local testing of combinations software versions and package dependency versions:
* [tox](https://tox.readthedocs.io/en/latest/) or [nox](https://nox.thea.codes/en/stable/) for Python
* [rhub](https://r-hub.github.io/rhub/) for R

However, [continuous integration](continuous-integration) can be used to automate these tests on a broader range on parameters.
```

(continuous-integration)=
### GitHub Actions

Continuous integration (CI) describes the practice of frequently committing changes to your code. CI tools support this working pattern by automating routine quality assurance tasks. This subsection describes how the GitHub CI tool, [GitHub Actions](https://github.com/features/actions), can be used in an analytical workflow. This includes verifying that your code successfully builds or installs and that your [code tests](testing_code.md) run successfully.

Automation of routine tasks in this way reduces the effort required to merge changes onto the existing code base. This supports frequent commiting and merging of changes. As such, conflicts between multiple contributions should be minimal and that review of these changes simpler. Additionally, the execution environment for CI is defined in a CI workflow configuration, which improves reproducibility when running tests.

CI is often linked to:
* Continuous delivery - ensuring that your code is fit for use after each integration
* Continuous deployment - automatically deploying working code into production


## Continuous Integration Platforms

* [GitHub Actions](https://github.com/features/actions)
* [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
* [Travis](https://travis-ci.org/)
* [Jenkins](https://www.jenkins.io/)
* [Coveralls](https://coveralls.io/)