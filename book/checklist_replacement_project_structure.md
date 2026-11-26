# Project structure

For Python and R projects, quality assurance (QA) should ask whether the structure helps someone understand, run, check and maintain the work. A familiar layout is useful, but the presence of files or tools is not evidence that they work. Apply these questions in proportion to the project’s complexity and risk.

## Can someone find their way around?

Are reusable code, tests, settings, documentation and outputs easy to distinguish? Do names explain their purpose? Is there a clear starting point and a visible route from inputs to results? Avoid unnecessary folders and duplicated logic.

## Can a new user understand the project?

The README should pass the two-minute test: a new reader should be able to find answers to these questions within two minutes.

- **What?** What does this project do?
- **Why?** Why should I use it?
- **How?** How do I install and run it?
- **Example?** What is the smallest working example?
- **Support?** Where do I get help?

## Does the structure suit the project?

If the project is a package, does it follow Python or R packaging conventions? Can it be built, installed and checked using only the documented setup instructions?

## Can the work be recreated?

Are language versions, required packages and setup steps recorded? Could someone recreate the required environment and run the project without undocumented files, installed packages or saved objects?

## Can important behaviour be checked?

Is reusable logic separated from the code that launches the workflow? Can it be tested without running everything? Are important calculations, data transformations and failure cases checked automatically, using small, non-sensitive examples?

## Are settings, data and sharing controlled?

Are changeable settings kept separate from the code and easy to find, for example in a top-level `config.yaml`? Are passwords and access keys kept out of version control? Are restricted data, local environments and temporary files excluded from version control, and are licensing and sharing permissions clear?

## Practical check

Can someone unfamiliar with the project follow the README, run the smallest example and execute the tests?

## Further guidance

- [Python packaging](https://packaging.python.org/)
- [R Packages](https://r-pkgs.org/)
- [renv](https://rstudio.github.io/renv/)
- [govcookiecutter-lite](https://github.com/best-practice-and-impact/govcookiecutter-lite)
