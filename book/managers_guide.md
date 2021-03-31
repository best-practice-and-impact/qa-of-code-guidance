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
* Users can be consulted throughout the development process.
* The program should be maintainable if it will be re-used.

### How have you specified the analysis?

The package should have an accompanying specification. The specification should show how data are transferred from function to function. The specification helps reviewers to understand the code. Well-specified packages are easier to maintain.

### What does the documentation look like?

Every function should be documented. Function documentation should say what goes in and what comes out. Documentation should be easy to read, accessible, and part of the package. Good documentation should include examples and test data.

### How has peer review been done?

Skilled colleagues should conduct internal peer reviews of the code. If the product is high risk an external peer review should be conducted. Peer review should follow a standard procedure like the Best Practice and Impact example.

### How have you kept track of who made changes and for which reasons?

The code, the documentation, and the peer review should all be version controlled. There should be a clear record of every change and who made it. Each change should have a reason. Reviews should be stored with the version they reviewed.

### How have you tested the code?

Testing means making sure that the code produces the right outputs for realistic example input data. Good testing is automated 'unit' testing. Combinations of functions, and the entire analysis, should also be tested on small but difficult data.

### What have you tested?

Aim for every single function being tested. Tests should account for edge cases like missing data, zeroes, infinities, negative numbers, wrong data types, and invalid inputs. Reviewers should sign-off that there is enough testing.

### Which other systems have you run this on?

It can be difficult to make sure your code runs where it is needed. Container systems, like Docker, help this to happen. In the absence of this it’s best to start by just trying to open it on a colleague’s system.

### What are the dependencies?

Dependencies include anything your package needs to run, including software and package versions. It can be difficult to run code on other systems when dependencies are not documented. Documenting dependencies allows others to reproduce analysis more easily.

### How would we do a dual run?

For the highest risk analysis, the program should be written twice separately or with different tools. Where possible, outputs should be compared between the runs for a variety of realistic inputs. 
