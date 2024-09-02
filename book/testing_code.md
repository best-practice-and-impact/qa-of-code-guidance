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
When you have carried out a test manually, you should ensure that you add a code test to reproduce this.

Code that we write for testing should also follow the good practices described earlier on in this book, in particular [](readable_code).

## Write repeatable tests

For us to be able to trust the results of our tests we need them to be repeatable.
That is for them to give them same outcome if we run them more than once against the same version of our analysis code.

For tests to run repeatably each test must be independent.
There should not be a shared state between tests, for example a test should not depend on another test having already run.
Many test runners will intentionally randomise the order that tests are executed to encourage this.

Where possible, test should be deterministic.
As such, the only reason for a test to fail should be that the code being tested is incorrect.
Where your code relies on randomness tests should reuse the same random seed each time they are run.

Where this is not possible/logical for the scenario that you are testing, you may want to run the test
case multiple times and make an assertion about the distribution of the outcomes instead.
For example, if we are testing a function that simulates a coin flip we might run it 100 times and
check the proportion of heads versus tails is close to half (within a reasonable range).

## Run all tests against each change to your code

All tests should be run whenever you make changes to your analysis.
This ensures that changes do not break the existing, intended functionality of your code.
Running the entire collection of tests has the added benefit of detecting unexpected side-effects of your changes.
For example, you might detect an unexpected failure in part of your code that you didn't even change.

Running tests regularly allows you to fix any issues before  changes are added to a stable or production version of your code (e.g. the `main` Git branch).

If you have altered the functionality of your code, this will likely break existing tests.
Failing tests here act as a good reminder that your should update your tests and documentation to reflect the new functionality.
Many testing frameworks supporting writing tests as examples in the function documentation, which ties these together nicely.

It's not easy to remember to run your tests manually at regular intervals.
And you're right to think "surely this could be automated too?".
 You should use [continuous integration](continuous-integration) to automate
the running of tests.
Using these tools, tests can be triggered to run when any changes are made to your
remote version control repository.

## Record the outcomes of your tests

For auditability, it is important that the outcome from running tests is recorded.
You should record the test outcomes with the code, so that
it is clear which tests have been run successfully for a given version of the code.

As mentioned above, automating the running of tests on a version control platform is the simplest and
most effective way to achieve this association between the code version and test outcomes.
See [](continuous_integration) for further guidance on using these tools.

## Minimise your test data

Tests for analytical code will usually require data. To ensure that tests are clear in their meaning, you should use the smallest possible dataset for a test.

Good test data are:
* only just detailed enough data to carry out the test
* fake, static (hardcoded) and readable
* stored closely to the test

```{warning}
You must not copy the output from running your code to create your expected test outcomes.
If you do this the test will check that the function is running in the same way that it ran when you generated the data.
This assumes that your function is working correctly.

You must create your test data independently, ensuring that it reflects how you want your code to work, rather than how it currently works.
```

It's tempting to create a test dataset that closely mimics your real data, like the example below:

```{code-block} python
from my_package import add_columns
from pandas.testing import assert_frame_equal
import pandas as pd

def test_sum_columns():
    expected_output = pd.DataFrame(
        'region_1_sales':            [1000,  50000, 500 , 30000, 10000,   50000 ],
        'region_2_sales':            [4000,  45000, 1000, 13000, 60000,   80000 ],
        ...
        'region_30_sales':           [1500,  32000, 2000, 41000, 40000,   10000 ],
        'total_sales':               [85000, 92000, 7000, 110000, 600000, 400000]
    )

    input_data = expected_output.drop('total_sales')

    actual_output = sum_columns(
        df=input_data,
        column_to_assign="total_sales",
        columns_to_sum=["region_1_sales", "region_2_sales"]
        )
    assert_frame_equal(expected_output, actual_output)
```

However, we can still conduct the same test with much less data like so:

```{code-block} python
...

def test_sum_columns():
    expected_output pd.DataFrame(
        'input_1': [1, -1, -1, 0],
        'input_2': [1, -1,  1, 0]
        'outcome': [2, -2,  0, 0]
    )
    input_data = expected_output.drop('outcome')

    actual_output = sum_columns(
        df=input_data,
        column_to_assign="outcome",
        columns_to_sum=["input_1", "input_2"]
        )
    assert_frame_equal(expected_output, actual_output)
```

Using  minimal and general data in the test has made it clearer what is being tested.
In this case our function is very generic, so our test doesn't need to know the names of real columns in our data or even have similar values in the data.
The test data are focussed on testing specific, realistic cases.
This makes it easy to see that this function works correctly with positive, negative and zero values.

Note that the way we write our test affects how the function is implemented.
Using minimal, generalised data encourages you to follow good practices when designing your function.
This function doesn't know the name of the columns that it will use in advance, so they are passed as parameters.
This makes the function reusable.
We might have named the original function `sum_sales_columns`, but the more general name used here makes it clear
that we could use this to sum columns in any other context.

We used a single test function above, but could have created separate tests for each scenario and included tests for more than two input columns, for example.

## Structure test files to match code structure

In [](modular_code) we describe how complexity can be managed by separating code into related groups.
Modular, well-structured code is easier to write tests for.
But we also want to make it easy to identify which tests relate to which parts of our code.

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

```{code-block} python
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

The R  project structure above has one test file per function in the modules.
There are multiple test files for the `math.R` module because it contains more than one function.
Tests in these test files do not need grouping into classes, as the file name is used to indicate exactly which function or class is being tested.

These are the common conventions for each of Python and R, but are interchangeable.
Use the approach that makes it easiest for developers to identify the relationship between tests and the code they are testing.

Note that some test frameworks allow you to keep the tests in the same file as the code that is being tested.
This is a good way of keeping tests and code associated,
but you should ensure that good modular code practices are followed to separate unrelated code into different files.

## Test that new logic is correct using unit tests

When we implement new logic in code, tests are required to assure us that the code works as expected.

To make sure that your code work as expected, you should aim to write tests for each individual unit in your code.
A unit is the smallest modular piece of logic in the code - a function or method.

Unit tests should cover realistic use cases for your function, such as:
* boundary cases, like the highest and lowest expected input values
* positive, negative, zero and missing value inputs
* examples that trigger errors that have been defined in your code

When your function documentation describes the expected inputs to your function, there is less need to test unexpected cases.
If missuse is still likely or risky, then providing the user with an error is the best approach to mitigate this risk.

Logic that is reused from an existing packages that is already tested do not require tests when we use that logic alone.
You should be aware of wether your dependencies are sufficiently tested.
Newly developed packages or those with very few users are more likely to not be thoroughly tested.

## Test that different parts of the code interact correctly using integration tests

We define integration tests as those that test on a higher level that a unit. This includes testing that:
* multiple units work together correctly
* multiple high level functions work together (e.g. many units grouped into stages of a pipeline)
* the end to end analysis runs correctly and meets users needs
* the analysis works with typical inputs from other systems

Integration tests give us assurance that our analysis is fit for purpose.
Additionally, they give us safety when refactoring or rearranging large parts of of code.
Refactoring is an important part of managing the complexity of our analysis as it grows.

Consider a piece of analysis that has an end to end test to check that the overall system gives an expected outcome.
For example, it tests that output data are the right shape, in the right format and have specific properties (e.g. a specific distribution).
There might also be a "regression" test that check that the exact values in the output remain the same.
After any changes that are made to tidy up or refactor the
code, these end to end tests can be run to assure us that no functionality has been inadvertently changed.

We can similarly consider a high level stage of an analysis pipeline.
If we have a stage responsible for imputing missing values, we might create integration tests to check that all values are
imputed and that particular imputation methods were used for specific cases in our test data.
When changes are made to individual imputation methods we might not expect these general characteristics to change.
This test helps to identify cases where this inadvertently has changed.

```{note}
Integration tests are more robust when they focus on general high level outcomes that we don't expect to change often.
Integration tests that check very specific outcomes will need to be updated with any small change to the logic within the part that is being tested.
```

User acceptance tests are those that check that a high level user requirement has been met.
In analysis, these are likely part of an end to end test that checks that the output is fit for purpose.

```{todo}
Discuss testing interface with external systems (e.g. database).
Test that your code works, given the format of response that the system can give.
Mocks?
```

## Write tests to assure that bugs are fixed

Each time you find a bug in your code, you should write a new test to assert that the code works correctly.
Once the bug is fixed, this new test should pass and give you confidence that the bug has been fixed.

When you change or refactor your code in future, the new tests
will continue to assure that bugs you have already fixed will not reappear.
Doing this increases the coverage of your tests in a proportionate way.

## Write tests before writing logic

The best practice for testing code is to use test-driven development (TDD).
This is an iterative approach that involves writing tests before writing the logic to meet the tests.

For a piece of analysis logic, you should know in advance what the desired outcome is.
This might be from a user need (e.g. someone needs output data in a certain shape) or an internal requirement (e.g. we need to impute all missing values).
Given that you know the expected outcome, you can write the test before even thinking about how you are going to write the solution.

```{note}
This section is framed more like training. Once dedicated training has been produced this section will likely adapted to provide more concise guidance on the practice.
```

TDD typically repeats three steps:
1. Red - Write a test that we expect to fail
2. Green - Write or update our code to pass the new test
3. Refactor - Make improvements to the quality of the code without changing the functionality

As with any code that is adequately covered by tests, code written using TDD can be safely refactored.
We can be more confident that our tests will capture any changes that would unintentionally alter the way our code works.

The three steps above are repeated to gradually increase the complexity of our code.
The first test that is written should focus on the minimum functionality.
Then this minimal functionality is implemented, to do nothing more than the test requires.
On the next iteration the test becomes more complex, as does the code logic.
In each iteration the refactoring steps means that the increasing complexity of the code is managed.

This approach provides many benefits beyond good test coverage.
The iterative nature of TDD encourages you to follow a number of other good practices.
These include keeping test data minimal and keeping functions or classes simple and focussed on doing one thing well.
TDD requires practice but is proven to produce clean, robust and adaptable code.

[Behaviour driven development](https://en.wikipedia.org/wiki/Behavior-driven_development) and
[acceptance test driven development](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)
are extensions of TDD with a useful focus on user needs.

## Reduce repetition in test code (fixtures and parameterised tests)

Where possible, reduce repetition in your tests. Tests are code too, so you should still [make this code reusable](functions).
As with functional code, test code is much easier to maintain when it is modular and reusable.

### Use fixtures to reduce repetition in test set up

As your test suite grows, many of your tests may use similar code to prepare your tests or to clean up after each test has run.
You can be more tolerant of repetition in in test code.
However, copying code snippets for each test is laborious and increases the risk of applying those steps inconsistently.

You can use fixtures help to avoid this form of repetition in tests.
A fixture allows you to define your test preparation and clean up as functions.
You then use the fixture to carry out these steps consistently for each test that they are required for.

In Class-based testing frameworks, these functions tend to be separated into `SetUp` and `TearDown` functions.
These are set to run before and after each test, respectively.

Fixtures can be most useful when setting up a test object takes a large amount of time or resource.
They can be designed to run for each test, once for a group of tests or once for the whole test suite.

```{code-block} python
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
Starting a new spark session can take a few seconds, so creating a new session
for each test function would significantly increase the time it takes to run all of the tests.
With a session level scope, the function is called once for the whole testing session
and the resulting `SparkSession` object is shared between our tests.
Reusing the same `SparkSession` object is safe to do if none of our tests modify the object.

```{code-block} python
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

Similar steps are often repeated when testing multiple combinations of inputs and outputs.
Parametrization allows us to reduce repetition in our test code, in a similar way to writing our logic in functions.
You should specify pairs of inputs and expected outputs, so that your testing tool can repeat the same test for each scenario.

Using parameterisation in a test framework is equivalent to using a for-loop to apply a test function over multiple inputs and expected outputs.
Using functionality from test packages may provide improved running efficiency and more detailed reporting of test failures.

In `pytest`, this can be achieved using the [Parametrize mark](https://docs.pytest.org/en/stable/parametrize.html).

In R, the `patrick` package extends `testthat` to provide a
[`with_parameters_test_that`](https://rdrr.io/cran/patrick/man/with_parameters_test_that.html) function to achieve this.

```{todo}
Add examples of applying the same test logic to multiple cases.
Add emphasis on documenting each case or at least making it clear what is being tested.
```
