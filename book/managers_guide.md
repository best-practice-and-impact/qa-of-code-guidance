# Managing analytical code development

```{note}
This section is a draft, while we make sure that it meets user needs.

It would benefit from case studies that demonstrate how to decide what level of quality assurance a piece of analysis requires.

Please get in touch with feedback or case studies to support the guidance
[by creating a GitHub Issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues)
or emailing us at [emailing us](mailto:ASAP@ons.gov.uk).
```

This section of the guidance targets those who manage data analysis, science and engineering work in government
or those acting as product owners for analytical products.

It aims to help you support your team to apply the good quality assurance practices described in the wider
[Quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html).
We refer to processes that apply these good practices as a reproducible analytical pipelines (RAP).

Before applying this guidance, you should have a basic awareness of the tools and
techniques used to do quality analysis as code - the [introduction to RAP course](https://learninghub.ons.gov.uk/course/view.php?id=1236) outlines these.
You should also be aware of any specific tools and platforms that are used in your department.

[The Government Service Standard](https://www.gov.uk/service-manual/service-standard) outlines best practices for creating public services, which include analysis.
You should use this when designing and managing the development of analysis as code.


## Apply quality assurance proportional to risk

As the [the Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) notes,
the quality assurance we apply to our analysis should be proportionate to the complexity and risk that the analysis carries.

When managing analytical work, you should not need an in-depth understanding of the analysis code to trust that it is working correctly.
However, you should be confident that the team who built the analysis process has taken an appropriate approach given the user need,
and that proportionate quality assurance is being applied to the development and running of the analysis.

You should work with your team to decide which quality assurance practices are necessary given each piece of analysis.
You might find our [](checklists.md) useful templates for defining the target level of assurance.
When possible, you should define the target assurance level before starting the analysis.


```{important}

While quality assurance must be applied relative to the risk and complexity of the analysis, you must consider the skills of your team.
It will take time to learn to apply the necessary good practices, so you should support their gradual development of these skills.

[The RAP learning pathway](https://learninghub.ons.gov.uk/mod/page/view.php?id=8699) provides training in good practices.
You can use the wider [Quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html)
as a reference to apply these practices to analysis.
You should identify where each analyst is along the pathway - they should look to develop the next skill in the pathway and apply this,
rather than attempting to adopt them all at once.

Note that it is important to maintain technical skills in the analysis team for sustainability, to ensure that the analysis can be understood, updated, and maintained.
```

Despite the initial cost of developing technical skills,
[evidence shows that applying good practices increases the efficiency of code development and maintainability of the code](https://www.devops-research.com/research.html).
There are number of case studies that describe how
[good quality assurance practices have improved government analysis](https://analysisfunction.civilservice.gov.uk/support/reproducible-analytical-pipelines/rap-case-studies/).

Not following good practices creates [technical debt](https://en.wikipedia.org/wiki/Technical_debt), which slows down further development of the analysis.
This can be necessary for delivering to short deadlines, but you should set aside time to address this for continued development of the analysis.

Where quality assurance of the code doesn't meet your target level of assurance,
for example where there is limited time or skill,
then you should supplement this with more in-depth assurance of outputs.
This might include dual running the analysis with an independent system and consistency checks across the output data.

The remaining parts of this section provide questions that aim to help you assess the quality assurance practices that your team are applying in their analysis.


## Design quality analysis

These questions aim to help you assess the design decisions at the beginning of the analysis.


### Why have you chosen to do the analysis this way?

Understanding user needs ensures that the analysis is valuable.

* You should have a plan to consult users at the beginning and throughout the development process, to ensure that you meet their needs.
* The methodology and data should be suitable for the question being asked.
* More than one person should develop the analysis to allow pair programming, peer review, and mentoring. This increases the sustainability of analysis.
* You should use open-source analysis tools to carry out the analysis, wherever possible.
Your team should be able to explain why they have chosen the analysis tools and why they are confident that they are fit for purpose.


### How are you storing input data?

Versioning input data ensures that we can reproduce our analysis.

* You should version input data so that you can reproduce analysis outputs.
* You should store data in an open format (e.g. CSV or ODS), not formats that are restricted to proprietary software like SAS and Stata.
* You should store large or complex datasets in a database.
* You should monitor the quality of data, following [the government data quality framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework).


### How will you keep track of changes to the code and why they were made?

[Version control](version_control.md) of changes provides an audit trail.

* You should version control the code, documentation, and peer reviews. Git software is most commonly used for this.
* You should develop the code on an open source code platform, like GitHub. This transparency increases your users trust in the analysis and promotes collaboration and re-use.
* You should have a clear record of every change and who made it.
* Each change should be linked to a reason, for example, a new requirement or an issue in the existing code.
* You should store reviews of changes with the version of the analysis that was reviewed.


## Quality assure throughout development

These questions can be used throughout the development of the analysis,
to assess how the team are progressing towards the target quality assurance practices that you have agreed.


### How is your code structured?

[Modular code](modular_code.md) makes it easier to understand, update and reuse the code.

* You should write logic as functions, so that it can be reused consistently and tested.
* You should group related functions together in the same file, so that it is easy to find them.
* You should clearly separate logic with different responsibilities (e.g., reading data versus transforming data).
* When code can be reused for other analyses, you should store and share this as a package.


### How easy is it to adjust the way that the analysis runs?

[Configuration files](configuration.md) allow you to change the way the code runs without editing the code itself.

* You should store parameters for the code that often change between runs in separate configuration files.
* Things that often change in analysis code include input and output file paths, reference dates and model parameters.


### How is the analysis documented?

[Code documentation](code_documentation.md) is essential for business continuity and sustainability.

* You should document every function in the code, so it is clear what each function is supposed to do.
* Function documentation should include what goes in and what comes out of each function.
* Where others will run or re-used the code, documentation should include usage examples and test data.


### What are the dependencies?

[Project documentation](project_documentation.md) ensures that others can reproduce our analysis.

* You should provide user instructions for running the analysis.
* You should document software and package versions with the code.
Typically, you record package versions using `setup.py` and `requirements.txt` files (Python) or a `DESCRIPTION` file (R).
* Code should not be dependent on a specific computer to run. Running it on a colleague's system can help to check this.
* When you run the same analysis multiple times or on different systems, it should give reproducible outcomes.
* Container systems, like Docker, help to create reproducible environments to run code.


### What assumptions does the analysis make?

Transparency of our analysis increases trust.

* You should record assumptions and caveats of the analysis close to the code.
* You must communicate these to users when releasing results from the analysis.


### How has peer review been done?

[Peer review](peer_review.md) increases the quality of our analysis and transfers skills and knowledge.

* Technical colleagues should conduct internal peer reviews of each change to the code.
This will identify issues early on and makes the review process more manageable than reviewing only the final analysis.
* Peer review should follow a standard procedure, so that reviews are consistent. Reviewers should check that each change follows the agreed good practices.
* You should evidence that peer reviews are acted on and how. When issues or concerns are raised, they should be addressed before the analysis is used.
* If the product is high risk,  you should arrange and conduct external peer review.


### How have you tested the code?

[Testing](testing_code.md) assures us that the code is working correctly.

* Testing means making sure that the code produces the right outputs for realistic example input data.
* You should apply automated 'unit' testing to each function to ensure that code continues to work after future changes.
* You should test each function and the end-to-end analysis using minimal, realistic data.
* Your testing should be more extensive on the most important or complex parts of the code. However, ideally you would test every single function.
* Tests should account for realistic cases, which might include missing data, zeroes, infinities, negative numbers, wrong data types, and invalid inputs.
* Reviewers should sign-off that there is enough testing to assure that the code is working as expected.
* Each time you identify an error in the code,you should add a test to assure that the error does not reoccur.


### What happens when the analysis fails to run?

Recording and reporting errors provides an audit trail and makes it easier for users to correctly use the code.

* When code fails to run, it should provide informative error messages to describe the problem.
* If another team will operate the code, error messages should help users to correct the problem.
* Errors or warnings might also be raised when data validation is not met.
* When code is run in production, errors should be recorded or logged.


### How does the analysis result differ from the previous analysis?

Comparing analysis to previous results can help to ensure reproducibility and identify errors.

* When repeating analysis over time, you should compare results between analyses.
Large differences in the outcome of the results may indicate an issue with the analysis process.
* When developing code to replace legacy analysis, you may wish to parallel this with the new method. This will allow you to identify differences and improvements.


### How can we further improve the quality of the analysis?

Code quality improves over time, as your team learn more about good practices.

* The team should be aiming to meet the agreed assurance level, but should also consider which practices could be applied next to improve the code beyond this.
* You should review training needs in your team and allow time for continuous personal development of these practices.
