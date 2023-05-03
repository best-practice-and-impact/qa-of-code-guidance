# Peer review

Peer review of code is a quality assurance activity where a developer, other than the code's author, views and tests the usage of a piece of code.

Peer review allows a fresh pair of eyes to take a look at your work.
It helps to assure that you have taken an appropriate approach to your analysis and may highlight errors in the analysis process.
Constructive review feedback helps you to improve your code quality and provides confidence in your work.
It acts to assure that our analysis is fit for purpose.

```{epigraph}
For analysis to be used to inform a decision it must be possible to assess its utility, reliability,
and the degree of validation and verification to which it has been subjected.

-- [The Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government)
```

[The Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government)
tells us that quality assurance of our analysis should be proportional to the complexity and business risk of the analysis.
This means that both internal and external peer review may be required to adequately assure your analysis.
External review is recommended if your analysis uses novel or complex techniques,
if comparison with other analyses cannot be used to challenge your results, or if the analysis is business critical.

```{epigraph}
Continuous challenge and improvement is essential to ensure that the people we serve – ministers and, of course, the public – have trust in our analysis. 

-- Nick Macphereson, former Permanent Secretary to the Treasury
```


## Focus reviews on code quality

Our [](checklists.md) provide an extensive list of good practices that reviewers can look for.
Many of these criteria consider the whole project.
You should tailor your review to the quality assurance criteria that the project is trying to meet and the scale of the review.

Reviewing is centered around conversations - asking yourself and the reviewer questions.
While reviewing changes to analytical code, example questions might be:


### Can I easily understand what the code does?

In more depth:

* Is the code sufficiently documented for me to understand it?
* Is there duplication in the code that could be simplified by refactoring into functions and classes?
* Are functions and class methods simple, using few parameters?

As we discussed in [](readable_code.md), good quality code is easier to read, understand and maintain.
Peer review improves the quality of our code through the constructive challenges of the reviewer.
As a reviewer, you might do this by suggesting alternative ways to represent the analysis or
by asking about decisions that have been made in the approach to the analysis.

Another benefit, particularly of internal review, is knowledge transfer.
Both the reviewer and reviewee are exposed to new ideas.
The reviewer must gain a low-level understanding of what the code is doing, in order to validate that it works as expected.
This may provide your team members with the understanding required to use and maintain your code in the future.


### Is the required functionality tested sufficiently?

If there are not tests for each part of the code, then we can't be sure that it works as expected.
As a reviewer, you should ask whether the amount of testing is proportionate given the risk to the analysis if the code does not work.


### How easy will it be to alter this code when requirements change?

In more depth:

* Are high level parameters kept in dedicated configuration files?
* Or would somebody need to work their way through the code with lots of manual edits to reconfigure for a new run?

Most analysis stems from some form of customer engagement.
Throughout design, implementation and review of analysis we must continue to assess whether our analysis is fit for purpose:
Does it meet the needs of the customer?
A project should document the scope of your analysis and any requirements, to make this assessment as easy as possible.
Additional documentation that supports the auditability of your analysis includes assumption logs,
technical reports describing the analysis and documentation on any verification or validation that has already been carried out.


### Can I generate the same outputs that the analysis claims to produce?

In more depth:

* Have dependencies been sufficiently documented?
* Is the code version, input data version and configuration recorded?

A key aspect of review is checking that the same results are acquired when running your code with the same input data.
Assurance that  analysis can be reproduced increases the trust in the results.

Note that each of these example questions focuses on important quality assurance practices in the code, rather than minor issues like code layout and style.


## Give practical feedback

Feedback should be practical and constructive.
For example, you should suggest an improvement or alternative that the developer may consider and learn from.
Although it may be necessary to highlight specific examples, you should avoid making feedback personal.

The CEDAR feedback model can be a useful framework for structuring review comments.
This model breaks review down into five sections:

1. Context - describe the issue and the potential impact.
2. Examples - give specific examples of when and where the issue has been present.
3. Diagnosis - use the example to discuss why this approach was taken, what could have been done differently and why the alternatives could be an improvement.
4. Actions - ask the person receiving feedback to suggest actions that they could follow to avoid this issue in future.
5. Review - revisit the discussion to look for progress following on the feedback.

This approach has been designed from a coaching or mentoring perspective, and can work well in verbal discussion or when giving written feedback.


## Document review feedback and outcomes

When you identify issues with code functionality or quality you should suggest improvements to solve these issues.
The code developer may respond to your comments to justify why they have taken a certain approach, otherwise they should act on your feedback before using the analysis.

It may be necessary to re-review changes that have resulted from your initial review, to confirm that your feedback has been actioned appropriately.

```{important}
It is essential that you document what you have considered in your review and how the developer has responded to your feedback.
This documentation should be kept close to the relevant version of the code, so that others can see what has been reviewed.
The easiest way to manage this is by using the Merge Request or Pull Request feature on your version control platform to conduct the review.
See [](version_control.md) for more information.
```


## Give consistent feedback

You might formalise your review using a template, to ensure that review is consistent within a project.
Templates are useful for setting criteria to review against.
You should tailor any template to reflect the scope of your review.
For example, small regular reviews may focus on smaller aspects of the analysis compared to a large project-wide review.
The general example below is written in Markdown, so that it can be used in version control platform Merge or Pull requests:


```{code-block} md
##  Code review

#### Documentation

Any new code includes all the following forms of documentation:

- [ ] **Function Documentation** as docstrings within the function definition.
- [ ] **Examples** demonstrating major functionality, which runs successfully locally.

#### Functionality

- [ ] **Installation**: Installation or build of the code succeeds.
- [ ] **Functionality**: Any functional claims of new code have been confirmed.
- [ ] **Automated tests**: Unit tests cover essential functions for a reasonable range
  of inputs and conditions. All tests pass on your local machine.
- [ ] **Packaging guidelines**: New code conforms to the project contribution
  guidelines.
---

### Review comments

*Insert detailed comments here!*

These might include, but not exclusively:

- bugs that need fixing (does it work as expected? and does it work with other code that it is likely to interact with?)
- alternative methods (could it be written more efficiently or with more clarity?)
- documentation improvements (does the documentation reflect how the code actually works?)
- additional tests that should be implemented (do the tests effectively assure that it  works correctly?)
- code style improvements (could the code be written more clearly?)

Your suggestions should be tailored to the code that you are reviewing.
Be critical and clear, but not mean. Ask questions and set actions.

```

Internal review should be carried out regularly within the development team.
Reviewing code written by those with more and less experience than you is beneficial for both reviewer and developer.
Similar questions can be asked from both perspectives, for the reviewer to get a good understanding of the approach and decisions behind the analysis.


## Give timely feedback

It's important that feedback is provided in good time, so that the review process does not hold up development of the code
and that issues can be addressed before more code is written using the same practices.

We strongly recommend applying pair programming for code review, as the most timely and practical method.
However, a separate review process may be necessary when multiple developers are not available to work at the same time.


### Review through pair programming

> Two heads are better than one.

Review doesn't have to be an arduous standalone task.
Pair programming combines the code writing and the review process into a single step.
Here, two or three developers work together to write a single piece of code.
Each developer takes turns to actively author parts of the code, while others provide real-time feedback on the code being written.

This practice encourages developers to consider why they are writing code in a particular way and to vocalise this ("programming out loud").
Additionally, it gives reviewers a chance to suggest improvements and question the author's approach as the code is written.
Working in this way can be more efficient than reviewing code separately - issues are identified sooner, so they are easier to fix.
Despite the upfront cost of two individuals writing the code, the resulting code is often higher quality and contains fewer bugs.

The rotational aspect of pair programming ensures that all team members gain experience from both the author and review perspective.
From both angles, you'll learn new programming and communication techniques.
In addition to this, sharing knowledge of how the code works across the team prevents too much risk being put on individuals.

Developers working in pairs can approve changes to code as it is written, however,
key discussions from pair programming sessions should still be documented to demonstrate which aspects of the code have been reviewed and discussed.

This blog post from the Government Digital Service provides
[more detailed steps to apply pair programming](https://gds.blog.gov.uk/2018/02/06/how-to-pair-program-effectively-in-6-steps/).


### Review separately when necessary

A separate review involves sharing your code with a reviewer, and receiving written feedback.
We describe this as separate, because code development and review are separate and the code author does not need to be present for the review.
This type of review is an iterative process, where the reviewer may make additional suggestions until they are satisfied with the code changes.

This form of review works best when changes to the code are small and frequent.
Requesting review of small but regular changes reduces the burden on reviewers, relative to large review of a complete project.
Similarly to pair programming, reviewing small changes to code allows you to catch issues sooner.

```{important}
If a project is only reviewed when all of the code has been written, this significantly reduces the benefit of review.

This creates a much larger burden on the reviewer.
Additionaly, any issues that are identified may take a lot of time to fix across the whole project.
A reviewer might highlight that certain quality assurance practices have not been used -
for example, there has not been enough documentation or automated testing in the project.
It would take a substantial amount of effort to add documentation and testing for the whole project.
If this was identified earlier, the improved practices could be applied as the remaining code is developed.
```

When you must carry out a review of larger or complete pieces of work, it may be worth reviewing different aspects of the code in separate sessions.
For example, focussing on documentation in one session and functionality in the next.

The thought of someone else reviewing your code in this way encourages good practices from the outset:

* Clear code and documentation - so that others with no experience can use and test your code
* Usable dependency management - so that others can run your code in their own environment

Separate review is aided by features of most version control platforms. See [](version_control.md) for more information.


#### Case study - rOpenSci review

Here we discuss a [review example from rOpenSci](https://ropensci.org/);
a community led initiative that curates open source, statistical R packages.
rOpenSci apply a rigorous peer review process to assure the quality of packages before including them in their collection.
This peer review process is entirely remote and is performed in the open, via GitHub pull requests.

In this example, from colleagues at Public Health England,
[the `fingertipsR` package is reviewed](https://github.com/ropensci/software-review/issues/168).
The initial comment describes the package that is being submitted and includes a check against a list of minimum requirements.
The [`goodpractice` R package](http://mangothecat.github.io/goodpractice/) is used to check that good R packaging practices have been followed.
[Continuous integration](continuous-integration) is commonly used to carry out automated checks on code repositories.
The reports from these checks can save reviewers time, by providing indicators of things like code complexity and test coverage.


#### Case studies

Here we discuss an example from [rOpenSci](https://ropensci.org/); a community led initiative that curates open source, statistical R packages.
rOpenSci apply a rigorous peer review process to assure the quality of packages before including them in their collection.
This peer review process is entirely remote and is performed in the open, via GitHub pull requests.

In this example, from colleagues at Public Health England, [the `fingertipsR` package is reviewed](https://github.com/ropensci/software-review/issues/168).
The initial comment describes the package that is being submitted and includes a check against a list of minimum requirements.
The [`goodpractice` R package](http://mangothecat.github.io/goodpractice/) is used to check that good R packaging practices have been followed.
[Continuous integration](https://www.atlassian.com/continuous-delivery/continuous-integration#:~:text=Continuous%20integration%20(CI)%20is%20the,builds%20and%20tests%20then%20run.)
is commonly used to carry out automated checks on code repositories.
The reports from these checks can save reviewers time, by providing indicators of things like code complexity and test coverage.

Two detailed external reviews are then conducted before the package is accepted - these reviews include additional checks for common aspects of code packages,
like documentation, examples and automated testing.
Perhaps the most informative part of these reviews, however, is the detailed bespoke comments.
Here the reviewers highlight problems, ask questions to clarify aspects of the package design and suggest improvements to the implementation of the code
(with examples).

Following the reviews, additional comments describe how the reviewers requested changes have been addressed.
And finally, there is a sign off to confirm that the reviewers are satisfied with the package.

Although this review looked at an entire, mature package, you can apply parts of this review process to smaller pieces of code as required.
