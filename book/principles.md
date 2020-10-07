# Principles

When we do analysis it must be fit for purpose.
If it isn't, we risk misinforming decisions.
Bad analysis can result in harm or misallocation of public funds.
As such, we must take the right steps to ensure high quality analysis.

This book recognises three founding principles of good analysis, each supported by the one before it.
Analysis in programming makes each of these principles easier to fulfil in most cases.


```{figure} ./_static/repro_stack.png
---
width: 50%
name: repro_stack
---
Founding principles of good analysis
```

Reproducibility guarantees that we have done what we are claiming to have done, and that users could do it to get the same result.
Auditability means that we know why we chose our analysis, and who is responsible for each part of it - including assurance.
Assurance improves the average quality and includes the communication of that quality to users.


## Reproducible

Reproducibility is the only thing that you can guarantee in your analysis.
It is the first pillar of good analysis.
If you can't prove that you can run the same analysis, with the same data, and obtain the same results then you are not adding valuable analysis.
The secondary assurances of peer review, rigorous testing, and validity are secondary to being able to reproduce any analysis that you produce in a proportionate amount of time.

```{figure} ./_static/reproducibility_matrix.jpg
---
width: 60%
name: reproducibility_matrix
---
Defining reproducibility, from [The Turing Way](https://the-turing-way.netlify.app/reproducible-research/overview/overview-definitions.html)
```


Reproducible analysis relies on a transparent production process, so that anyone can follow your steps and understand your results.
This transparency eases reuse of our methods and results. 
Easy reproducibility helps your colleagues test and validate what we have done.
When reproducibility is guaranteed, users and colleagues can focus on verifying that the implementation is correct and that the research is useful for its intended purpose.

Reproducibility relies on effective documentation.
Good documentation should show how our methodology and our implementation map to each other.
Good documentation should allow users and other researchers to reuse and adapt our analysis.

Reproducible analysis supports the requirements of the [Code of Practice for Statistics](https://www.statisticsauthority.gov.uk/code-of-practice/) around quality assurance and transparency (auditability).
Wherever possible, we share the code we used to produce our outputs, along with enough data to allow for proper testing.


## Auditable

If decisions are made, based on our analysis, then we must make sure that the story of that analysis is available.
Our analysis and the evidence that we provide must be available for scrutiny and audit.
Auditable analysis is about being able to, at any point, answer: 

> Who made each decision?
> When was this decision made?
> What evidence was this decision made on?

Answering these questions gives decision makers and users greater trust in our work.
They know the story of our analysis and why we made certain analytical choices.
They know who is responsible for each part of the analysis, including the assurance.
They know exactly what changes have been made at any point.

In a reproducible workflow, we must bring together the code and the data that we used to generate our results.
These are ideally published alongside our reports, with a record of analytical choices made and the responsible owners of those choices.
The transparency that this gives our work helps to increase trustworthiness.
More eyes examining our work can point out challenges or flaws that can help us to improve.
We can be fully open about the decisions we made when we generated our outputs, so that other analysts can follow what we did and re-create them.
By making our analysis reproducible, we make it easier for others to quality assure, assess and critique.


## Assured

Good quality analysis requires good quality assurance (QA).
If decisions are being made based on analysis then this analysis must be held to high standards.
This is true for analysis carried out using any medium, including code.

However, some of the analysis that we do in government doesn't bear on decisions at that level.
We don't want to overburden analysts with QA procedures when they are not required.
In government we advocate *proportionality* - the right quality assurance procedures for the right analysis.
Analysis can be proportionately assured through peer review and defensive design.

We advocate following your department's guidance on what proportionate quality assurance looks like.
Most departments derive their guidance from the [Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government).
Assurance is best demonstrated through peer review.
Peer reviewers must be able to understand your analytical choices and be able to reproduce your conclusions.
In particularly high risk analysis, dual running should be considered.

Guarantees of quality assurance should be published alongside any report, or be taken into consideration by decision makers.


## Reproducible analytical pipelines

Producing analysis, such as official statistics, can be time-consuming and painstaking.
We need to make sure that our outputs are both accurate and timely.
We aim to develop effective and efficient analytical workflows that are repeatable and sustainable over time.
These workflows should follow the principles of reproducible analysis. 
We call these [Reproducible Analytical Pipelines (RAP)](https://dataingovernment.blog.gov.uk/2017/03/27/reproducible-analytical-pipeline/).

Reproducible analysis is still not widely practised across government.
Many analysts use proprietary (paid-for) analytical tools like SAS or SPSS in combination with programs like Excel, Word or Acrobat to create statistical products. 
The processes for creating statistics in this way are usually manual or semi-manual.
Colleagues then typically repeat parts of the process manually to quality assure the outputs.

This way of working is time consuming and can be frustrating, especially where the manual steps are difficult to replicate quickly. 
These processes are also prone to error, because the input data and the outputs are not connected directly, only through the analyst’s manual intervention.

In a recent case, manual data transfer and use of legacy analytical tools lead to [gross under-reporting of COVID-19 statistics](https://www.bbc.co.uk/news/technology-54423988).
It is essential that we use appropriate, up-to-date tools for analysis.

More recently, the tools and techniques available to analysts have evolved. 
Open-source tools like Python and R have become available.
Coupled with version control and software management platforms like git and git services have made it possible to develop automatic, streamlined processes, accompanied by a full audit trail.

RAP was first piloted in the Government Statistical Service in 2017 by analysts in the Department for Digital, Culture, Media & Sport (DCMS) and the Department for Education (DfE). 
They collaborated with data scientists from the Government Digital Service (GDS) to automate the production of statistical bulletins.

To support the adoption of RAP across government, there is a network of [RAP champions](https://gss.civilservice.gov.uk/about-us/champion-networks/reproducible-analytical-pipeline-rap-champions/). 
These champions are responsible for promoting reproducible analysis through the use of reproducible analytical pipelines, and supporting others who want to develop RAP in their own departments.


## Further reading

Various government guidance has been developed to help you when developing analysis.
We recommend:
1. The [Aqua book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) to understand guidance around assurance.
2. The [GSS Quality Strategy](https://gss.civilservice.gov.uk/policy-store/government-statistical-service-gss-quality-strategy/) when thinking about the quality of statistics.
3. The [DCMS Data Ethics Framework](https://www.gov.uk/government/publications/data-ethics-framework/data-ethics-framework) when approaching any analysis.
4. The [Communicating quality, uncertainty and change guidance](https://gss.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/) whenever you must develop user-facing products.

Each of these pieces of guidance advocate reproducibility as a core tenet of quality analysis.