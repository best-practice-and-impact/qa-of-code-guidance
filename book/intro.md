# Quality assurance of code for analysis and research

This Government Analysis Function (AF) guidance, also known as the Duck Book,
is produced by the Analysis Standards and Pipelines hub of the [Office for National Statistics](https://www.ons.gov.uk).

This guidance is a living document, which is continually updated.
We are extremely grateful for any feedback that you are able to provide on existing and future content.


## How to get the most out of the book

This guidance describes software engineering good practices that are tailored to those working with data using code.
It is designed for those who would like to quality assure their code and increase the reproducibility of their analyses.
Software that apply these practices are referred to as reproducible analytical pipelines (RAP).

This guidance is relevant if you are:

- writing code to automate part of your work and would like to assure that it is working as expected
- developing statistical or data engineering pipelines and would like to assure that they are sustainable and reproducible
- developing models and would like to assure that they are transparent and reproducible
- developing data science techniques and would like your code to be useful to others
- looking for a high level introduction to software engineering practices in the context of analysis and research

The good practices outlined in the book are general to many applications of programming, so may also be relevant for those outside of government.

The [RAP learning pathway](https://learninghub.ons.gov.uk/mod/page/view.php?id=8699) provides training for many of these good practices.
This book can be used to guide your learning and as a reference when applying these practices in your work.
Each chapter describes the risks that each practice may help to address.
As recommended by [the Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government),
you should strive to apply the most appropriate quality assurance practices given the risks associated with your work.

The principles in this book are language agnostic.
The book does not aim to form a comprehensive learning resource and you may often need to study further resources to implement these practices.
That said, examples and useful references are provided for **Python** and **R**, as open source languages that are commonly applied across government.


## About us

The Analysis Standards and Pipelines hub supports government analysis by providing guidance, consultancy and training.

You can find us on:

- Our websites: [Government Analysis Function](https://www.gov.uk/government/organisations/government-analysis-function)
- Email: [Analysis Standards and Pipelines hub](mailto:ASAP@ons.gov.uk)
- Slack: [Government Data Science](https://govdatascience.slack.com)
- Twitter: [Government Analysis Function](https://twitter.com/gov_analysis) and [UK GSS](https://twitter.com/ukgss)


## Citing the book

The book uses an Open Government Licence which can be read on the National Archives website:
[National Archives](https://nationalarchives.gov.uk/doc/open-government-licence/version/3/)

In summary, you are free to use, adapt and distribute the information in this book with citation but not imply endorsement,
and that the information is provided 'as is' without warranty.

The following structure can be used to reference the current version of the book:

> UK Government Analytical Community. (2020). Quality assurance of code for analysis and research (version 2023.2).
> Office for National Statistics, Analytical Standards and Pipelines hub:
> [https://best-practice-and-impact.github.io/qa-of-code-guidance/](https://best-practice-and-impact.github.io/qa-of-code-guidance/)


## Accessibility statement

This accessibility statement applies to the Quality assurance of code for analysis and research guidance.
Please note that this does not include third-party content that is referenced from this guidance.

The website is managed by the Quality and Improvement division of the Office for National Statistics.
We would like this guidance to be accessible for as many people as possible.
This means that you should be able to:

- change colours, contrast levels and fonts
- zoom in up to 300% without the text spilling off the screen
- navigate most of the website using just a keyboard
- navigate most of the website using speech recognition software
- listen to most of the website using a screen reader (including the most recent versions of JAWS, NVDA and VoiceOver)

For keyboard navigation, {kbd}`Up Arrow` and {kbd}`Down Arrow`keys can be used to scroll up and down on the current page.
{kbd}`Left Arrow` and {kbd}`Right Arrow` keys can be used to move forwards and backwards through the pages of the book.
Tabbed content (including code example) can be focused using the {kbd}`Tab` key.
{kbd}`Left Arrow` and {kbd}`Right Arrow` keys are then used to focus the required tab option,
where {kbd}`Enter` can be used to select that option and display the associated content.


### Help us improve this book

We’re always looking to improve the accessibility of our guidance.
If you find any problems not listed on this page or think that we’re not meeting accessibility requirements, please contact us by emailing [ASAP@ons.gov.uk](mailto:ASAP@ons.gov.uk).
Please also get in touch if you are unable to access any part of this guidance, or require the content in a different format.

We will consider your request and aim to get back to you within five working days.


### Enforcement procedure

The Equality and Human Rights Commission (EHRC) is responsible for enforcing the
[Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018 (the ‘accessibility regulations’)](https://www.legislation.gov.uk/uksi/2018/952/made).
If you’re not happy with how we respond to your complaint, you should [contact the Equality Advisory and Support Service (EASS)](https://www.equalityadvisoryservice.com/).
