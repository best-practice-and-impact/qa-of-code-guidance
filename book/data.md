# Data Management

Data management covers a broad range of disciplines, including organising, storing and maintaining data.
This management is typically handled by dedicated data architects and engineers, however, we appreciate that analysts are often expected to manage their own data.
This section aims to highlight good data management practices, so that you can either appreciate how your organisation handles its data or implement your own data management solutions.

In order to reproduce a piece of analysis we need to be able to identify and access the same data that our analysis used.
This requires suitable storage of data, with documentation and versioning of the data where it may change over time.


```{admonition} Key strategies
:class: admonition-strategies

[The Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework) focuses primarily on assessing and improving the quality of input data. It should be a primary resource for all analysts working with data in the public sector.
```

## Data storage

It is assumed that most data are now stored digitally.

Digital data risk becoming inaccessible as technology develops and commonly used software changes.
Long term data storage should use open or standard file formats.
There are [recommended formats](https://www.ukdataservice.ac.uk/manage-data/format/recommended-formats.aspx) for storing different data types, though we suggest avoiding formats that depend on proprietary software like SPSS, STATA and SAS.

Short term storage, for use in analysis, might use any format that is suitable for the analysis task.
However, most analysis tools should support reading data directly from safe long term storage, including databases.


### Spreadsheets

Spreadsheets (e.g. Microsoft Excel formats and open equivalents) are a very general data analysis tool.
The cost of their easy to use interface and flexibility is increased difficulty of quality assurance.

```{figure} https://assets.amuniversal.com/7f343ac0870a01332a13005056a9545d
---
width: 75%
name: spreadsheets-comic
alt: A comic strip joking that it doesn't matter if a spreadsheet if wrong, "as long as it gives me the answer I want".
---
Does it matter if the spreadsheet is wrong, from [Dilbert by Scott Adams](https://dilbert.com/strip/2016-01-07)
```

Spreadsheets are not suitable for storage of data (or statistics production and modelling processes).
Issues when using spreadsheets for data storage include:
* Lack of audibility - changes to data are not recorded.
* Multiple users can't work with a single spreadsheet file at once.
* They are error prone and have no built in quality assurance.
* Files become cumbersome when they are large.
* Automatic "correction" of grammar and data type, which silently corrupts your data.
  * Converting dates to a different datetime format.
  * Converting numbers or text that resemble dates to dates.

See the European Spreadsheet Risks Interest Group document [spreadsheet related errors and their consequences](http://www.eusprig.org/horror-stories.htm) for more information.


### Databases

Databases are collections of related data, which can be easily accessed and managed.
Each database contains one or more tables, which hold data.
Database creation and management is carried out using a database management system (DBMS).
These usually support authorisation of access to the database and support multiple users accessing the database concurrently.
Popular open source DBMS include:
* SQLite
* MySQL
* PostgreSQL
* Redis

The most common form of database is a relational database.
Data in the tables of a relational database are linked by common keys (e.g. unique identifiers).
This allows you to store data with minimal duplication within a table, but quickly collect related data when required.
Relational DBMS are called RDBMS.

Most DBMS use structured query language (SQL) to communicate with databases.

```{admonition} Key Learning
:class: admonition-learning

You might find this [foundations of SQL (government analysts only course)](https://learninghub.ons.gov.uk/enrol/index.php?id=529) or [w3schools SQL tutorials](https://www.w3schools.com/sql/default.asp) useful for learning the basics of SQL.
```

Common analysis tools can interface with databases using SQL packages, or those which provide an object-relational mapping (ORM).
An ORM is non-SQL-based interface to connect to a database.
They are often user-friendly, but may not support all of the functionality that SQL offers.

```{admonition} Key Learning
:class: admonition-learning

This guide covers [Python SQL libraries](https://realpython.com/python-sql-libraries/) in detail.
While this Software Carpentry course covers [SQL databases and R](http://datacarpentry.org/R-ecology-lesson/05-r-and-databases.html).
```

Other database concepts:
* Schema - a blueprint that describes the field names and types for a table, including any other rules (constraints).
* Query - a SQL command that creates, reads, updates or deletes data from a database.
* View - a virtual table that provides a quick way to look at part of your database, defined by a stored query.
* Indexes - data structures that can increase the speed of particular queries.

Good practices when working with databases include:
* Use auto-generated primary keys, rather than composites of multiple fields.
* Break your data into logical chunks (tables), to reduce redundancy in each table.
* Lock tables that should not be modified.

Other resources:
* This [SQL lecture from Harvard's computer science course](https://www.youtube.com/watch?v=u5pDdEKnbKA) may be a useful introduction to working with databases from Python.
* A guide to [using the `sqldf` R package](https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/sql.html).


## Documenting data

Without documentation, it is difficult to understand and work with a new dataset.

For our analysis, we should be able to quickly grasp:
* What data are available to us?
* How were these data collected or generated?
* How are these data represented?
* Have these data been validated or manipulated?
* How am I ethically and legally permitted to use the data?

This information should be created by data providers and analysts, in the form of documentation.


### Data dictionary

A data dictionary describes the contents and format of a dataset.

For variables in tabular datasets, you might document:
* a short description of what each variable represents
* the frame of reference of the data
* variable labels, if categorical
* valid values or ranges, if numerical
* representation of missing data
* reference to the question, if survey data
* reference to any related variables in the dataset
* if derived, detail how variables were obtained or calculated
* any rules for use or processing of the data, set by the data owner

See this detailed example - the [National Workforce Data Set](https://www.datadictionary.nhs.uk/data_sets/administrative_data_sets/national_workforce_data_set.html#dataset_national_workforce_data_set), from the NHS Data Model and Dictionary.

Please see [UK Data Service guidance on documenting other data](https://www.ukdataservice.ac.uk/manage-data/document/data-level/tabular.aspx), including qualitative data.


### Information Asset Register (IAR)

An information asset register (IAR) documents the information assets within your organisation.
Your department should have an IAR in place, to document its information assets.
As an analyst, you might use the register to identify contacts for data required for your analyses.

This form of documentation may not contain detailed information on how to use each data source (provided by data dictionaries), but an IAR does increase visibility of data flows.
An IAR may include:
* the owner of each dataset
* a high level description of the dataset
* the reason that your organisation holds the dataset
* how the information is stored and secured
* the risk of information being lost or compromised

GOV.UK provides [IAR templates](https://www.gov.uk/government/publications/information-asset-register) that your department might use to structure their IAR.


## Data versioning

A key requirement for reproducing your analysis is the ability to identify the data that you used.
Data change over time;
Open data and other secondary data may be revised over time or cease to be available with no notice.
The owners of these data can't always be relied on to provide historical versions of their data.

As an analyst, it is your responsibility to ensure that the exact data that you have used can be identified.

Whether using a primary or secondary data source, you should version and document all changes to the data that you use.
Documentation for data versions should include the reason why the version has changed.
For example, if an open data source has been recollected, revisions have been made to existing data, or part of the data has been removed.

You should be able to generate your analytical outputs reproducibly and, as such, treat them as disposable.
If this is not the case, you should also version outputs so that they can be easily linked to the versioned input data and analysis code.

To automate the versioning of data, you might use the Python package [DVC, which provides Git-like version control of data](https://dvc.org/).
This tool can also relate the data version to the version of analysis code, further facilitating reproducibility.
Git can be used to version data, but you should be mindful of where your remote repository stores this data.
The [`daff` package summarises changes in tabular data files](https://github.com/paulfitz/daff), which can be integrated with Git to investigate changes to data.

You might alternatively version your data manually.
For example, by creating new database tables or files for each new version of the data.
It must be possible to recreated previous versions of the data, for reproducibility.
As such, it is important that data file versions are named uniquely, for example, using incrementing numbers and/or date of collection.
Additionally, file versions must not be modified after they have been used for analysis - they should be treated as read-only.
All modifications to the data should result in new versions.

```{todo}
Diagram of good manual data versioning workflow.

[#22](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/22)
```

Finally, for this to be effective, your analysis should record the version of data used to generate a specified set of outputs.
This might be documented in analysis reports or automatically logged by your code.


## Releasing data

```{todo}
Open Linked Data ratings

Use CSVW when possible

[#23](https://github.com/best-practice-and-impact/qa-of-code-guidance/issues/23)
```


Other guidance addresses:
* [Releasing statistics in spreadsheets](https://gss.civilservice.gov.uk/policy-store/releasing-statistics-in-spreadsheets/)
* [Quality assurance of administrative data](https://osr.statisticsauthority.gov.uk/guidance/administrative-data-and-official-statistics/)
* [Data linking methods](https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods)
* When publishing or sharing tabular data, you should follow the [GOV.UK Tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).

Analysts producing published statistics may also be interested in [Connected Open Government Statistics (COGS)](https://gss.civilservice.gov.uk/guidance/the-gss-data-project/).

Guidance from the UK Data Service describes [data security considerations](https://www.ukdataservice.ac.uk/manage-data/store/security).
