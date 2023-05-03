# Testing code

Code tests verify that your analytical code is working as expected. Where code documentation helps others to understand what you expect your code to do, testing assures that the the code meets these expectations. Without carrying out tests we have no assurance that our code works correctly, so we can't be sure that our analysis is fit for purpose.

Tests should be used proportionately for your analysis. This means writing more tests for parts of your code that are more complex or carry more risk.

Testing helps you assure your code quality and makes developing your code more efficient. Code that has not been tested is more likely to contain errors and require more maintenance in the future.

Tests come in many shapes and sizes, but usually follow the pattern:

1. Arrange - set up any objects needed for your test, e.g. example input data and expected output data.
2. Act - run the code that you are testing (one or more functions or methods).
3. Assert - verify that the code performed the expected action, e.g. that the output matched the expected output.

```{admonition} Key Learning
:class: admonition-learning

You should follow the [Introduction to Unit Testing course](https://learninghub.ons.gov.uk/course/view.php?id=499) for applied examples in Python and R. This course also covers writing and documenting functions, and error handling.

Other useful learning resources include:
* [`pytest` getting started](https://docs.pytest.org/en/3.0.1/getting-started.html)
* Real Python [Getting Started With Testing in Python](https://realpython.com/python-testing/)
* Hadley Wickham's [testthat: getting started with testing](https://vita.had.co.nz/papers/testthat.pdf) and [testing design in R](https://r-pkgs.org/testing-design.html)
```

In this section we assume that you are using a testing framework to run your tests (e.g. `pytest` for python or `testthat` for R) and have your code in a package. Not packaging your code will make it difficult to follow many of the testing good practices described here.

## Write reproducible tests

As analysts we routinely check that our analysis is carried out correctly. This might be done informally by running all or part of our analysis with example data or subsets of real data.

These tests give us confidence that our analysis is correct. However, it's important that we are able to reproduce the same checks against our code reproducibly. Code changes over time, so we need to be able to repeat these checks against the updated code. Additionally, other analysts should be able to carry out the same checks and get the same results.

Representing our tests as code allows us to consistently repeat the same steps. This lets us or another analyst to carry out the same verification again to get the same results. When you carry out a test manually, you should ensure that you add a code test to reproduce this.

Code that we write for testing should also follow the good practices described earlier on in this book, in particular [](readable_code).

### Write repeatable test

For us to be able to trust the results of our tests we need them to be repeatable. That is for them to give them same outcome if we run them more than once against the same version of our analysis code.

For tests to run repeatably each test must be independent. There should not be a shared state between tests, for example one test depending on another testing having already run. Many test runners will intentionally randomise the order that tests are executed to encourage this.

Where possible, test should be deterministic. Where your code relies on randomness tests should reuse the same random seed each time they are run.

Where this is not possible/logical for the scenario that you are testing you may want to run the test case multiple times and make an assertion about the distribution of the outcomes instead. For example, if we are testing a function that simulates a coin flip we might run it 100 times and check the proportion of heads versus tails is close to half (within a reasonable range).

## Run tests against all changes to your code

Tests should be run whenever you make changes to your analysis. This ensures that changes do not break the existing, intended functionality of your code. Running the entire collection of tests has the added benefit of detecting unexpected side-effects of your changes. For example, you might pick up an unexpected failure in part of your code that you have not directly changed.

Running tests regularly allows your to fix any issues before adding changes to a stable or production version of your code.

If you have altered the functionality of your code, this will likely break existing tests. Failing tests here act as a good reminder that your should update your documentation and tests to reflect the new functionality.

It's not easy to remember to run your tests manually at regular intervals. And you're right to think "surely this could be automated too?". [Continuous integration](continuous-integration) can be used to automate the running of tests and can be triggered when changes are made to your remote version control repository.

## Record the outcomes of your tests

For auditability, it is important that the outcome from running tests is recorded. You should record the test outcomes with the code, so that it is clear what tests have been carried out for a given version of the code.

As mentioned above, automating the running of tests on a version control platform is the simplest and most effective way to achieve this association between the code version and test outcomes.

## Minimise your test data

Tests for analytical code will usually require data.

```{warning} Key Learning

You must not copy the output from running your code to create your expected test outcomes. If you do this the test will check that the function is running in the same way that it ran when you generated the data. This assumes that your function is working correctly.

You must create your test data independently, ensuring that it reflects how you want your code to work, rather than how it currently works.
```

## Structure test files to match code structure

## Test that new logic is correct (unit tests)

## Test that different parts of the code interact correctly (integration tests)

## Test that the whole system works (end to end tests)

## Test that user needs are met (user acceptance tests)

## Minimise repetition in test code (fixtures and parameterised tests)

## Write tests before writing logic (TDD)

## Write tests to assure that bugs are fixed