# Testing code

Tests are bits of code that verify that your analytical code is working as expected.
Where code documentation helps others to understand what you expect your code to do,
testing assures that the the code meets these expectations.

Tests should be used proportionately across your codebase.
Hadley Wickham gives advice on designing test suites in
[his book on writing packages for R](https://r-pkgs.org/testing-design.html#what-to-test).
Although this book is written for R developers the advice at the start of the chapter is more general.


## Introduction

When testing, ask: **"Does my code do what I expect it to, given realistic inputs?"**.

Delivering a piece of analysis or research includes both writing the code that performs your analysis and assuring that it works.
You cannot be sure that your code works without having run it with realistic examples.
Therefore, you must test your analytical code proportionately.

Tests can:

* verify that users expectations are met by the code,
* define what code should do,
* let you know when you've broken the expected functionality of your code,
* be used to report or flag poor performance, for example, when modelling.

Testing helps you assure your code quality and makes developing your code more efficient.
Code that has not been tested is more likely to contain bugs and require more maintenance in the future.

Code for testing should also follow good practice.
Testing is a useful and rewarding skill to learn.
You can learn basic testing that will immediately improve the quality of your code quickly.
However, it is usual for it to seem a daunting learning curve.


## Good test suites are thorough but realistic

> A quality assurance engineer walks into a bar. They order 1 beer.
> They order 3.14 beers. They order -1 beers. They order 99999999999 beers. They order a lizard. They order `NULL`.
>
> The first customer walks in and asks where the bathroom is. The bar bursts into flames.

When writing code outside dedicated testing frameworks, we manually test our code.
We might do this by running our code and seeing what the outputs are.
We test these outputs against our mental model - or understanding - of how the code should work.
Testing frameworks structure this process so that computers can automate the testing of the code.

Unfortunately, there's no golden rule for exactly what you should test.
We can use general guides to direct where most of our testing effort goes.

Types of test - positive, negative (errors, if API). positive, negative, 0, NA.

You should:

* Focus on testing the most complex and vulnerable parts of your code
* Focus on testing the "behaviour" of your code as opposed to the implementation
* Write a new test every time you find a bug, to squash it for good
* Focus on testing the most realistic use cases of your code
* Test external interfaces - what happens if something unexpected is returned from one of your dependencies?
* Document what your code should and shouldn't be used for, to steer users towards the correct and tested usage

You shouldn't:

* Attempt to test every possible input and type of input
* Focus on things that are already sufficiently tested
(e.g. it should not be necessary to test the functionality from your dependencies packages
if you are confident that they are already been subjected to sufficient assurance)
* Write tests that have an element of randomness - tests should be deterministic

You may want to use a short check-list for questions to ask when writing tests. For example:

```{code-block} md
- [ ] Have I tested realistic combinations of my code's input parameters?
- [ ] Have I tested any discrete outputs once?
- [ ] Have I tested the boundaries of non-discrete outputs?
- [ ] Are informative errors raised when the code is not used in a valid or correct way?
- [ ] Are informative warnings raised when the code is not used in a standard way?
```

Don't worry if writing all of these tests sounds like a large task.
You'll find that tests are repetitive, so we can reuse testing code to broaden the cases that our tests cover.
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


## Structure your tests to reflect how the code works

Tests come in many shapes and sizes, but usually follow the pattern:

1. Arrange - set up any objects for your test, e.g. example input data and expected output data.
2. Act - run the code that you are testing (1 or more functions or methods).
3. Assert - verify that the code performed the expected action, e.g. that the output matched the expected output.

We'll use a couple of examples throughout this section of the book, to demonstrate how tests relate to analytical code.
Here we've a basic function to get the absolute equivalent of a number:

````{tabs}
```{code-tab} py Python
from math import sqrt

def absolute(number):
    """Get the non-negative equivalent of a real number."""
    if not isinstance(number, (int, float)):
        raise TypeError("Input number must be numeric.")
    return sqrt(number * number) 
```

```{code-tab} r R
#' Absolute
#'
#' Get the non-negative equivalent of a real number.

absolute <- function(number) {
    if (!is.numeric(number)) {
        stop("Input number must be numeric.")
    }

    return(sqrt(number * number))
}
```
````

To test that this function works as expected, we write code to carry out the test.
In Python this is another function, whereas in R it is simply a statement.
We've spread the code out over separate lines, to make it clear how this test follows the arrange, act, assert pattern:

````{tabs}
```{code-tab} py
def test_absolute_converts_negative_inputs():
    """Makes negative numbers positive."""
    # Arrange
    input_value = -5
    expected_output = 5

    # Act
    actual_output = absolute(input_value)

    # Assert
    assert actual_output == expected_output
```

```{code-tab} r R
# Arrange
input_value <- -5
expected_output <- 5

# Act
actual_output <- absolute(input_value)

# Assert
test_that("absolute converts negative inputs to positive", {
    expect_equal(expected_output, actual_output)
    }
)
```
````

The example above can be described as a 'unit test'.
This means that it tests the smallest unit of our code - a function.
There are three common "layers" of testing:

* Unit testing - assuring that functions or class methods perform as expected.
* Integration testing - assuring that units interact with other units or third party code as expected.
* End-to-end or system testing - assuring that a complete system functions as expected.

[User acceptance testing](https://en.wikipedia.org/wiki/Acceptance_testing) is an additional level of software testing although it doesn't involve writing test code.
It should be applied whenever developing software for users.

Each level of testing mitigates specific risks.


### Use minimal data for tests

Data for tests must be:

* only just large enough to carry out the test,
* static (hardcoded), readable, fake and in the same folder as the tests (if unit test),
* not generated by running your function then pasting it into the script,
* larger for integration and end-to-end tests,
* returned from a function or fixture for consistency.


### Write your test code to mirror your codebase

Modular, well-structured code is easier to write tests for.
As such, testing encourages you to structure your code well.
Directories of testing code should mirror the source code directories.
You might want one file per function/class or one per module.
Overall, it should be easy to identify which functions or classes your tests are for.

`````{tabs}
````{tab} Python
```
project/
│
├── src/
│   ├── __init__.py
│   ├── math.py
│   ├── strings.py
│   └── api.py
│
└── tests/
    ├── unit/
    │   ├── __init__.py
    │   ├── test_math.py
    │   └── test_strings.py
    │
    ├── integration/
    │   ├── __init__.py
    │   └── test_sum.py
    │
    └── end_to_end/
        ├── __init__.py
        └── test_end_to_end.py
```
````

````{tab} R
```
project/  
│  
├── .Rproj  
│  
├── R/  
│   ├── math.R  
│   ├── strings.R  
│   └── api.R  
│  
└── tests/  
    │  
    ├── testthat/  
    │   ├── test-maths_abs.R  
    │   ├── test-maths_sum.R  
    │   └── test-strings_option.R  
    │  
    └── testthat.R  
```
````
`````


### Good tests do not rely on external states

Tests should be clean and easy to maintain.

Independent tests that do not rely on external states make maintenance easier.
Tests should not need to be run in a specific order.
Testing frameworks will often randomly order the tests when running them for this reason.

Likewise, tests should leave no trace.
Use set up and tear down code to manage this.
Some testing frameworks provide tools like fixtures or mocks to help with this.

Tests should be independent from the code.
If the code changes, the tests may fail but test functions should not break.


### Tests are documentation and tests are documented

Good tests describe what it is they are testing.
They do this by using good naming practices within the test code.
A good test suite should tell a story - given this data, having run this function, we expect this output.
Tests should follow the relevant practices outlined in [](readable_code.md).

The story told in a testing suite helps developers understand what code is meant to do.
By defining expected outputs from given inputs, developers can understand the use of a particular piece of code.
Good testing suites recognise this and supplement other forms of documentation.


### Use bugs to improve your test suite

Every time you find a bug, write a test to check that it is fixed.
Doing so guarantees that your code covers common edge cases.
When you change your code or refactor your product you can be sure that bugs you have already fixed will not reappear.


### Avoid flickering tests by making them deterministic

Good tests are deterministic and repeatable.
Don't use randomness when writing tests.
The only thing that should cause a test to fail when it has been passing is if the tested code has changed.
Running the same test with the same tested code should always produce the same outcome.

In short, a test should either pass or fail every time, not "mostly pass".


### Writing tests at a later date

You should write tests when you write code.
However, this may not always be possible because of time, capability or tooling constraints.
Write test shells where you intend to write test - this highlights where testing is missing, which makes it easy to come back to later.

```{todo}
Add more examples here

[#116](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/116)
```

````{tabs}
```{code-tab} console Python
$ pytest
...

snippets/pytest_example.py::test_absolute_converts_negative_inputs PASSED [ 25%]
snippets/pytest_example.py::test_absolute_non_negative_inputs PASSED     [ 50%]
snippets/pytest_example.py::test_absolute_non_numeric_raises PASSED      [ 75%]
snippets/pytest_example.py::test_absolute_na SKIPPED                     [100%]

===================== 3 passed, 1 skipped in 0.11 seconds =====================
                                                                                    $
```

```{code-tab} r R
if (1 != 1) {
  stop("Something has gone terribly wrong")
}
```
````

Use [Continuous Integration](continuous-integration) where possible as it keeps testing associated with version control.

Where manual testing is carried out instead of writing test code, this must be documented to create an audit trail.
This documentation should include what has been tested and who has approved that it works as expected.


## Write test code only once

Where possible, reduce repetition in your tests. Tests are code too, so you should still [make this code reusable](functions).
Tests need not be totally singular, but, as with non-test code, repetition makes maintenance of test code more difficult and risky .
As with functional code, test code is much easier to maintain when it is modular and reusable.

```{todo}
Add examples to reducing repetition in tests to demonstrate these

[#29](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/29)
```


### Use fixtures to reduce repetition

As your test suite grows, many of your tests may use similar code to prepare your tests or to clean up after each test has run.
Copying these code snippets for each test is laborious and increases the risk of applying those steps inconsistently.

Fixtures help us to avoid this form of repetition in our tests.
With a fixture, you define your test preparation and clean up as functions.
You then use the fixture to carry out these steps consistently for each test that they are required for.

In Class-based testing frameworks, these functions tend to be separated into `SetUp` and `TearDown` functions.
These are set to run before and after each test, respectively.

Fixtures can be most useful when setting up a test object takes a large amount of time or resource.
They can be designed to run for each test, once for a group of tests or once for the whole test suite.
They are also useful for undoing the effects of each test run on the global environment.
For example, they can remove test data which has been written to a temporary file or database.

Reference material:

* [Python `pytest` Fixture](https://docs.pytest.org/en/stable/fixture.html) documentation
* [R `testthat` Fixture](https://testthat.r-lib.org/articles/test-fixtures.html) documentation


### Use parametrization to test multiple cases at once

Often, similar steps are taken when testing multiple combinations of inputs and outputs.
Parametrization allows us to reduce repetition in our code, in a similar way to reusable functions.
We specify the pairs of inputs and expected outputs, so that our testing tool can repeat a test for each scenario.

This approach is equivalent to using a for-loop to apply a test function over multiple inputs and expected outputs.
Using functionality from test packages may improve running efficiency and the detail given in test logs.

In `pytest`, this can be achieved using the [Parametrize mark](https://docs.pytest.org/en/stable/parametrize.html).

In R, the `patrick` package extends `testthat` to provide a
[`with_parameters_test_that`](https://rdrr.io/cran/patrick/man/with_parameters_test_that.html) function to achieve this.


## Run tests whenever you make changes to your project

Tests should be run whenever you make changes to your project.
This ensures that changes do not break the existing, intended functionality of your code.
Where tests fail, fix these before adding changes to a stable or production version of your code.

If you have altered the functionality of your code, this will likely break existing tests.
Failing tests are a good reminder that you should update your documentation and tests to reflect the new functionality.

If your collection of tests runs quickly, it's simplest to run them all often. This has the added benefit of capturing unexpected side-effects of your changes.
For example, you might pick up an unexpected failure in part of your code that you have not directly changed.

To ensure that tests are run consistently every time changes to code are made, you should automate the process using [continuous integration](automate-tests).


## Testing at multiple levels

Each level is important for different reasons.


### Unit testing

```{admonition} Key Learning
:class: admonition-learning

You should follow the [Introduction to Unit Testing course](https://learninghub.ons.gov.uk/course/view.php?id=499) for applied examples in Python and R.
The course also covers writing and documenting functions, and error handling.

Other resources include:
* Hadley Wickham's [testthat: getting started with testing](https://vita.had.co.nz/papers/testthat.pdf)
* [`pytest` getting started](https://docs.pytest.org/en/3.0.1/getting-started.html)
* Real Python [Getting Started With Testing in Python](https://realpython.com/python-testing/)
```

```{todo}
Testing in multiple environments?
* [tox](https://tox.readthedocs.io/en/latest/)/[nox](https://nox.thea.codes/en/stable/)
* [rhub](https://r-hub.github.io/rhub/)
```


### Integration testing


### Systems testing


## Use mocks where code cannot be easily decoupled

Tests should be specific.

If you can't refactor the code to make it easier to test specific aspects, then Mocks can be useful for removing unwanted factors.
Mocking is useful for removing things that we don't care about from the the test. But should not be used to avoid testing complex parts of code that you've written.
