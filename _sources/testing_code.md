# Testing code

Testing refers here to code that verifies that your code is working as expected.
Where code documentation specifies what code should do, testing assures that this specification is true.

The core concept of testing is **"Does my code do what I expect it to, given realistic inputs?"**.

The most common pattern for writing these tests is:
1. Arrange - set up any pre-requisites for your test
2. Act - run the code that you are testing
3. Assert - verify that the code performed the expected action


## Why test code?

You can't be sure that your code works without having run it with realistic examples. Tests can verify that users expectations are met by the code.
They let you know when you've broken the expected functionality of your code - or when users have.
They can be used to report or flag poor performance (e.g. modelling).
Well-structured code is easier to write tests for, so testing incentivises good code structure.

Testing is crucial to assuring quality in your code and will also increase efficiency in the development of your code.


## What to test

> A quality assurance engineer walks into a bar. They order 1 beer. They order 3.14 beers. They order -1 beers. They order 99999999999 beers. They order a lizard. They order `NULL`.  

> The first customer walks in and asks where the bathroom is. The bar bursts into flames.

Unfortunately, there's no golden rule for exactly what you should test.
We can use general guides to direct where most of our testing effort goes.

You should:
* Focus on testing the most complex and vulnerable parts of your code
* Write a new test every time you find a bug, to squash it for good
* Focus on testing the most realistic use cases of your code
* Test external interfaces - what happens if something unexpected is returned from one of your dependencies?
* Document what your code should and shouldn't be used for, to steer users towards the correct and tested usage

You shouldn't:
* Attempt to test every possible input and type of input
* Focus on things that are already sufficiently tested (e.g. it should not be necessary to test the functionality from your dependencies packages if you are confident that they are already been subjected to sufficient assurance)
* Write tests that have an element of randomness - tests should be deterministic


A short check-list for questions to ask when writing tests:
* Have I tested realistic combinations of my code's input parameters?
* Have I tested any discrete outputs once?
* Have I tested the boundaries of non-discrete outputs?
* Are informative errors raised when the code is not used in a valid or correct way?
* Are informative warnings raised when the code is not used in a standard way?


Don't worry if writing all of these tests sounds like a large task.
You'll find that tests are very repetitive in nature, so we can reuse testing code to broaden the cases that our tests cover.
We'll describe two useful ways of reducing the burden of writing and maintaining tests in a later section.

The examples in this section use these testing frameworks:
* `pytest` for Python
* `testthat` for R

R users might also be interested in `assertthat`, which provides Python-like assertions in R.

Other common frameworks, which have a Class-based focus, are:
* `unittest` built into Python
* `Runit` for R


```{todo}

Modelling-relevant testing
including https://www.jeremyjordan.me/testing-ml/

[#15](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/15)
```

## When to run tests

Tests should be run whenever you make changes to your project.
This ensures that changes do not break the existing, intended functionality of your code.
When tests fail, you should endeavour to fix these before adding these changes to a stable or production version of your code.

If you have intentionally altered the functionality of your code, this will likely break existing tests.
Failing tests here are a good reminder that your should update your documentation and tests to reflect the new functionality.

If your collection of tests runs quickly, it's simplest to run them all often.
If some tests take considerably longer to run, you might want to run these less often - perhaps only when relevant changes have been made.
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


## Layers of testing

Testing comes in many shapes and sizes.

In its simplest form, a test asserts that an expectation is true:

````{tabs}

```{code-tab} py
assert 1 == 1
```

```{code-tab} r R
if (1 != 1):
  stop("Something has gone terribly wrong")
```

````

In this chapter we will describe a more formalised method for testing.

In order of increasing scale, the main layers of testing covered here will be:

* Unit testing - assuring that functions or class methods perform as expected
* Integration testing - assuring that multiple units interact with each other as expected
* End-to-end or system testing - verifying that a complete system meets its requirements

The time taken to develop and run individual tests roughly increases down this list.

[Acceptance testing](https://en.wikipedia.org/wiki/Acceptance_testing) is often considered as an additional level, but is not covered here.

The following sections will climb through these layers of testing.
Please note that the principles covered early on also apply at subsequent levels.


## Structuring test code

```{todo}
Need to write structure test code

Might just be a reference to project structure?

Lots of content needed below

[#27](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/27)

```


## Unit testing


```{admonition} Key Learning
:class: admonition-learning

You should follow the [Introduction to Unit Testing course](https://learninghub.ons.gov.uk/enrol/index.php?id=539) (GSS only) for applied examples in Python and R.
The course also covers writing and documenting functions, and error handling.

Other resources include:
* Hadley Wickham's [testthat: getting started with testing](https://vita.had.co.nz/papers/testthat.pdf)
* [`pytest` getting started](https://docs.pytest.org/en/3.0.1/getting-started.html)
* Real Python [Getting Started With Testing in Python](https://realpython.com/python-testing/)
```

```{todo}
These testing sections all need more content/examples.

[#28](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/28)
```

## Integration testing

Your analysis likely involves multiple units working together to perform a high level task.
Assuring that individual units work as expected, using unit testing, does not guarantee that multiple units interact with one another as expected.

```{figure} ./_static/no_integration_tests.png
---
width: 40%
name: no_integration_tests
alt: Two drawers that open into each other's handles.
---
Two unit tests, no integration tests.
```

Integration tests incorporate two or more units and check that they work together correctly.
These tests are also used to test the interface between your code and external dependencies, such as a database or web-based API.

When your code relies upon interaction with complex or external dependencies, it may be difficult for your tests to reproducibly access these dependencies.
Creating abstractions of these dependencies when they are not being directly tested can keep your test code simpler and more focused.
You might use Stubs or Mocks for this purpose:
* Stubs carry out a predetermined behaviour. For example, a stub representing an API always returns the same response. Use these when you are not interested in the details around how your code interacts with the dependency.
* Mocks require additional setup in your test code, to define your expectations. Use these when your test needs to verify that your code interacts with the Mock in a specific way.


## End-to-end testing

As the name suggests, these tests cover the entire process.
The motivation for using end-to-end tests is similar to that of integration tests.
Despite assurance that small sections of the code are functioning correctly, it's important to validate that your overall system is fit for purpose.

```{figure} https://i.stack.imgur.com/Nirxy.jpg
---
width: 50%
name: sinking_ship
alt: A sinking ship would still report passing unit tests.
---
A sinking ship would still report a number of passing unit and integration tests, while the system is failing overall.
```

These tests are much slower to run and can take longer to develop for complex processes.
Having at least one end-to-end test for your process will ensure that the high-level specification of your code is met.
This should validate that your user requirements are met.



## Reducing repetition in tests

Repetitive test code violates the "Don't repeat yourself" rule.
As with functional code, test code is much easier to maintain when it is modular and reusable.

```{todo}
Add examples to reducing repetition in tests to demonstrate these

[#29](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/29)
```


### Fixtures

As your test suite grows, you might notice that many of your tests use similar code to prepare your tests or to clean up after each test has run.
Copying these code snippets for each test is laborious and also increases the risk of inconsistently applying those steps.

Fixtures help us to avoid this form of repetition in our tests.
You define your test preparation and clean up within a function (the fixture).
You then use the fixture to carry out these steps consistently for each test that they are required for. 

In Class-based testing frameworks, these functions tend to be separated into `SetUp` and `TearDown` functions.
These are similarly set to run before and after each test, respectively.

Fixtures can be especially useful when setting up a test object takes a large amount of time or resource.
They can be designed to run for each test, once for a group of tests or once for the whole test suite.
They are also useful for undoing any consequences of each test run.
For example, removing data which has been written to a temporary file or database.

Reference material:
* [Python `pytest` Fixture](https://docs.pytest.org/en/stable/fixture.html) documentation
* [R `testthat` Fixture](https://testthat.r-lib.org/articles/test-fixtures.html) documentation


### Parameterization

You might also find that similar steps are taken when testing multiple combinations of inputs and outputs.
Parameterization allows us to reduce repetition in our code, in a similar way to reusable functions.
We specify the pairs of inputs and expected outputs, so that our testing tool can repeat a test for each scenario.

Note that this approach is equivalent to using a for-loop to apply a test function over multiple inputs and expected outputs.
However, using functionality from test packages may improve running efficiency and the detail of subsequent test reports.

In `pytest`, this can be achieved using the [Parametrize mark](https://docs.pytest.org/en/stable/parametrize.html).

In R, the `patrick` package extends `testthat` to provide a [`with_parameters_test_that`](https://rdrr.io/cran/patrick/man/with_parameters_test_that.html) function to achieve this.



```{todo}
Testing in multiple environments?
* [tox](https://tox.readthedocs.io/en/latest/)/[nox](https://nox.thea.codes/en/stable/)
* [rhub](https://r-hub.github.io/rhub/)
```