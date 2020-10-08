# Data

In order to reproduce a piece of analysis we need to be able to identify and access the data that our analysis used and produced.
This requires suitable storage of the data, with any relevant documentation.
And versioning of the data where it may change over time.


## Data storage

It is assumed that most data are now stored digitally.

Digital data risk becoming inaccessible as technology develops and commonly used software changes.
Long term data storage should use open or standard file formats.
There are [recommended formats](https://www.ukdataservice.ac.uk/manage-data/format/recommended-formats.aspx) for storing different data types, though we suggest avoiding formats that depend on proprietary software like SPSS and SAS.

Short term storage, for use in analysis, might use any format that is suitable for the analysis task.
However, most analysis tools should support reading data directly from safe long term storage, including databases.

When publishing or sharing tabular data, you should follow the [GOV.UK Tabular data standard](https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard).

Guidance from the UK Data Service describes [data security considerations](https://www.ukdataservice.ac.uk/manage-data/store/security).


### Spreadsheets

Spreadsheets (e.g. Microsoft Excel formats) are a very general data analysis tool.
The cost of their easy to use interface and flexibility is a complete lack of quality assurance.

Spreadsheets are not suitable for storage of data (or statistics production and modelling processes).
Issues when using spreadsheets for data storage include:
* Lack of audibility - changes to data are not recorded.
* Multiple users can't work with a single spreadsheet file at once.
* They are error prone and have no built in quality assurance.
* Files become cumbersome when they are large.
* Automatic "correction" of grammar and data type, which silently corrupts your data.
  * Converting dates to a different datetime format.
  * Converting numbers to dates.
  * Converting text to dates (e.g. [gene names that are converted to dates](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)).


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
You might find this [foundations of SQL (GSS only course)](https://learninghub.ons.gov.uk/enrol/index.php?id=529) or [w3schools SQL tutorials](https://www.w3schools.com/sql/default.asp) useful for learning the basics of SQL.

Common analysis tools can interface with databases using SQL packages, or those which provide an object-relational mapping (ORM).
An ORM is non-SQL-based interface to connect to a database.
They are often user-friendly, but may not support all of the functionality that SQL offers.
This guide covers [Python SQL libraries](https://realpython.com/python-sql-libraries/) in detail.
While this Software Carpentry course covers [SQL databases and R](http://datacarpentry.org/R-ecology-lesson/05-r-and-databases.html).

Other database concepts:
* Schema - a blueprint that describes the field names and types for a table, including any other rules (constraints).
* Query - a SQL command that creates, reads, updates or deletes data from a database.
* View - a virtual table that provides a quick way to look at part of your database, defined by a stored query.
* Indexes - data structures that can increase the speed of particular queries.

Good practices when working with databases:
* Use auto-generated primary keys, rather than composites of multiple fields.
* Break your data into logical chunks (tables), to reduce redundancy in each table.
* Lock tables that should not be modified.

Other resources:
* This [SQL lecture from Harvard's computer science course](https://www.youtube.com/watch?v=u5pDdEKnbKA) may be a useful introduction to working with databases from Python.
* A guide to [using the `sqldf` R package](https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/sql.html).


## Documenting data

```{todo}
Add content for documenting and versioning data
```


## Data versioning



