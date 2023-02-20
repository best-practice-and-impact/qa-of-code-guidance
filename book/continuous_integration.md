# Continuous Integration

## Introduction

Continuous integration (CI) describes the practice of frequently committing changes to your code. CI tools support this working pattern by automating routine quality assurance tasks. This includes verifying that your code successfully builds or installs and that your [code tests](testing_code.md) run successfully.

CI is often linked to:

* Continuous delivery - ensuring that your code is fit for use after each integration
* Continuous deployment - automatically deploying working code into production

## Automating your tests

Tests should be run whenever you make changes to your project.
This ensures that changes do not break the existing, intended functionality of your code.
However, it's not easy to remember to run your tests at regular intervals.
You're already putting effort into `commit`ing your changes to a version control system regularly.

And you're right to think "surely this could be automated too?"
[Continuous integration](continuous-integration) can be used to automate testing, amongst other quality assurance measures, and can be triggered when changes are made to your remote version control repository.
These tools can be used to ensure that all changes to a project are tested.
Additionally, it allows others, who are reviewing your code, to see the results of your tests.

Automation of routine tasks in this way reduces the effort required to merge changes onto the existing code base. This supports frequent commiting and merging of changes. As such, conflicts between multiple contributions should be minimal and that review of these changes simpler. Additionally, the execution environment for CI is defined in a CI workflow configuration, which improves reproducibility when running tests.

## Continuous Integration Platforms

* [GitHub Actions](https://github.com/features/actions)
* [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
* [Travis](https://travis-ci.org/)
* [Jenkins](https://www.jenkins.io/)
* [Coveralls](https://coveralls.io/)

## Git Hooks

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