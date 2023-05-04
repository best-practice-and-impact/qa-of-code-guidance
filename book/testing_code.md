# Testing code

Code tests verify that your analytical code is working as expected.
Where code documentation helps others to understand what you expect your code to do, testing assures that the the code meets these expectations.
Without carrying out tests we have no assurance that our code works correctly, so we can't be sure that our analysis is fit for purpose.

Tests should be used proportionately for your analysis.
This means writing more tests for parts of your code that are more complex or carry more risk.

Testing helps you assure your code quality and makes developing your code more efficient.
Code that has not been tested is more likely to contain errors and require more maintenance in the future.

Good tests tell a story - given this data, having run this code, we expect this output.
Tests come in many shapes and sizes, but usually follow the pattern:

1. Arrange - set up any objects needed for your test, e.g. example input data and expected output data.
2. Act - run the code that you are testing (one or more functions or methods).
3. Assert - verify that the code performed the expected action, e.g. that the output matched the expected output.

```{admonition} Key Learning
:class: admonition-learning

You should follow the [Introduction to Unit Testing course](https://learninghub.ons.gov.uk/course/view.php?id=499) for applied examples in Python and R.
This course also covers writing and documenting functions, and error handling.

Other useful learning resources include:
* [`pytest` getting started](https://docs.pytest.org/en/3.0.1/getting-started.html)
* Real Python [Getting Started With Testing in Python](https://realpython.com/python-testing/)
* Hadley Wickham's [testthat: getting started with testing](https://vita.had.co.nz/papers/testthat.pdf) and [testing design in R](https://r-pkgs.org/testing-design.html)
```

In this section we assume that you are using a testing framework to run your tests (e.g. `pytest` for python or `testthat` for R) and have your code in a package.
Code that is not in a package can be more difficult to test and follow the testing good practices described here.

## Write reproducible tests

As analysts we routinely check that our analysis is carried out correctly.
This might be done informally by running all or part of our analysis with example data or subsets of real data.

These tests give us confidence that our analysis is correct.
However, it's important that we are able to reproduce the same checks against our code reproducibly.
Code changes over time, so we need to be able to repeat these checks against the updated code.
Additionally, other analysts should be able to carry out the same checks and get the same results.

Representing our tests as code allows us to consistently repeat the same steps.
This lets us or another analyst to carry out the same verification again to get the same results.
When you carry out a test manually, you should ensure that you add a code test to reproduce this.

Code that we write for testing should also follow the good practices described earlier on in this book, in particular [](readable_code).

### Write repeatable test

For us to be able to trust the results of our tests we need them to be repeatable.
That is for them to give them same outcome if we run them more than once against the same version of our analysis code.

For tests to run repeatably each test must be independent.
There should not be a shared state between tests, for example one test depending on another testing having already run.
Many test runners will intentionally randomise the order that tests are executed to encourage this.

Where possible, test should be deterministic.
As such, the only reason for a test to fail should be that the code being tested is incorrect.
Where your code relies on randomness tests should reuse the same random seed each time they are run.

Where this is not possible/logical for the scenario that you are testing you may want to run the test
case multiple times and make an assertion about the distribution of the outcomes instead.
For example, if we are testing a function that simulates a coin flip we might run it 100 times and
check the proportion of heads versus tails is close to half (within a reasonable range).

## Run all tests against each change to your code

All tests should be run whenever you make changes to your analysis.
This ensures that changes do not break the existing, intended functionality of your code.
Running the entire collection of tests has the added benefit of detecting unexpected side-effects of your changes.
For example, you might pick up an unexpected failure in part of your code that you have not directly changed.

Running tests regularly allows your to fix any issues before adding changes to a stable or production version of your code.

If you have altered the functionality of your code, this will likely break existing tests.
Failing tests here act as a good reminder that your should update your documentation and tests to reflect the new functionality.

It's not easy to remember to run your tests manually at regular intervals.
And you're right to think "surely this could be automated too?".
[Continuous integration](continuous-integration) can be used to automate
the running of tests and can be triggered when changes are made to your
remote version control repository.

## Record the outcomes of your tests

For auditability, it is important that the outcome from running tests is recorded.
You should record the test outcomes with the code, so that
it is clear what tests have been carried out for a given version of the code.

As mentioned above, automating the running of tests on a version control platform is the simplest and
most effective way to achieve this association between the code version and test outcomes.
See [](continous_integration) for details.

## Minimise your test data

Tests for analytical code will usually require data. To ensure that tests are clear in their meaning, you should use the smallest possible dataset for a test.

Good test data are:
* just enough data to carry out the test
* fake, static (hardcoded) and readable
* stored closely to the test

```{warning} Key Learning
You must not copy the output from running your code to create your expected test outcomes.
If you do this the test will check that the function is running in the same way that it ran when you generated the data.
This assumes that your function is working correctly.

You must create your test data independently, ensuring that it reflects how you want your code to work, rather than how it currently works.
```

```{todo}
EXAMPLE OF MINIMISING TEST DATA
```

## Structure test files to match code structure

In [](modular_code) we describe how complexity can be managed by separating code into related groups.
Modular, well-structured code is easier to write tests for.

You should mirror the structure of your code in the structure of your test files.
You might use one test file per function/class or one test file per module.
Overall, the aim is to make it easy to find the tests for a given function or class and vice versa.

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
    │   ├── test_math.py
    │   └── test_strings.py
    │
    ├── integration/
    │   └── test_api.py
    │
    └── end_to_end/
        └── test_end_to_end_pipeline.py
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

The Python example above has one file containing unit tests for each module (group of related functions and classes).
When using this structure you may want to also group multiple test functions into test classes.
Having one test class per function/class that you are testing will make it clear that the group of tests relates to a that function or class in your source code.

```{python}
# An example for tests/unit/test_math.py

class TestAbs:
    def test_abs_all_positive_values():
        ...

    def test_abs_all_negative_values():
        ...
    
    ...


class TestSum:
    def test_sum_all_positive_values():
        ...

    def test_sum_all_negative_values():
        ...
    
    ...
```

The R example above has one test file per function in the modules.
There are multiple test files for the `math.R` module because it contains more than one function.
Tests in these test files do not need grouping into classes, as the file name is used to indicate exactly which code is being tested.

These are the common conventions for each of Python and R, but are interchangeable.
Use the approach that makes it easiest for developers to identify the relationship between tests and the code they are testing.


## Test that new logic is correct (unit tests)

## Test that different parts of the code interact correctly (integration tests)

## Test that the whole system works (end to end tests)

## Test that user needs are met (user acceptance tests)

## Reduce repetition in test code (fixtures and parameterised tests)

Where possible, reduce repetition in your tests. Tests are code too, so you should still [make this code reusable](functions).
As with functional code, test code is much easier to maintain when it is modular and reusable.

### Use fixtures to reduce repetition in test set up

As your test suite grows, many of your tests may use similar code to prepare your tests or to clean up after each test has run.
Copying these code snippets for each test is laborious and increases the risk of applying those steps inconsistently.

Fixtures help us to avoid this form of repetition in our tests.
With a fixture, you define your test preparation and clean up as functions.
You then use the fixture to carry out these steps consistently for each test that they are required for.

In Class-based testing frameworks, these functions tend to be separated into `SetUp` and `TearDown` functions.
These are set to run before and after each test, respectively.

Fixtures can be most useful when setting up a test object takes a large amount of time or resource.
They can be designed to run for each test, once for a group of tests or once for the whole test suite.

```{python}
import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark_session():
    """Session-wide SparkSession to optimise testing PySpark functions."""
    spark_session = SparkSession.builder.master("local[*]").getOrCreate()
    yield spark_session
    spark_session.stop()

def test_my_function(spark_session):
    ...

def test_another_function(spark_session):
    ...
```

This examples shows a fixture named `spark_session` with a testing session scope.
Starting a new spark session can take a few seconds, so creating a new session for each test function would significantly increase the time it takes to run all of the tests.
With a session level scope, the function is called once for the whole testing session and the resulting `SparkSession` object is shared between our tests.
Reusing the same `SparkSession` object is safe to do if none of our tests modify the object.

```{python}
import pytest

@pytest.fixture(scope="function")
def database_connection():
    database_connection = connect_to_test_database()
    yield database_connection
    database_connection.reset_to_default()

def test_my_function(database_connection):
    ...

def test_another_function(database_connection):
    ...
```

Fixtures can also useful for undoing any effects each test run might have on the global environment.
For example, they can remove test data which has been written to a temporary file or database.
The example above shows how a fixture might be used to reset a test database between each test.
Here a test function scope is used, so the fixture is run separately for each test function that uses it.
The fixture performs a reset on the database after the database connection has been used by the test.

For usage details see the documentation for packages that offer fixtures:
* [Python `pytest` Fixture](https://docs.pytest.org/en/stable/fixture.html) documentation
* [R `testthat` Fixture](https://testthat.r-lib.org/articles/test-fixtures.html) documentation

### Use parametrization to reduce repetition in test logic

Often, similar steps are taken when testing multiple combinations of inputs and outputs.
Parametrization allows us to reduce repetition in our code, in a similar way to reusable functions.
We specify pairs of inputs and expected outputs, so that our testing tool can repeat a test for each scenario.

This approach is equivalent to using a for-loop to apply a test function over multiple inputs and expected outputs.
Using functionality from test packages may provide improved running efficiency and detail given in test logs.

In `pytest`, this can be achieved using the [Parametrize mark](https://docs.pytest.org/en/stable/parametrize.html).

In R, the `patrick` package extends `testthat` to provide a [`with_parameters_test_that`](https://rdrr.io/cran/patrick/man/with_parameters_test_that.html) function to achieve this.

```{todo}
EXAMPLES SHOWING REPEATED TEST LOGIC AND PARAMETERISED TEST
```

## Write tests before writing logic (TDD)

## Write tests to assure that bugs are fixed

Each time you find a bug in your code, write a new test to assert that the code works correctly.
This gives you confidence that the bug has been fixed.
When you change or refactor your code in future, the new tests will continue to assure that bugs you have already fixed will not reappear.
Doing this increases the coverage of your tests in a proportionate way.

