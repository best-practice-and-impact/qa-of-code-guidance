# Glossary of terms

```{note}
This section is a draft, while we make sure that it meets user needs.

Please get in touch with feedback [by creating a GitHub Issue](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues) or [emailing us](mailto:ASAP@ons.gov.uk).
```

## Terms
### Abstraction

Treating a problem as an idea or concept, rather than a detailed individual example.

Abstraction is used to manage the complexity of software, by describing our logic in a more generic way or by hiding complexity.
When we use similar logic in multiple parts of our code, we can abstract this logic into a generic function or method to be reused.
When part of our process is very complex, but is self-contained, we can hide this complexity it by putting it inside a function and referring to the function.


### Application Programming Interface (API)

An interface that defines how you can interact with software through code.
For example, the functions or methods from a package that a typical user will interact with.


### Attribute

A variable associated with a class object.


### Automated testing

Tests that are written in code, to check that other code works as expected.
Test are like a controlled experience, to check that our code produces the expected outcome.
Tests can check code multiple levels, for example, checking that an individual function works or checking that a pipeline runs from end to end.


### Code interpreter

A computer program that runs code in a particular programming language.
For example, the program that reads your Python or R analysis code and runs it.
A non-interactive interpreter runs code in order, which is important for reproducibility.

Interactive interpreters allow you to run individual lines of code, which means that you can run code  out of order.
Notebooks use interactive interpreters.
These are not suitable for running analysis pipelines, because they do not ensure that the code is run reproducibly.


### Class

Contains code to create instances of objects and methods to edit these instances of classes and their attributes. Methods may also produce output other than the class instance.

Examples of built in python classes are float, string, and bool.

Examples of built in R classes are double, character, and logical.


### Cloud computing

Cloud computing allows us to access scalable computing power and data storage on-demand.
This means that we can access high-specification hardware or store large amounts of data, usually only paying for what we have used.

The most common cloud platforms are Google Cloud Platform (GCP), Amazon Web Service (AWS) and Microsoft Azure.


### Code

The part of software that contains program instructions.
In analysis, code is a set of human-readable instructions that tell a computer how to carry out our analysis.


### Code repository

A folder for storing the code and associated documents for a piece of software.
These are often associated with Git, as the folder that is being version controlled.
Also known as a 'repo'.


### Configuration file

Files that are used to configure the parameters or settings of a program.
In analysis, these often include paths to input data files and other information that may change between each run of the pipeline.


### Continuous integration and continuous delivery (CI/CD)

CI/CD tools help to automate parts of your code development workflow.
This can include running automated tests against your code and deploying the latest version of your code into production.
GitHub Actions is an example tool for running CI/CD workflows.

Continuous integration describes regularly combining code changes from multiple contributors on a single software project.
Integrating these changes regularly helps to check that independent changes work correctly together.
Continous delivery describes automation of the software release process.
Automating both of these using a CI/CD tool increases the efficiency of building software and getting it into production.


### Debugger

A computer program that is used to test software and to identify the root cause of errors or "bugs".
Debuggers allow you to pause the code at specific points and to walk through code step by step, in order to understand how it is working.


### Dependencies

Something that is required for your code to run correctly - your code depends upon it.
This includes your operating system, environment, software and packages (and their versions), if these are needed to reproducibly run your analysis code.
Dependencies are usually documented alongside code, so that others can prepare an environment to run the code.


### Documentation

Human readable text that describes your analysis and code.
There are many ways to document code.
Low level documentation might describe a single function, a code comment might describe a decision you made when writing the code,
and high level documentation might describe your overall approach to a piece of analysis.


### Dual Running

In a RAP context, where a pipeline or process is run in different ways, on different systems, or by different people to verify reproducibility.


### Functions and methods

Functions and methods are named units of logic that can be used multiple times in our code.
Methods are similar to functions, but are associated with a class.
Functions and methods are crucial for creating modular code.

Functions are written to generalise a piece of logic, so that it can be used consistently in multiple places in our code.
You might define a function for a particular statistical method, validation check or to manipulate data in a certain way.


### Git

By far the most popular version control tool.
Used to version changes to code for any programming language.


### Instance

When an object is created by a constructor of a class, the resulting object is called an instance of the class. The variables specific to an object are called instance variables.


### Integrated development environment (IDE)

An IDE is a tool that facilitates software development for a given programming language.
An IDE will usually consist of a code editor, debugger and development automation tools like a text auto-complete.


### Interative Running

Where a script is run as expressions with immediate feedback given, such as in a terminal or command line.


### Logging

Automatically recording information when your analysis runs.
This might include what options were used when configuring the pipeline and any decisions that the code made when running.
Recording this information can help you to reproduce previous runs of the analysis and to identify the source of errors.


### Maintainability

Ability to easily understand, modify and repair the code.


### Modularity

Modular code is written in discrete, re-usable chunks.
Similar code is kept close together, while pieces of code with different uses are stored separately.
Breaking code down in this way makes code easier to work with, understand and review.


### Module

A module is a script grouping related functions and/or classes that are reused across larger programs. It may also include statements used to initialise the module when it is imported in another script. 


### Notebooks

Notebooks are documents that contain text, executable code, and the output of that code.
Notebooks are used to share the results of exploratory analysis.
However, because parts of a notebook can be run out of order they are not suitable for production of published outputs.


### Object-oriented programming (OOP)

Writing code that defines and uses classes.
Classes are objects that contain both data (attributes) and logic (methods).
Classes are often used to represent a real life entity - for example a bank account, which stores a balance and has method for withdrawing money.


### Open source

A type of software license that allows users to view the software's code.
Open-source code is openly available to anyone.
Using open-source software and publishing our code with open-source licenses ensures that our users can easily understand and reproduce our analysis.

Open-source programming languages are free to use.
We recommend using Python and R, which support the good practices outlined in this guidance.

Proprietary software, including SPSS, SAS, and Stata are closed source.
These are expensive to use and do not support many of the good analysis practices outlined in this guidance.
Not using open source analysis tools means that your users need to purchase software to reproduce your results.


### Packages

Packages are file structures that contain code and documentation.
These collections of code are designed for you to install and re-use them with ease.
Packages in Python and R act as extensions, to allow us to reuse code that has already been written.

"Library" is similarly used to describe a software collection, however, packages are more specifically for distribution of code.


### Parameters and arguments

Parameters are the variables that a piece of code expects to be provided when it is used.
They act as placeholders, to allow us to make code more generic.
A function might have parameters to allow it to be run on different inputs.
For example, there may be a parameter to allow the user to select which column of data a piece of logic should use.

An argument is the value that is being passed to a given parameter.


### Peer review

Having another developer review changes that you have made to code.
This helps to assure that your code is readable and follows a sensible approach.
It also helps to transfer understanding of the code between members of the team.


### Pipeline

A orchestrated chain of programs that will execute the next program(s) in the chain when a program completes successfully. Outputs will be stored on completion of a program and will feed in as inputs to the next program(s) in the chain.


### Procedural Running

Where a script is executed as statements that run one after the other.


### Program

A main script that can contain statements, functions, and methods. The main script may import functions and methods from other scripts. This is the script that would be run by the user/orchestration tool.


### Python and R

Python and R are high-level programming languages that are commonly used in government analysis.
They are both free to use and open source.


### Readability

Ability to gain an understanding of code within a reasonable amount of time.


### Reproducible Analytical Pipelines (RAP)

Reproducible Analytical Pipelines (RAP) are analyses that are carried out following good software engineering practices that are described by this guidance.
They focus on the use of open-source analytical tools and a variety of techniques to deliver reproducible, auditable, and assured data analyses.
RAP is more generally a culture of wanting to improve the quality of our analysis, by improving the quality assurance of our analysis code.


### Scripts

A script is a single file containing code. Code in scripts can be run interactively or procedurally.


### Variables

A variable is a named code object for storing data within a programming language.


### Version control

Saving versions of documents to keep an audit trails of changes.
Version control tools typically allow you to backtrack to previous versions and to merge multiple concurrent changes from different users.


### Version control platforms

For example, GitHub, GitLab and BitBucket.

These services use Git to manage remote repositories.
Having a remote version of your repository allows multiple users to collaborate using Git.
Each platform has free and paid options and allow users to open-source their work.

Some platforms (e.g. GitLab) are open source and can be hosted internally by your organisation.


### Virtual environment

Virtual environments are tools for managing dependencies and isolating projects.
A virtual environment is effectively a folder tree containing the programming language version and a list of dependencies.
This helps keep track of dependencies and avoid conflicts between different projects.

