# Unit Testing

Test your code to make sure it does what you expected it to.
Just because code runs without errors and produces outputs that look plausible does not guarantee that it works as intended!

There are many ways to test code. Usually, testing is a lot easier when your code is modular or packaged.
Make sure your tests are proportionate to risks and complexity.
Ideally, tests should be formalised, whether they are manual or automated.

Tests are not a tick box exercise! Each test should serve a clear purpose.
Good tests will help you spot issues with the code before errors happen and speed up code production.

Further details can be viewed in the [testing code chapter of this book][testing-code-chapter].

## Minimum Standards

To meet the minimum standard for unit testing, we expect:

- Unit tests are used throughout the codebase and all tests pass.
- Tests are updated and re-run whenever *any* functionality is changed.
- Integration or end-to-end tests are implemented, re-run, and pass whenever functionality is changed.

## Advanced Techniques  

More advanced users may also consider:

- Using continuous integration (CI) pipelines to automatically run tests when creating a merge request  
 (see [GitHub CI documentation][ci-pipeline-documentation-github] for more details).
- Following [test-driven development][test-driven-development] (TDD): write unit tests first, then implement code to make those tests pass.
- Automating additional quality checks (for example, linting, type checks, and test reporting).
- Testing that output files are created in expected locations (typically using temporary file utilities).


## Test Coverage

Coverage metrics are useful for showing whether lines of code were executed during tests, but they should not be used alone to assess test quality.

For example, a simple test that runs the main pipeline without asserting expected outputs may result in very high coverage.
By contrast, a package with thoroughly tested lower-level functions may show lower overall coverage while still being more rigorously tested.

Those interested may wish to read more about [the fallacy of unit test coverage][unit-test-coverage-fallacy].


[ci-pipeline-documentation-github]: https://docs.github.com/en/actions/tutorials/build-and-test-code/python
[test-driven-development]: https://en.wikipedia.org/wiki/Acceptance_test-driven_development
[testing-code-chapter]: ./testing_code.md
[unit-test-coverage-fallacy]: https://medium.com/@eamonn.faherty_58176/the-fallacy-of-unit-test-coverage-9a63c919388b
