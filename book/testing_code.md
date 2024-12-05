# Testing code

Code tests verify that your analytical code is working as expected.
Where code documentation helps others to understand what you expect your code to do, testing assures that the code meets these expectations.
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

You should follow the [Introduction to Unit Testing course](https://learninghub.ons.gov.uk/course/view.php?id=1171) for applied examples in Python and R.
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
This lets us or another analyst carry out the same verification again to get the same results.
When you have carried out a test manually, you should ensure that you add a code test to reproduce this.

Code that we write for testing should also follow the good practices described earlier on in this book, in particular [](readable_code).

## Write repeatable tests

For us to be able to trust the results of our tests we need them to be repeatable.
That is for them to give the same outcome if we run them more than once against the same version of our analysis code.

For tests to run repeatably each test must be independent.
There should not be a shared state between tests, for example a test should not depend on another test having already run.
Many test runners will intentionally randomise the order that tests are executed to encourage this.

Where possible, tests should be deterministic.
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
Failing tests here act as a good reminder that you should update your tests and documentation to reflect the new functionality.
Many testing frameworks support writing tests as examples in the function documentation, which ties these together nicely.

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

Using  minimal and general data in the test has made it clearer what is being tested, and also avoids any unnecessary disclosure.
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
Having one test class per function/class that you are testing will make it clear that the group of tests relates to that function or class in your source code.

```{code-block} python
# An example for tests/unit/test_math.py

class TestAbs:
    def test_abs_all_positive_values(self):
        ...

    def test_abs_all_negative_values(self):
        ...
    
    ...


class TestSum:
    def test_sum_all_positive_values(self):
        ...

    def test_sum_all_negative_values(self):
        ...
    
    ...
```

Using classes for unit tests has a number of additional benefits, this allows us to reuse the same logic either by class inheritance, or through fixtures.
Similar to fixtures,
we are able to use the same pieces of logic through class inheritance in python.
However, it should be noted that it is easier to mix up and link unit tests when using class inheritance.
The following code block demonstrates an example of class inheritance which will inherit both the
variable and the `test_var_positive` unit test, meaning three unit tests are run.
We are able to overwrite the variable within the subclass at any time, but will still inherit defined functions/tests from the parent class.

```{code-block} python
class TestBase:
    var = 3

    def test_var_positive(self):
        assert self.var >= 0

class TestSub(TestBase):
    var = 8
    def test_var_even(self):
        assert self.var % 2 == 0
```


The R  project structure above has one test file per function in the modules.
There are multiple test files for the `math.R` module because it contains more than one function.
Tests in these test files do not need grouping into classes, as the file name is used to indicate exactly which function or class is being tested.
Tests in R are now linked together based on the file, previously named [contexts](https://testthat.r-lib.org/reference/context.html).
Context is now tied to test file name to ensure they are always synced.
The `context()` function is now depreciated and should be removed from your R script.

These are the common conventions for each of Python and R, but are interchangeable.
Use the approach that makes it easiest for developers to identify the relationship between tests and the code they are testing.

Note that some test frameworks allow you to keep the tests in the same file as the code that is being tested.
This is a good way of keeping tests and code associated,
but you should ensure that good modular code practices are followed to separate unrelated code into different files.
Additional arguments are made to separate tests and functions when you are packaging your code.
If unit tests and code are located together in the same file,
the unit tests would also be packaged and installed by additional users.
Therefore when packaging code,
the unit tests should be moved to an adjacent test folder as users will not need to have unit tests installed when installing the package.

When separating unit tests into main package and testing scripts, it is important to import your package to ensure the correct functions are being unit tested.
For the module structure outlined previously, we would use `from src.math import my_math_function`.
For R you need to specify the name of your package within the `testthat.R` file within your tests folder.

## Structuring tests

In order to maintain a consistency across modules you develop, you should follow [PEP8](https://www.python.org/dev/peps/pep-0008/) (python)
or [Google](https://google.github.io/styleguide/Rguide.html) / [tidyverse](https://style.tidyverse.org/) (R) standards when structuring unit tests.

For python this involves importing all needed functions at the beginning of the test file.
To ensure that the correct functions are imported from your module,
it is also recommended to install a local editable version into your virtual environment.
This is done by running `pip install -e .` and any changes made to your
module functions will also be updated in your python environment.
Following this it is recommended to define fixtures, classes and then test functions.
An example of this can be found below.
More information can be found in Real Python [Getting Started With Testing in Python](https://realpython.com/python-testing/).

Similar structure should be followed in R, with all modules loaded in the beginning of a test script.
Test contexts and then functions should be defined in turn as shown above.
For more information see [testing design in R](https://r-pkgs.org/testing-design.html).

Generally tests within the same file should follow some structure or order.
We recommend that the order that functions are defined in the main script is also mirrored
within the test scripts.
This will be easier for future developers to debug and follow.
It also ensures that no functions have been missed and do not have unit tests written.


## Test that new logic is correct using unit tests

When we implement new logic in code, tests are required to assure us that the code works as expected.

To make sure that your code works as expected, you should write tests for each individual unit in your code.
A unit is the smallest modular piece of logic in the code - a function or method.

Unit tests should cover realistic use cases for your function, such as:
* boundary cases, like the highest and lowest expected input values
* positive, negative, zero and missing value inputs
* examples that trigger errors that have been defined in your code

When your function documentation describes the expected inputs to your function, there is less need to test unexpected cases.
If misuse is still likely or risky, then providing the user with an error is the best approach to mitigate this risk.

Logic that is reused from an existing package that is already tested does not require tests when we use that logic alone.
You should be aware of whether your dependencies are sufficiently tested.
Newly developed packages or those with very few users are more likely to not be thoroughly tested.

## Test that different parts of the code interact correctly using integration tests

We define integration tests as those that test on a higher level than a unit. This includes testing that:
* multiple units work together correctly
* multiple high level functions work together (e.g. many units grouped into stages of a pipeline)
* the analysis works with typical inputs from other systems

Integration tests give us assurance that our analysis is fit for purpose.
Additionally, they give us safety when refactoring or rearranging large parts of code.
Refactoring is an important part of managing the complexity of our analysis as it grows.

We can similarly consider a high level stage of an analysis pipeline.
If we have a stage responsible for imputing missing values, we might create integration tests to check that all values are
imputed and that particular imputation methods were used for specific cases in our test data.
When changes are made to individual imputation methods we might not expect these general characteristics to change.
This test helps to identify cases where this inadvertently has changed.

```{note}
Integration tests are more robust when they focus on general high level outcomes that we don't expect to change often.
Integration tests that check very specific outcomes will need to be updated with any small change to the logic within the part that is being tested.
```

## Test that the analysis runs as expected using end to end tests

End to end testing (sometimes called system testing) checks the entire workflow from start to finish, ensuring all components work correctly in real-world scenarios. While integration testing focuses on the interaction of specific modules, end to end testing involves all elements of a pipeline. This is useful when refactoring code for example, by providing assurance that overall functionality remains unchanged. 

For example, a piece of analysis has an end to end test to check that outputs are generated and the data are the right shape or format. There might also be a "regression" test that checks that the exact values in the output remain the same. After any changes that are made to tidy up or refactor the code, these end to end tests can be run to assure us that no functionality has been inadvertently changed.

End to end tests can also be used to quality assure a project from an end user's perspective, and should be run in an environment that replicates the production environment as closely as possible. This type of testing can catch errors that individual unit tests might miss, and confirm that the output is fit for purpose and the user requirements are met. End to end testing is a form of 'black-box' testing, meaning the tester verifies functionality without focusing on the underlying code. It is therefore important to use end to end testing alongside other forms of testing such as unit tests.


## Isolate code tests from external systems

Testing code that interacts with an external system can be particularly challenging when you can't guarantee
that the system will provide you with the same response each time; this could include code querying a database or
making API requests, for example.

Best practice is to separate external system dependencies from your code tests as much as possible. This can mitigate against various risks, depending on your application:

- Testing database interaction with a production database could result in damage to, or loss of, data.
- Making real API calls when testing a function that handles requests could incur unintended monetary costs.

Isolating code from external systems allows for tests to run without reliance on the real systems; for example, tests for a database interaction that can still run even if the database connection goes down.
Writing tests in this way means that tests evaluate how your code handles an output or response, and not the system dependency itself.
This is another benefit of enforcing isolation in unit tests - helping you understand when errors are coming from an external system, and when they're coming from your code.
The unit of code being tested is referred to as the 'System Under Test' (SUT).

One way of achieving this is with mocking. This is where a response from an outside system is replaced with a mock object that your code can be tested against.
In this example, there's a function making an API request in `src/handle_api_request.py`, and two test functions in `tests/test_handle_api_request.py`.
The response from `requests.get()` is mocked with a `Mock()` object, to which `text` and `status_code` attributes are assigned.
The `get_response()` function can now be evaluated for how it handles successful and unsuccessful requests; but thanks to the mocking, get requests are not made to `http://example.com`.

```{code-block} python
# AI has been used to produce content within this artefact.

# src/handle_api_request.py
import requests

def get_response(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise(requests.HTTPError("Unsuccessful request"))

    return response.text

...

# tests/test_handle_api_request.py
from src.api_requests import get_response
import requests
import pytest
from unittest import mock

@mock.patch("requests.get")
def test_get_response_success(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.text = "Successful"
    mock_response.status_code = 200

    mock_requests_get.return_value = mock_response
    
    actual = get_response("http://example.com/good-request")
    assert(actual == "Successful")

@mock.patch("requests.get")
def test_get_response_fail(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_requests_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError):
        actual = get_response("http://example.com/bad-request")

```

These tests pass successfully. However, if the mocking was implemented incorrectly and the real request executed, our tests may continue to pass depending on how the response was handled by our function. Better practice is to assert that the mock function was called - for example, with `mock_function.assert_called()` or `mock_function.assert_called_one_with(parameter)` - in order be assured of the tests working as expected. Additional stringency comes from matching warnings and error message strings with `pytest.raises()`.

```{code-block} python
# tests/test_handle_api_request.py
from src.api_requests import get_response
import requests
import pytest
from unittest import mock

@mock.patch("requests.get")
def test_get_response_success(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.text = "Successful"
    mock_response.status_code = 200

    mock_requests_get.return_value = mock_response
    
    actual = get_response("http://example.com/good-request")
    assert(actual == "Successful")

    mock_requests_get.assert_called()
    mock_requests_get.assert_called_once_with("http://example.com/good-request")


@mock.patch("requests.get")
def test_get_response_fail(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_requests_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError, match="Unsuccessful request"):
        get_response("http://example.com/bad-request")

    mock_requests_get.assert_called()
    mock_requests_get.assert_called_once_with("http://example.com/bad-request")

```

You may also consider using fixtures to make test code more concise by generating the necessary `Mock` object attributes dynamically. [`Mock.reset_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.reset_mock) is used to remove the attributes associated with a mock object between different test cases.

```
# tests/test_handle_api_request.py
from src.api_requests import get_response
import requests
import pytest
from unittest import mock

@pytest.fixture(scope="function")
def mock_response():
    def _create_mock_response(url):
        """factory function allows flexible return values when evaluated"""
        mock_response = mock.Mock()
        if url == "http://example.com/good-request":
            mock_response.text = "Successful"
            mock_response.status_code = 200
        elif url == "http://example.com/bad-request":
            mock_response.status_code = 400
        return mock_response
    return _create_mock_response


@mock.patch("requests.get")
def test_get_response_all_conditions(mock_requests_get, mock_response):

    good_url = "http://example.com/good-request"
    mock_requests_get.return_value = mock_response(good_url)
    actual = get_response(good_url)
    assert actual == "Successful"
    mock_requests_get.assert_called_once_with(good_url)

    mock_requests_get.reset_mock()

    bad_url = "http://example.com/bad-request"
    mock_requests_get.return_value = mock_response(bad_url)
    with pytest.raises(requests.HTTPError, match="Unsuccessful request"):
        get_response(bad_url)
    mock_requests_get.assert_called_once_with(bad_url)

```

[Monkeypatching](https://docs.pytest.org/en/stable/how-to/monkeypatch.html#how-to-monkeypatch-mock-modules-and-environments) in `pytest` provides an alternative way of handling mock objects and attributes, and also allows for the mocking of environment variables.

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
This section is framed more like training. Once dedicated training has been produced this section will likely be adapted to provide more concise guidance on
the practice.
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
You can be more tolerant of repetition in test code.
However, copying code snippets for each test is laborious and increases the risk of applying those steps inconsistently.

You can use fixtures to help avoid this form of repetition in tests.
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

This example shows a fixture named `spark_session` with a testing session scope.
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

Fixtures can also be useful for undoing any effects each test run might have on the global environment.
For example, they can remove test data which has been written to a temporary file or database.
The example above shows how a fixture might be used to reset a test database between each test.
Here a test function scope is used, so the fixture is run separately for each test function that uses it.
The fixture performs a reset on the database after the database connection has been used by the test.

For usage details see the documentation for packages that offer fixtures:
* [Python `pytest` Fixture](https://docs.pytest.org/en/stable/fixture.html) documentation
* [R `testthat` Fixture](https://testthat.r-lib.org/articles/test-fixtures.html) documentation

### Use parameterisation to reduce repetition in test logic

Similar steps are often repeated when testing multiple combinations of inputs and outputs.
Parameterisation allows us to reduce repetition in our test code, in a similar way to writing our logic in functions.
You should specify pairs of inputs and expected outputs, so that your testing tool can repeat the same test for each scenario.

Using parameterisation in a test framework is equivalent to using a for-loop to apply a test function over multiple inputs and expected outputs.
Using functionality from test packages may provide improved running efficiency and more detailed reporting of test failures.

In `pytest`, this can be achieved using the [Parametrize mark](https://docs.pytest.org/en/stable/parametrize.html).

In R, the `patrick` package extends `testthat` to provide a
[`with_parameters_test_that`](https://rdrr.io/cran/patrick/man/with_parameters_test_that.html) function to achieve this.

### Define Source Code

Take the below function for example, it can take 2 arguments.

```{code-block} python
def sum_two_nums(num1:int, num2:int) -> int:
    """Sum two numbers. Numbers can be integer or float."""
    return num1 + num2
```

### Simple Parameterisation

It is simple to check multiple assertions for this simple function. In the most
basic example, simply define a parameterised list of parameter values and
expected outcomes.

```{code-block} python
import pytest

@pytest.mark.parametrize("num_1s, expected_out", [(1, 2), (-1, 0), (0, 1)])
def test_sum_two_nums_parameterise_arg_1(num_1s, expected_out):
    assert sum_two_nums(num1=num_1s, num2=1) == expected_out

```

We reference the parameter values and expected answers in the same way that we
access pytest fixtures, covered earlier in this article. Running `pytest -v`
reveals 3 tests are run, with the parameterised values printed to the console:

```{code-block}

collected 3 items                                                             

foo.py::test_sum_two_nums_parameterise_arg_1[1-2] PASSED                  [ 33%]
foo.py::test_sum_two_nums_parameterise_arg_1[-1-0] PASSED                 [ 66%]
foo.py::test_sum_two_nums_parameterise_arg_1[0-1] PASSED                  [100%]

============================= 3 passed in 0.00s ==============================

```

It would be trivial to repeat a similar parameterised test for `num_2` values.
But how is it possible to make assertions when parameterising **both**
arguments?

### Stacked Parameterisation

In order to test multiple values for `num1` and `num2`, a fixture should be
defined that returns a dictionary of the expected values. For example:

```{code-block} python

@pytest.fixture
def expected_answers() -> dict:
    """A nested dictionary of expected answers for all combinations in 0:5.

    First level key corresponds to `num1` and the second level key to `num2`.
    The dictionary values are the expected answers. So that when we subset the
    dictionary with parameterised values, we provide the expected values to
    assert statements.

    Returns
    -------
    dict
        Dictionary of cases and their expected tuples.
    """
    expected= {
        0: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4,},
        1: {0: 1, 1: 2, 2: 3, 3: 4, 4: 5,},
        2: {0: 2, 1: 3, 2: 4, 3: 5, 4: 6,},
        3: {0: 3, 1: 4, 2: 5, 3: 6, 4: 7,},
        4: {0: 4, 1: 5, 2: 6, 3: 7, 4: 8,},
    }
    return expected

```

This fixture of expected answers can be served to a parameterised test and the
returned dictionary can be accessed to provide the expected answer for
parameter combinations. In order to parameterise both of the required arguments,
the parameterise statements are simply stacked on top of each other:

```{code-block} python

@pytest.mark.parametrize("num1s", range(0,5))
@pytest.mark.parametrize("num2s", range(0,5))
def test_sum_two_nums_stacked_parameterise(num1s, num2s, expected_answers):
    assert sum_two_nums(
        num1=num1s, num2=num2s
        ) == expected_answers[num1s][num2s]
```

Executing this test with `pytest -v` shows all combinations are tested:

```{code-block}
collected 25 items                                                            

foo.py::test_sum_two_nums_stacked_parameterise[0-0] PASSED                [ 14%]
foo.py::test_sum_two_nums_stacked_parameterise[0-1] PASSED                [ 17%]
foo.py::test_sum_two_nums_stacked_parameterise[0-2] PASSED                [ 21%]
foo.py::test_sum_two_nums_stacked_parameterise[0-3] PASSED                [ 25%]
foo.py::test_sum_two_nums_stacked_parameterise[0-4] PASSED                [ 28%]
foo.py::test_sum_two_nums_stacked_parameterise[1-0] PASSED                [ 32%]
foo.py::test_sum_two_nums_stacked_parameterise[1-1] PASSED                [ 35%]
foo.py::test_sum_two_nums_stacked_parameterise[1-2] PASSED                [ 39%]
foo.py::test_sum_two_nums_stacked_parameterise[1-3] PASSED                [ 42%]
foo.py::test_sum_two_nums_stacked_parameterise[1-4] PASSED                [ 46%]
foo.py::test_sum_two_nums_stacked_parameterise[2-0] PASSED                [ 50%]
foo.py::test_sum_two_nums_stacked_parameterise[2-1] PASSED                [ 53%]
foo.py::test_sum_two_nums_stacked_parameterise[2-2] PASSED                [ 57%]
foo.py::test_sum_two_nums_stacked_parameterise[2-3] PASSED                [ 60%]
foo.py::test_sum_two_nums_stacked_parameterise[2-4] PASSED                [ 64%]
foo.py::test_sum_two_nums_stacked_parameterise[3-0] PASSED                [ 67%]
foo.py::test_sum_two_nums_stacked_parameterise[3-1] PASSED                [ 71%]
foo.py::test_sum_two_nums_stacked_parameterise[3-2] PASSED                [ 75%]
foo.py::test_sum_two_nums_stacked_parameterise[3-3] PASSED                [ 78%]
foo.py::test_sum_two_nums_stacked_parameterise[3-4] PASSED                [ 82%]
foo.py::test_sum_two_nums_stacked_parameterise[4-0] PASSED                [ 85%]
foo.py::test_sum_two_nums_stacked_parameterise[4-1] PASSED                [ 89%]
foo.py::test_sum_two_nums_stacked_parameterise[4-2] PASSED                [ 92%]
foo.py::test_sum_two_nums_stacked_parameterise[4-3] PASSED                [ 96%]
foo.py::test_sum_two_nums_stacked_parameterise[4-4] PASSED                [100%]

============================= 25 passed in 0.01s =============================

```

## Testing SQL
Although testing SQL is outside the scope of this guidance, many of the concepts discussed
in this guidance are also applicable to SQL. In SQL,
single queries often contain several parts. These can be more readily
tested by breaking up these queries and taking a more step-by-step approach,
similar to breaking up functions. Integration testing can be used to verify
that queries and functions behave as expected when combined.

Functions that interact with a database (DB) should be tested within a development
environment, rather than with a production database. This is in order to prevent
unintended data modification or deletion. Functions can also be unit tested
from simplified dummy data.

There are a range of established SQL testing frameworks. Examples include [tSQLt](https://github.com/tSQLt-org/tSQLt)
and [pgTAP](https://github.com/theory/pgtap/) for Postgres.


## In a time crunch? The risks to skipping tests
In an ideal world, testing code would never be skipped, keeping the software reliable,
and easily reproducible. However, in practice there are times when skipping tests may be necessary—
perhaps due to tight deadlines, limited resources, or the need to quickly get a feature up
and running. While this can save time in the moment, it’s important to be cautious, as
skipping tests can lead to hidden problems that may become harder to fix later, particularly
as the project grows. Whenever tests are set aside, it’s best to have a plan for going back to add
them, to avoid risks to the stability and quality of the software.