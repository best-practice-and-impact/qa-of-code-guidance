# Managing analytical code development

This section of the guidance is aimed at those who manage data analysis/science/engineering work in government or those acting as product owners for analytical products.

It aims to help you support your team to apply the good quality assurance practices described in the wider [Quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html). Proccesses that appliy these good practices are referred to as a reproducible analytical pipelines (RAP).

Before applying this guidance, you should have a basic awareness of the tools and techniques used to do quality analysis as code - the [introduction to RAP course](https://learninghub.ons.gov.uk/course/view.php?name=intro_to_RAP) outlines these. You should also be aware of any specific tools and platforms that are used in your department.

[The Government Service Standard](https://www.gov.uk/service-manual/service-standard) outlines best practices for creating public services, which includes analysis. You should use this when designing and managing the development of analysis as code.


## Quality assurance is proportional to risk

As described by [the Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government), the quality assurance of our analysis should be proportional to the complexity and risk of the analysis.

When managing analytical work, you should not need an in-depth understanding of the analysis code to trust that it is working correclty. However, you should be confident that the approach the team has taken is appropriate given the user need, and that proportionate quality assurance is being applied to the development and running of the analysis.

You should work with your team to decide on which quality assurance practices are necessary given each piece of analysis. You might find our [](version_control.md) useful templates for defining the target level of assurance. When possible, you should define the target assurance level before starting the analysis.

```{important} Developing good practice skills

While quality assurance must be applied relative to the risk and complexity of the analysis, you must consider the skills of your team. It will take time to learn to apply the necessary good practices, so you should support their gradual development of these skills.

[The RAP learning pathway](https://learninghub.ons.gov.uk/course/view.php?name=intro_to_RAP) provides training in good practices. Then the wider [Quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html) can be used as a reference to apply these to your analysis. You should identify where each analyst is along the pathway - they should look to develop the next skill in the pathway and apply this, rather than attempting to adopt them all at once.

Where quality assurance of the code doesn't meet your target level of assurance, for example where there is limited time or skill, then it is necessary to supplement this with  in-depth assurance of analysis outputs. This might include dual running the analysis with an independent system and consistency checks across the output data.
```

## Analysis as code is beneficial

Carrying out analysis as code has many benefits:
* Reproducible, quality analysis.
* Greater efficiency and timeliness, through automation.
* Transparent analysis and quality assurance, increasing trust.
* Improved business continuity and knowledge management.

Automating a process using code is not sufficient to achieve all of these benefits, without also applying adequate quality assurance.

Learning from previous projects, we've found that moving to doing analysis as code is most successful when there is: 
* intention to transform and improve the quality of the wider business process around the project, not just automating an existing process. 
* committed, skilled resource for the duration of the project and for ongoing maintenance for the life span of the product. 
* motivation for the project and personal development from those working on the project. 
* access to appropriate tools for the development and deployment of the project. 
* a plan for collecting requirements and for transitioning the product into business as usual. 

It is common for transformation of existing processes to identify quality issues in the current process. This should be seen as an opportunity to improve the quality of the process.

## Analytical code requires quality assurance

We recommend that you ask your team the following questions to understand the quality assurance that is being applied in their analysis. Good quality assurance should be applied throughout an analysis project, therefore, it is important that the areas outlined below are reviewed regularly.

The practices outlined below should be applied proportionately to the business risk and complexity of the project. Analytical code that doesn't apply quality assurance carries similar risk to other analysis appraoches. Your team should aim to outline what adequate quality assurance looks like early on in a project. These questions can then be used throughout the project to assess whether this target is being met, or whether the team are moving towards this goal.

### Why have your chosen to do things this way?

* The methodology and data should be suitable for the question being asked.
* Your team should be using open-source analysis tools. They should be able to explain why they have chosen these tools and why they are confident that they are fit for purpose.
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
* There should be evidence that peer reviews are acted on. When issues or concerns are raised, they should be addressed before the analysis is used.

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

* For high risk parts of the analysis, the results of this part of the analysis should be compared from two independent calculations (i.e. one from another tool or software).
* Where possible, outputs should be compared between analysis using a variety of realistic inputs.
* You may also wish to parallel run new analysis processes with a legacy approach, to quantify changes or improvements to the analysis.