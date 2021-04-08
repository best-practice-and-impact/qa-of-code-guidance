# Managers guide

This section is aimed at those who manage analysts in government or act as product owners for analytical code.

Analytical managers should not need an in-depth understanding of the code produced by their team. However, they should be able to asses whether adequate quality assurance is being applied to the development of the analysis.

For a better understanding of the tools that your team use for analysis, you might look at the [Awareness of Coding Tools](https://learninghub.ons.gov.uk/enrol/index.php?id=530) course on th GSS Learning Hub.

## Questions around quality assurance

We recommend that you ask your team the following questions to understand the quality assurance that is being applied in their analysis. Good quality assurance should be applied throughout an analysis project, therefore, it is important that the areas outlined below are reviewed regularly.

The practices outlined below should be applied proportionately to the business risk and complexity of the project. You should aim to establish what adequate quality assurance looks like at the beginning of a project. These questions can then be used throughout the project to assess whether this goal is being met.

### Why have your chosen to do things this way?

* The methodology and data should be suitable for the question being asked.
* The analysis tools that your team use should have some rationale for being chosen.
* Users should be consulted throughout the development process.
* The program should be maintainable if it will be re-used.


### What happens when the analysis fails to run?

* When code fails to run, it should provide informative error messages to describe the problem.
* Errors or warnings might also be raised when data validation is not met.

### How easy is it to adjust the way that the analysis runs?

* Configuration of the code that might change should be easily identified from the code.
* Ideally separate configuration files are used to store these options.

### How are you storing input data?

* Input data should be versioned, so that analysis outputs can be reproduced.
* Data should be stored in an open format (e.g. CSV and ODS), not formats that are restricted to proprietary software like SAS and Stata. 
* Large or complex datasets should be stored in a database.

### How have you specified the analysis?

* The code should have an accompanying specification.
* The specification should show how data are transferred from function to function.
* The specification helps reviewers to understand the code. Well-specified code is easier to understand and maintain.

### What does the documentation look like?

* Every function should be documented.
* Function documentation should say what goes in and what comes out of each function.
* Documentation should be easy to read, accessible, and stored closely to the code.
* Good documentation includes usage examples and test data.

### How has peer review been done?

* Skilled colleagues should conduct internal peer reviews of the code.
* If the product is high risk an external peer review should also be conducted.
* Peer review should follow a standard procedure.

### How have you kept track of who made changes and for which reasons?

* The code, documentation, and peer review should all be version controlled. Git software is most commonly used for this.
* There should be a clear record of every change and who made it.
* Each change should have a reason.
* Reviews should be stored with the version of the analysis that was reviewed.

### How have you tested the code?

* Testing means making sure that the code produces the right outputs for realistic example input data.
* Good testing is automated 'unit' testing.
* Each function and the end-to-end analysis should be tested using minimal, realistic data.

### What have you tested?

* Aim for every single function being tested
* Tests should account for edge cases like missing data, zeroes, infinities, negative numbers, wrong data types, and invalid inputs.
* Reviewers should sign-off that there is enough testing.

### What are the dependencies?

* Dependencies include anything the code needs to run, including software and package versions.
* It can be difficult to run code on other systems when dependencies are not documented.
* Documenting dependencies allows others to reproduce the analysis more easily.

### Which other systems have you run this on?

* Code should not be dependent on a specific computer to run. Running it on a colleague's system can help to check this. 
* Container systems, like Docker, help to create reproducible environments to run code.
### How would we do a dual run?

* For the highest risk analysis, the program should be written twice separately or with different tools.
* Where possible, outputs should be compared between the runs for a variety of realistic inputs. 
