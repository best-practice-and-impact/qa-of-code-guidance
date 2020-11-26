# Peer review

Peer review of code is a quality assurance activity, where a developer other than the code's author views and tests the usage of a piece of code.

```{epigraph}
For analysis to be used to inform a decision it must be possible to assess its utility, reliability, and the degree of validation and verification to which it has been subjected.

-- [The Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government)
```

## Why do we need peer review?

Peer review allows a fresh pair of eyes to take a look at your work. It validates that you have taken a correct approach to your analysis and may highlight errors. This constructive feedback helps you to improve your code quality and provides confidence in your work. It acts to make sure that our analysis is fit for purpose.

```{epigraph}
Continuous challenge and improvement is essential to ensure that the people we serve – ministers and, of course, the public – have trust in our analysis. 

-- Nick Macphereson, former Permanent Secretary to the Treasury
```

[The Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) tells us that quality of assurance of our analysis should be proportional to the complexity and business risk of the analysis. This means that both internal and external peer review may be required to adequately assure your analysis. Particularly if your analysis uses novel or complex techniques, where comparison with other analyses cannot be used to challenge your results, or if the analysis is business critical.

Most analysis stems from some form of customer engagement. Throughout design, implementation and review of analysis we must continue to assess whether our analysis is fit for purpose. **Does it meet the needs of our customer?** Your project should document the scope of your analysis and any requirements, to make this assessment as easy as possible. Regular contact with customers helps to keep these requirements up to date. Additional documentation that supports the auditability of your analysis includes assumption logs, technical reports describing the analysis and documentation on any verification or validation that has already been carried out.

As we discussed in [](core_programming.md), good quality code is easier to read, understand and maintain. Peer review improves the quality of our code through the constructive challenges from the reviewer. A reviewer might do this by suggesting alternative ways to represent your analysis or they may ask questions to check the reasons behind decisions in your coding approach and analysis as a whole.

Moreover, effective peer review requires and, therefore, enforces reproducibility. A key aspect of review is checking that the same results are acquired when running your code with the same input data. Assurance that your analysis can be reproduced increases the trust in your results.

Another benefit, particularly of internal review, is knowledge transfer. Both the reviewer and reviewee are exposed to new ideas. The reviewer must gain a low-level understanding of what the code is doing, in order to validate that it works as expected. This may provide your team members with the understanding required to use and maintain your code in the future.


## What should we review?

When reviewing code, you can ask yourself the following questions:
* Can I easily understand what the code does?
    * Is the code sufficiently documented for me to understand it?
    * Is there duplication in the code that could be simplified by refactoring into functions and classes?
    * Are functions and class methods simple, using few parameters?
* Does the code fulfil its requirements?
* Is the required functionality tested sufficiently?
* How easy will it be to alter this code when requirements change? They always do.
    * Are high level parameters kept in a dedicated configuration files? Or would somebody need to work their way through the code with lots of manual edits to reconfigure for a new run?
* Can I generate the same outputs that the analysis claims to produce?
    * Have dependencies been sufficiently documented?
    * Is the code version, input data version and configuration recorded?
* Is the code style consistent?

In addition to asking these questions, you might formalise your review using a template. Templates are useful for setting criteria to review against. You should tailor any template to reflect the scope of your review. For example, small regular reviews may focus on smaller aspects of the analysis than a large project-wide review. The general example below is written in Markdown, so that it can be used in Git platform Pull/Merge requests:


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

#### Final approval (post-review)

The author has responded to my review and made changes to my satisfaction.
- [ ] **I recommend merging this request.**

Estimated time spent reviewing: #

---

### Review comments

*Insert detailed comments here!*

These might include, but not exclusively:

- bugs that need fixing (does it work as expected? and does it work with other code
  that it is likely to interact with?)
- alternative methods (could it be written more efficiently or with more clarity?)
- documentation improvements (does the documentation reflect how the code actually works?)
- additional tests that should be implemented (do the tests effectively assure that it
  works correctly?)
- code style improvements (could the code be written more clearly?)

Your suggestions should be tailored to the code that you are reviewing.
Be critical and clear, but not mean. Ask questions and set actions.

```

Here we discuss an example from [rOpenSci](https://ropensci.org/); a community led initiative that curates open source, statistical R packages. rOpenSci apply a rigorous, open peer review process to assure the quality of packages before including them in their collection.

In this example, from colleagues at Public Health England, [the `fingertipsR` package is reviewed](https://github.com/ropensci/software-review/issues/168). The initial comment, which describes the package, includes a check against a list of minimum requirements. Two detailed external reviews are then conducted before the package is accepted - these reviews include additional checks for common aspects of code packages, like documentation, example and automated testing. Perhaps the most informative part of these reviews, however, is the detailed comments. Here the reviewers highlight problems, ask questions to clarify aspects of the package design and suggest improvements to the implementation of the code (with examples). Following the reviews, additional comments describe how the reviewers requested changes have been addressed. And finally, there is a sign off to confirm that the reviewers are satisfied with the package.

Internal review should be carried out within your teams. Reviewing code from those with more and less experience is beneficial.


## How do we approach code review?

### Pair programming

> Two heads are better than one.

This practice combines the code writing and review process into one step. Here, two or three developers work together on a writing a single piece of code. Each developer takes turns to actively author parts of the code, while others provide real time feedback on the code being written.

This encourages developers to think about and vocalise why they are writing code in a particular way. It gives reviewers a chance to suggest improvements and question the author's approach as they write the code. The rotational aspect of this practice ensures that all team members gain experience from both the author and review perspective. From both angles, you'll learn new techniques and practices.

If used regularly, this approach can help you to get used to receiving constructive feedback and being more open to improve your coding practices.


### Remote review

This approach essentially involves sharing your code with a reviewer, and receiving constructive comments following the review. This may be an iterative process, until the reviewer is satisfied with the resulting code.

This can work best where changes are small and frequent. Requesting review of small but regular changes reduces the burden on reviewers, relative to large review of a complete project.
When reviewing larger pieces of work, it may be worth reviewing different aspects of the code is separate passes. For example, focussing on documentation in one session and then functionality in the next.

The thought of someone else reviewing your code in this way encourages good practices from the outset:
* Clear code and documentation - so that others with no experience can use and test your code
* Usable dependency management - so that others can run your code in their own environment

This form of review is aided by features of most version control platforms, namely the Pull request (or equivalent). See [](version_control.md) for more information.

```{todo}
There's probably an example from ROpenSci we can point people to for peer review

https://github.com/ropensci/software-review/issues/168

[#26](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/26)
```