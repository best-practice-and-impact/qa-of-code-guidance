# Testing Code

Testing here refers to code that assert that your code is working as expected.
Where code documentation specifies what code should do, testing assures that this specification is true.

The core concept of testing is **"Does my code give do what I expect it to, given realistic inputs?"**.

The most common pattern for writing these tests is:
1. Arrange - set up any pre-requisites for your test
2. Act - run the code that your are testing
3. Assert - verify that the code performed the expected action


## Why test code ★☆☆☆☆

Key reasons for testing your code include:
* Knowing that your code works - you can't be sure that your code works without having run it with realistic examples
* Asserting that user requirements have been met - test can verify that users expectations are met by the code
* Increasing confidence in your changes - tests let you know when you've broken the expected functionality of your code
* Profiling performance - tests can be used to report or flag poor performance (e.g. modelling)
* Improving code structure - well-structured code is easier to write tests for, so testing incentivises good code structure


## What to test ★☆☆☆☆

> A QA engineer walks into a bar. Orders 1 beer. Orders 3.14 beers. Orders -1 beers. Orders 99999999999 beers. Orders a lizard.  Orders NULL.
> First real customer walks in and asks where the bathroom is. The bar bursts into flames.

Unfortunately, there's no golden rule for exactly what you should test.
We can use general guides to direct where most of our testing effort goes.

You should:
* Focus on testing the most complex and vulnerable parts of your code
* Write a new test every time you find a bug, to squash it for good
* Focus on testing the most realistic use cases of your code
* Test external interfaces - what happens if something unexpected is returned from one of your dependencies?
* Document what your code should and shouldn't be used for, to steer users towards the corrected and tested usage

You shouldn't:
* Attempt to test every possible input and type of input
* Focus on things that are already tested (e.g. functionality from your dependencies packages)
* Write tests that have an element of randomness - tests should be deterministic


A short check-list for questions to ask when writing tests:
* Have I tested realistic combinations of my codes input parameters?
* Have I tested any discrete outputs once?
* Have I tested the boundaries of non-discrete outputs?
* Are informative errors raised when the code is not used in a valid or correct way?
* Are informative warnings raised when the code is not used in a standard way?


Don't worry if writing all of these tests sounds like a large task.
You'll find that tests are very repetitive in nature, so we can reuse testing code to broaden the cases that our tests cover.
We'll describe two useful ways of reducing the burden of writing and maintaining tests in a later section.

The examples in this section use these testing frameworks:
* `pytest` for Python
* `{testthat}` for R

Other common frameworks, which have a Class-based focus, are:
* `unittest` built into Python
* `{Runit}` for R


TODO: Modelling-relevant testing


## When to run tests ★☆☆☆☆

Tests should be run whenever you make changes to your project.
This ensures that changes do not break the existing, intended functionality of your code.
When tests fail, you should endeavour to fix these before adding these changes to a stable or production version of your code.

If you have intentionally altered the functionality of your code, this will like break existing tests.
Failing tests here are a good reminder that your should update your documentation and tests to reflect the new functionality.

If your collection of tests runs quickly, it's simplest to run them all often.
If some tests take considerably longer to run, you might want to run these less often - perhaps only when relevant changes have been made.
Otherwise, running the entire collection of tests has the added benefit of capturing unexpected side-effects of your changes.
For example, in part of your code that you have not directly changed.

It's not easy to remember running tests at regular intervals.
You're already putting effort into commiting your changes to a version control system regularly.
And you're right to think "surely this could be automated too?"

TODO: Reference CI

The most effective way of automating testing is through the use of Continuous Integration.
This can be used to ensure that all changes to a particular project are tested.
Additionally, it allows anyone reviewing your code to see the results of your tests.

An alternative to continuous integration, is using a Git hook.
[Git hooks](https://git-scm.com/docs/githooks) are scripts which can be set to run locally at specific points in your Git workflow.
For example, we might set up a `pre-commit` or `pre-push` hook that runs our tests before we make each commit or push to the remote repository.
This might stop our commit/push if the tests fail, so that we don't push breaking changes to our remote repository.


## Layers of testing ★☆☆☆☆

Testing comes in many shapes and sizes.

In it's simplest form, a test asserts that an expectation is true:

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

[Acceptance testing](https://en.wikipedia.org/wiki/Acceptance_testing) is often considered as additional level, but is not covered here.

The following sections will climb through these layers of testing.
Please note that principles covered early on also apply at subsequent levels.


## Structuring Test Code ★☆☆☆☆

TODO: Might just be a reference to project structure?



## Unit Testing ★★☆☆☆


<!-- 
````{tabs}

```{code-tab} py

```

```{code-tab} r R
```

````
-->


## Integration Testing ★★★☆☆


## End-to-end Testing ★★★☆☆


## Reducing Testing Effort


### Parametrization


Reference material:
* [`pytest` Parametrize mark](https://docs.pytest.org/en/stable/parametrize.html) documentation
* [`{testthat}` Fixture](https://testthat.r-lib.org/articles/test-fixtures.html) documentation


### Fixtures

As your test suite grows, you might notice that many of your test use similar code to prepare your tests or to clean up after each test has run.
You're be right to be unnerved by this, especially if "Don't Repeat Yourself" comes to mind.

Fixtures help us to avoid this form of repetition in our tests.
You define your test preparation and clean up within a function, then the fixture carries out these steps consistently for each function that it is used with. 

In Class-based testing frameworks, these functions tend to be separated into `SetUp` and `TearDown` functions.
These are similarly set to run before and after each test, respectively.

Fixtures can be especially useful when setting up a test object takes a large amount of time or resource.
Or perhaps, you need to ensure that changes are undone after each test is complete.

Reference material:
* [`pytest` Fixture](https://docs.pytest.org/en/stable/fixture.html) documentation
* [`{testthat}` Fixture](https://testthat.r-lib.org/articles/test-fixtures.html) documentation


## Testing in multiple environments ★★★☆☆

tox/nox

[rhub](https://r-hub.github.io/rhub/)?


## Other references

* Hadley Wickham's [testthat: getting started with testing](https://vita.had.co.nz/papers/testthat.pdf)
* [`pytest` getting started](https://docs.pytest.org/en/3.0.1/getting-started.html)
* Real Python [Getting Started With Testing in Python](https://realpython.com/python-testing/)
