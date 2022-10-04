# Managing analytical code development

This section is aimed at those who manage data analysis/science/engineering work in government or those acting as product owners for analytical products.

Learning from previous projects, we've found that moving from traditional analysis approaches to developing analysis as code requires: 
* Intention to transform and improve the quality of the wider business process around the project, not just automating an existing process. 
* Committed, skilled resource for the duration of the project and for ongoing maintenance for the life span of the product. 
* Motivation for the project and personal development from those working on the project. 
* Having appropriate tools available for the development and deployment of the project. 
* A plan for requirement collection and transitioning the product into business as usual. 

It is common for this kind of transformation to identify quality issues in the current process. This should be seen as an opportunity to improve the quality of the process.

[The Government Service Standard](https://www.gov.uk/service-manual/service-standard) outlines best practices for creating public services, which includes analysis. You should use this when designing and managing the development of analysis.

The rest of this page describes the benefits of doing analysis as code and aims to help you ensure that your team are applying the good quality assurance practices outlined in the wider [Quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html). Code that applies these good practices are refered to as reproducible analytical pipelines (RAP).

Analysis team managers should not need an in-depth understanding of the code produced by their team. However, they should be able to asses whether adequate quality assurance is being applied to the development of the analysis.

## Analysis as code is beneficial

Carrying out analysis as code has many benefits:
* Reproducible, quality analysis.
* Greater efficiency and timeliness, through automation.
* Transparent analysis and quality assurance, increasing trust.
* Improved business continuity and knowledge management.

Automating a process using code is not sufficient to achieve all of the benefits, without also applying adequate quality assurance.

## Analytical code requires quality assurance

We recommend that you ask your team the following questions to understand the quality assurance that is being applied in their analysis. Good quality assurance should be applied throughout an analysis project, therefore, it is important that the areas outlined below are reviewed regularly.

The practices outlined below should be applied proportionately to the business risk and complexity of the project. Analytical code that doesn't apply quality assurance carries similar risk to other analysis appraoches. Your team should aim to outline what adequate quality assurance looks like early on in a project. These questions can then be used throughout the project to assess whether this target is being met, or whether the team are moving towards this goal.

### Why have your chosen to do things this way?

* The methodology and data should be suitable for the question being asked.
* Your team should be using open-source analysis tools, with a reason for each given tool being chosen.
* Users should be consulted throughout the development process, to ensure that their need is being met.

### How is your code structured?

* Logic should be written as functions, so that it can be reused consistently and tested.
* Related functions should be grouped together in the same file, so that it is easy to find them.

### How easy is it to adjust the way that the analysis runs?

* Parts of the code that may change should be stored in separate configuration files, so that they can be changed without changing the code.
* Things that often change in analysis code include input and output file paths, reference dates and model parameters.

### How are you storing input data?

* Input data should be versioned, so that analysis outputs can be reproduced.
* Data should be stored in an open format (e.g. CSV or ODS), not formats that are restricted to proprietary software like SAS and Stata. 
* Large or complex datasets should be stored in a database.

### What does the documentation look like?

* Every function should be documented in the code, so that it is clear what the function is supposed to do.
* Function documentation should also include what goes in and what comes out of each function.
* Where code will be run or re-used by others, documentation should include usage examples and test data.

### How has peer review been done?

* Technical colleagues should conduct internal peer reviews of the code.
* Peer review of individual changes to the code will help to identify issues sooner. This is also more manageable than reviewing the complete final analysis.
* If the product is high risk, an external peer review should also be conducted.
* Peer review should follow a standard procedure, so that reviews are consistent.

### How have you kept track of who made changes to the code and why?

* The code, documentation, and peer reviews should all be version controlled. Git software is most commonly used for this.
* There should be a clear record of every change and who made it.
* Each change should be linked to a reason, for example, a new requirement or an issue in the existing code.
* Reviews should be stored with the version of the analysis that was reviewed.

### How have you tested the code?

* Testing means making sure that the code produces the right outputs for realistic example input data.
* Automated 'unit' testing should be applied to each function, to ensure that code continues to work after future changes to the code.
* Each function and the end-to-end analysis should be tested using minimal, realistic data.

### What have you tested?

* Testing should be more extensive on the most important or complex parts of the code. However, ideally every single function should be tested.
* Tests should account for realistic cases, which might include missing data, zeroes, infinities, negative numbers, wrong data types, and invalid inputs.
* Reviewers should sign-off that there is enough testing to assure that the code is working as expected.

### What are the dependencies?

* Documenting the code dependencies allows others to reproduce the analysis more easily.
* Dependencies include anything the code needs to run, including software and package versions.

### What happens when the analysis fails to run?

* When code fails to run, it should provide informative error messages to describe the problem.
* If another team will operate the code, error messages should help users to correct the problem.
* Errors or warnings might also be raised when data validation is not met.

### How can we further improve the quality of the code?

* Code quality should improve over time, as your team learn more about good practices. They should consider which practices could be applied next to improve the code.
* You should review training needs in your team and allow time for continous personal development of these practices.

### Which other systems have you run this on?

* Code should not be dependent on a specific computer to run. Running it on a colleague's system can help to check this.
* Container systems, like Docker, help to create reproducible environments to run code.

### How would we do a dual run?

* For the highest risk analysis, the results of your analysis should be compared from two independent calculations (i.e. one from another tool or software).
* Where possible, outputs should be compared between analysis using a variety of realistic inputs.
* You may also wish to parallel run new analysis processes with a legacy approach, to quantify changes or improvements to the analysis.

# Other resources

For a better understanding of the tools that your team use for analysis, you might look at the [Awareness of Coding Tools](https://learninghub.ons.gov.uk/enrol/index.php?id=530) course on the GSS Learning Hub.