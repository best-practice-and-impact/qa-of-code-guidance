# Peer Review

Peer review of code is a quality assurance activity, where a developer other than the code's author views and tests the usage of piece of code.

## Rationale

### Why do we need peer review

```{todo}

content pls

```
### What to review

When reviewing code, you might ask yourself the following questions:
* Am I able to easily understand what the code is doing?
    * Is the code sufficiently documented?
    * Is there any duplication in the code?
    * Are functions and class methods simple, using few parameters?
* Does the code fulfil its requirements?
* Is the required functionality tested sufficiently?
* How easy will it be to alter this code when requirements change? They always do.
    * Are high level parameters kept in a dedicated configuration file?
* Does the code style appear to be consistent?
* Can I generate the same outputs that the analysis claims to produce?
    * Have dependencies been sufficiently documented?
    * Is the code version, data version and configuration recorded?

You might use a review template to formalise review in your development process.
This example is written in Markdown, so that it can be used in Git platform Pull/Merge requests:


```{code-block} markdown

##  Code Review

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

### Review Comments

*Insert detailed comments here!*

These might include, but not exclusively:

- bugs that need fixing (does it work as expected? and does it work with other code
  that it is likely to interact with?)
- alternative methods (could it be written more efficiently?)
- documentation improvements (does it reflect what the code actually does?)
- additional tests that should be implemented (do the tests effectively assure that it
  works correctly?)
- code style improvements (could the code be written more clearly?)

Your suggestions should be tailored to the code that you are reviewing.
Be critical and clear, but not mean. Ask questions and set actions.

```

## Review Approaches

### Pair programming

> Two heads are better than one

This practice combines the code writing and review process into one step.
Here, two or three developers work together on a writing a single piece of code.
Each developer takes turns to actively author parts of the code, while others provide real time feedback on the code being written.

This encourages developers to think about and vocalise why they are writing code in a particular way.
It gives reviewers a chance to suggest improvements and question the author's approach as they write code.
The rotational aspect of this practice ensures that all team members gain experience from both the author and review perspective.
From both angles,  you'll to learn new techniques and practices.

If used regularly, this approach can help you to get used to receiving constructive feedback and being more open to improve your coding practices.

An alternative to this is the over-the-shoulder review technique, where one developer authors for the entire session.
This can be useful when working with a mentor, but it is often more useful for a mentor to lead by example.


### Remote Review

This approach essentially involves sharing your code with a reviewer, and receiving constructive comments following the review.
This may be an iterative process, until the reviewer is satisfied with the resulting code.

This can work best within an Agile working pattern, where changes are little and often. Requesting review of small but regular changes reduces the burden, relative to large review of a complete project.

The thought of someone else reviewing your code in this way encourages good practices from the outset:
* Clear code and documentation - so that others with no experience can use and test your code
* Usable dependency management - so that others can run your code in their own environment

This form of review is aided by features of most version control platforms, namely the Pull request (or equivalent).
See [](version_control.md) for more information.
