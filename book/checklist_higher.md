# Higher quality assurance

## Quality assurance checklist

Quality assurance checklist from [the quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html).

### Modular code

- Individual pieces of logic are written as functions. Classes are used if more appropriate.
- Code is grouped in themed files (modules) and is packaged for easier use.
- Main analysis scripts import and run high level functions from the package.
- Low level functions and classes carry out one specific task. As such, there is only one reason to change each function.
- Repetition in the code is minimalised. For example, by moving reusable code into functions or classes.
- Objects and functions are open for extension but closed for modification; functionality can be extended without modifying the source code.
- Subclasses retain the functionality of their parent class while adding new functionality. Parent class objects can be replaced with instances of the subclass and still work as expected.

### Good coding practices

- Names used in the code are informative and concise.
- Names used in the code are explicit, rather than implicit.
- Code logic is clear and avoids unnecessary complexity.
- Code follows a standard style, e.g. [PEP8 for Python](https://www.python.org/dev/peps/pep-0008/) and [Google](https://google.github.io/styleguide/Rguide.html) or [tidyverse](https://style.tidyverse.org/) for R.

### Project structure

- A clear, standard directory structure is used to separate input data, outputs, code and documentation.
- Packages follow a standard structure.

### Code documentation

- Comments are used to describe why code is written in a particular way, rather than describing what the code is doing.
- Comments are kept up to date, so they do not confuse the reader.
- Code is not commented out to adjust which lines of code run.
- All functions and classes are documented to describe what they do, what inputs they take and what they return.
- Python code is [documented using docstrings](https://www.python.org/dev/peps/pep-0257/). R code is [documented using `roxygen2` comments](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html).
- Human-readable (preferably HTML) documentation is generated automatically from code documentation.
- Documentation is hosted for easy access. [GitHub Pages](https://pages.github.com/) and [Read the Docs](https://readthedocs.org/) provide a free service for hosting documentation publicly.

### Project documentation

- A README file details the purpose of the project, basic installation instructions, and examples of usage.
- Where appropriate, guidance for prospective contributors is available including a code of conduct.
- If the code's users are not familiar with the code, desk instructions are provided to guide lead users through example use cases.
- The extent of analytical quality assurance conducted on the project is clearly documented.
- Assumptions in the analysis and their quality are documented next to the code that implements them. These are also made available to users.
- Copyright and licenses are specified for both documentation and code.
- Instructions for how to cite the project are given.
- Releases of the project used for reports, publications, or other outputs are versioned using a standard pattern such as [semantic versioning](https://semver.org/).
- A summary of [changes to functionality are documented in a changelog](https://keepachangelog.com/en/1.0.0/) following releases. The changelog is available to users.
- Example usage of packages and underlying functionality is documented for developers and users.
- Design certificates confirm that the design is compliant with requirements.
- If appropriate, the software is fully specified.

### Version control

- Code is [version controlled using Git](https://git-scm.com/).
- Code is committed regularly, preferably when a discrete unit of work has been completed.
- An appropriate branching strategy is defined and used throughout development.
- Code is open-sourced. Any sensitive data are omitted or replaced with dummy data.
- Committing standards are followed such as appropriate commit summary and message supplied.
- Commits are tagged at significant stages. This is used to indicate the state of code for specific releases or model versions.
- Continuous integration is applied through tools such as [GitHub Actions](https://github.com/features/actions), to ensure that each change is integrated into the workflow smoothly.

### Configuration

- Credentials and other secrets are not written in code but are configured as environment variables.
- Configuration is stored in a dedicated configuration file, separate to the code.
- If appropriate, multiple configuration files are used depending on system/local/user.
- Configuration files are version controlled separately to the analysis code, so that they can be updated independently.
- The configuration used to generate particular outputs, releases and publications is recorded.
- Example configuration file templates are provided alongside the code, but do not include real data.

### Data management

- Published outputs meet [accessibility regulations](https://analysisfunction.civilservice.gov.uk/area_of_work/accessibility/).
- All data for analysis are stored in an open format, so that specific software is not required to access them.
- Input data are stored safely and are treated as read-only.
- Input data are versioned. All changes to the data result in new versions being created, or [changes are recorded as new records](https://en.wikipedia.org/wiki/Slowly_changing_dimension).
- All input data is documented in a data register, including where they come from and their importance to the analysis.
- Outputs from your analysis are disposable and are regularly deleted and regenerated while analysis develops. Your analysis code is able to reproduce them at any time.
- Non-sensitive data are made available to users. If data are sensitive, dummy data is made available so that the code can be run by others.
- Data quality is monitored, as per [the government data quality framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework).
- Fields within input and output datasets are documented in a data dictionary.
- Large or complex data are stored in a database.
- Data are documented in an information asset register.

### Peer review

- Peer review is conducted and recorded near to the code. Merge or pull requests are used to document review, when relevant.
- Pair programming is used to review code and share knowledge.
- Users are encouraged to participate in peer review.

### Testing

- Core functionality is unit tested as code. See [`pytest` for Python](https://docs.pytest.org/en/stable/) and [`testthat` for R](https://testthat.r-lib.org/).
- Code based tests are run regularly.
- Bug fixes include implementing new unit tests to ensure that the same bug does not reoccur.
- Informal tests are recorded near to the code.
- Stakeholder or user acceptance sign-offs are recorded near to the code.
- Test are automatically run and recorded using continuous integration or git hooks.
- The whole process is tested from start to finish using one or more realistic end-to-end tests.
- Test code is clean an readable. Tests make use of fixtures and parametrisation to reduce repetition.
- Formal user acceptance testing is conducted and recorded.
- Integration tests ensure that multiple units of code work together as expected.

### Dependency management

- Required passwords, secrets and tokens are documented, but are stored outside of version control.
- Required libraries and packages are documented, including their versions.
- Working operating system environments are documented.
- Example configuration files are provided.
- Where appropriate, code runs independent of operating system (e.g. suitable management of file paths).
- Dependencies are managed separately for users, developers, and testers.
- There are as few dependencies as possible.
- Package dependencies are managed using an environment manager such as [virtualenv for Python](https://virtualenv.pypa.io/en/latest/) or [renv for R](https://rstudio.github.io/renv/articles/renv.html).
- Docker containers or virtual machine builds are available for the code execution environment and these are version controlled.

### Logging

- Misuse or failure in the code produces informative error messages.
- Code configuration is recorded when the code is run.
- Pipeline route is recorded if decisions are made in code.

### Project management

- The roles and responsibilities of team members are clearly defined.
- An issue tracker (e.g GitHub Project, Trello or Jira) is used to record development tasks.
- New issues or tasks are guided by users’ needs and stories.
- Issues templates are used to ensure proper logging of the title, description, labels and comments.
- Acceptance criteria are noted for issues and tasks. Fulfilment of acceptance criteria is recorded.
- Quality assurance standards and processes for the project are defined. These are based around [the quality assurance of code for analysis and research guidance document](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html).

## Template checklist

You can either refer to the checklist above, or use the Markdown template below to include the checklist in your project.

```{code-block} md
## Quality assurance checklist

Quality assurance checklist from [the quality assurance of code for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html).

### Modular code

- [ ] Individual pieces of logic are written as functions. Classes are used if more appropriate.
- [ ] Code is grouped in themed files (modules) and is packaged for easier use.
- [ ] Main analysis scripts import and run high level functions from the package.
- [ ] Low level functions and classes carry out one specific task. As such, there is only one reason to change each function.
- [ ] Repetition in the code is minimalised. For example, by moving reusable code into functions or classes.
- [ ] Objects and functions are open for extension but closed for modification; functionality can be extended without modifying the source code.
- [ ] Subclasses retain the functionality of their parent class while adding new functionality. Parent class objects can be replaced with instances of the subclass and still work as expected.

### Good coding practices

- [ ] Names used in the code are informative and concise.
- [ ] Names used in the code are explicit, rather than implicit.
- [ ] Code logic is clear and avoids unnecessary complexity.
- [ ] Code follows a standard style, e.g. [PEP8 for Python](https://www.python.org/dev/peps/pep-0008/) and [Google](https://google.github.io/styleguide/Rguide.html) or [tidyverse](https://style.tidyverse.org/) for R.

### Project structure

- [ ] A clear, standard directory structure is used to separate input data, outputs, code and documentation.
- [ ] Packages follow a standard structure.

### Code documentation

- [ ] Comments are used to describe why code is written in a particular way, rather than describing what the code is doing.
- [ ] Comments are kept up to date, so they do not confuse the reader.
- [ ] Code is not commented out to adjust which lines of code run.
- [ ] All functions and classes are documented to describe what they do, what inputs they take and what they return.
- [ ] Python code is [documented using docstrings](https://www.python.org/dev/peps/pep-0257/). R code is [documented using `roxygen2` comments](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html).
- [ ] Human-readable (preferably HTML) documentation is generated automatically from code documentation.
- [ ] Documentation is hosted for easy access. [GitHub Pages](https://pages.github.com/) and [Read the Docs](https://readthedocs.org/) provide a free service for hosting documentation publicly.

### Project documentation

- [ ] A README file details the purpose of the project, basic installation instructions, and examples of usage.
- [ ] Where appropriate, guidance for prospective contributors is available including a code of conduct.
- [ ] If the code's users are not familiar with the code, desk instructions are provided to guide lead users through example use cases.
- [ ] The extent of analytical quality assurance conducted on the project is clearly documented.
- [ ] Assumptions in the analysis and their quality are documented next to the code that implements them. These are also made available to users.
- [ ] Copyright and licenses are specified for both documentation and code.
- [ ] Instructions for how to cite the project are given.
- [ ] Releases of the project used for reports, publications, or other outputs are versioned using a standard pattern such as [semantic versioning](https://semver.org/).
- [ ] A summary of [changes to functionality are documented in a changelog](https://keepachangelog.com/en/1.0.0/) following releases. The changelog is available to users.
- [ ] Example usage of packages and underlying functionality is documented for developers and users.
- [ ] Design certificates confirm that the design is compliant with requirements.
- [ ] If appropriate, the software is fully specified.

### Version control

- [ ] Code is [version controlled using Git](https://git-scm.com/).
- [ ] Code is committed regularly, preferably when a discrete unit of work has been completed.
- [ ] An appropriate branching strategy is defined and used throughout development.
- [ ] Code is open-sourced. Any sensitive data are omitted or replaced with dummy data.
- [ ] Committing standards are followed such as appropriate commit summary and message supplied.
- [ ] Commits are tagged at significant stages. This is used to indicate the state of code for specific releases or model versions.
- [ ] Continuous integration is applied through tools such as [GitHub Actions](https://github.com/features/actions), to ensure that each change is integrated into the workflow smoothly.

### Configuration

- [ ] Credentials and other secrets are not written in code but are configured as environment variables.
- [ ] Configuration is stored in a dedicated configuration file, separate to the code.
- [ ] If appropriate, multiple configuration files are used depending on system/local/user.
- [ ] Configuration files are version controlled separately to the analysis code, so that they can be updated independently.
- [ ] The configuration used to generate particular outputs, releases and publications is recorded.
- [ ] Example configuration file templates are provided alongside the code, but do not include real data.

### Data management

- [ ] Published outputs meet [accessibility regulations](https://analysisfunction.civilservice.gov.uk/area_of_work/accessibility/).
- [ ] All data for analysis are stored in an open format, so that specific software is not required to access them.
- [ ] Input data are stored safely and are treated as read-only.
- [ ] Input data are versioned. All changes to the data result in new versions being created, or [changes are recorded as new records](https://en.wikipedia.org/wiki/Slowly_changing_dimension).
- [ ] All input data is documented in a data register, including where they come from and their importance to the analysis.
- [ ] Outputs from your analysis are disposable and are regularly deleted and regenerated while analysis develops. Your analysis code is able to reproduce them at any time.
- [ ] Non-sensitive data are made available to users. If data are sensitive, dummy data is made available so that the code can be run by others.
- [ ] Data quality is monitored, as per [the government data quality framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework).
- [ ] Fields within input and output datasets are documented in a data dictionary.
- [ ] Large or complex data are stored in a database.
- [ ] Data are documented in an information asset register.

### Peer review

- [ ] Peer review is conducted and recorded near to the code. Merge or pull requests are used to document review, when relevant.
- [ ] Pair programming is used to review code and share knowledge.
- [ ] Users are encouraged to participate in peer review.

### Testing

- [ ] Core functionality is unit tested as code. See [`pytest` for Python](https://docs.pytest.org/en/stable/) and [`testthat` for R](https://testthat.r-lib.org/). 
- [ ] Code based tests are run regularly.
- [ ] Bug fixes include implementing new unit tests to ensure that the same bug does not reoccur.
- [ ] Informal tests are recorded near to the code.
- [ ] Stakeholder or user acceptance sign-offs are recorded near to the code.
- [ ] Test are automatically run and recorded using continuous integration or git hooks.
- [ ] The whole process is tested from start to finish using one or more realistic end-to-end tests.
- [ ] Test code is clean an readable. Tests make use of fixtures and parametrisation to reduce repetition.
- [ ] Formal user acceptance testing is conducted and recorded.
- [ ] Integration tests ensure that multiple units of code work together as expected.

### Dependency management

- [ ] Required passwords, secrets and tokens are documented, but are stored outside of version control.
- [ ] Required libraries and packages are documented, including their versions.
- [ ] Working operating system environments are documented.
- [ ] Example configuration files are provided.
- [ ] Where appropriate, code runs independent of operating system (e.g. suitable management of file paths).
- [ ] Dependencies are managed separately for users, developers, and testers.
- [ ] There are as few dependencies as possible.
- [ ] Package dependencies are managed using an environment manager such as [virtualenv for Python](https://virtualenv.pypa.io/en/latest/) or [renv for R](https://rstudio.github.io/renv/articles/renv.html).
- [ ] Docker containers or virtual machine builds are available for the code execution environment and these are version controlled.

### Logging

- [ ] Misuse or failure in the code produces informative error messages.
- [ ] Code configuration is recorded when the code is run.
- [ ] Pipeline route is recorded if decisions are made in code.

### Project management

- [ ] The roles and responsibilities of team members are clearly defined.
- [ ] An issue tracker (e.g GitHub Project, Trello or Jira) is used to record development tasks.
- [ ] New issues or tasks are guided by users’ needs and stories.
- [ ] Issues templates are used to ensure proper logging of the title, description, labels and comments.
- [ ] Acceptance criteria are noted for issues and tasks. Fulfilment of acceptance criteria is recorded.
- [ ] Quality assurance standards and processes for the project are defined. These are based around [the quality assurance of code for analysis and research guidance document](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html).
```
