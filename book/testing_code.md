# Testing Code

Testing here refers to automated tests that assert that your code is working as expected.
Where code documentation specifies what code should do, testing assures that this specification is true.

The core concept of testing is **"Does my code give do what I expect it to, given realistic inputs?"**.


## What to test ★☆☆☆☆

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


A check-list for possible tests that may be relevant to your code:
* Have I tested realistic combinations of my codes input parameters?
* Have I tested any discrete outputs once?
* Have I tested the boundaries of non-discrete outputs?
* Are informative errors raised when the code is not used in a valid or correct way?
* Are informative warnings raised when the code is not used in a standard way?


Don't worry if this writing all of these tests sounds like a large task.
We'll describe ways of reducing the burden of writing and maintaining tests in later sections.
In particular see Test Parametrisation.

The testing frameworks described here are:
* `pytest` for Python
* `{testthat}` for R

Though other common frameworks are:
* `unittest` built into Python
* `{Runit}` for R



## Layers of Testing ★☆☆☆☆

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

In this chapter we will cover describe a more formalised method for testing.

In order of increasing scale, the main layers of testing covered here are:

* Unit testing - assuring that functions or class methods perform as expected
* Integration testing - assuring that multiple units interact with each other as expected
* End-to-end or system testing - verifying that a complete system meets its requirements

[Acceptance testing](https://en.wikipedia.org/wiki/Acceptance_testing) is often considered as additional level, but is not covered here.

The following sections will climb through these layers of testing. Please note that principles covered early on also apply at subsequent levels.


## Structuring Test Code ★☆☆☆☆



## Unit Testing ★★☆☆☆


<!-- 
````{tabs}

```{code-tab} py

```

```{code-tab} r
```

````
-->


## Integration Testing ★★★☆☆


## End-to-end Testing ★★★☆☆