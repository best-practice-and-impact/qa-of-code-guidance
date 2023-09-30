# Modular code

The principles outlined in this chapter represent good practices for general programming and software development.
These have been tailored to a more analytical workflow.

```{admonition} Pre-requisites
:class: admonition-learning

To get the most benefit from this section, you should have an understanding of core programming concepts such as:

* storing information in variables
* using control flow, such as if-statements and for-loops
* writing code as functions or classes
* using functions or classes in your code

You can find links to relevant training in the [](learning.md) section of the book.
```


## Motivation

Code that is repetitive, disorganised or overly complex can be difficult to understand, even for experienced programmers.
This makes assuring, testing or changing the code more burdersome.
It also makes it harder to spot and fix mistakes.

Code that isn't modular can cause a range of issues:

- walls of repetitive code that is hard to absorb
- long, complex scripts that are hard to follow
- over-complicated code where a simpler solution could be used
- a code base that makes it difficult to find what you're looking for

This chapter highlights ways to write modular code that is easier to read, review and maintain.
These practices will also help you implement the other good coding practices you will come across in this book, such as version control, review, testing and documentation.
Because of this, modular code is fundamental to making analysis more reproducible, auditable and assured.


(modular)=
## Modular code

Breaking your code down into smaller, more manageable chunks is a sensible way to improve readability.
Regardless of the language, there are often techniques to containerise your code into self-contained parts such as modules, classes or functions.


(functions)=
### Write re-usable code as functions

In the early stages of analysis we often copy and paste code to 'make it work'. As this work matures, it is worth taking repetitive code and turning it into functions.
Functions allow us to make a  piece of logic reusable in a consistent and readable way, and also makes it easier for us to [test our logic](testing_code.md).

When starting to write functions, you should consider what is the right level of complexity for a single function.
Namely, can the code containing my logic be turned into a concise and readable function as it is, without having to pass too many arguments to the resulting function?
If not, it might be better to break the code into multiple smaller functions and
then use these smaller functions to build up a larger high-level function that performs the group of actions that you need.
These smaller functions might also be used in other places in your code. For example, in other high-level functions that perform similar tasks.

This approach helps you break complex logic down into small, understandable chunks that can be documented and tested more easily.

When writing functions, it's also important to consider how they interact with other parts of your code.
As a general rule of thumb, your code should run in the same way if a call to your function was replaced by the value that it would have returned.
This is called 'referential transparency'.

In practice, this means that your functions should not depend on or affect variables that have not been explicitly fed into them as arguments.
For instance, a function should not add columns to a data table that has not been passed as an input to the function.
Nor should the action of a function be affected by anything other than arguments that are passed to it.
For example, running your function twice with the same inputs should always produce the same results.

Avoiding such behaviours makes your code more transparent;
it will be easier for users and developers to understand which functions affect which data without being concerned about hidden behaviours.
In turn, this makes it easier to locate bugs in the code and assure its function by peer review.

When it is not possible or practical to follow these practices, you should ensure that any 'side-effects' are adequately documented for both users and developers.
This may be the case where your code interacts with a file, database or an external service.
Ultimately, if you do signal where these kind of things might happen, someone trying to debug issues will know where to look.

To summarise:

- Make sure that functions are not overcomplicated;
break down your code into smaller functions and build up your functionality with larger functions from these small building blocks.
- Minimise the 'side-effects' of functions in order to make sure that your code is easy to debug and is transparent in its functionality.
- Strive to make sure that running your function with the same inputs will produce the same results every time.


### Group data and methods as classes

Classes are fundamental parts of [object-orientated programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming).
They create an association between data (attributes of the class) and logic (methods of the class).
As you will see in the examples below, classes can be useful when representing real objects in our code.

Although classes exist in R, [writing custom classes](https://adv-r.hadley.nz/oo.html) is less common than it is in Python (and other OOP enabling languages).
Because of this, the following sub-section will focus primarily on Python classes.

With a more complex system, OOP can help to reduce complexity by hiding low-level details from users, such as an internal state.

```{note}
The 'state' of an object is usually a set of variables that are particular to a given instance of a class.
To illustrate, imagine a bank account that is represented by an `Account` class.
You can have many instances of this class (many unique bank accounts), each defined by the following internal state:

- owner name
- account number
- balance
```

Since the end user does not need to know all of the state associated with an object, when writing classes consider marking such state as 'private'.
This prevents users from accessing attributes directly, instead accessing them through class methods (functions defined with the class).

````{admonition} Method vs Function
When talking about methods, we mean functions that are strictly 'attached' to a given class.
The following example illustrates the difference between the two:

```python
# Defining a class with a diagnose method
class Car:
    """A car class"""
    wheels = 4
    def __init__(self, brand):
        self.brand = brand

    def diagnose(self):
        ...

# versus defining a standalone diagnosis function
def diagnose(car, ...):
    """A car diagnosis function"""
    ...


# Calling a method on a class instance that holds it's own state
cadillac = Car(brand="Cadillac")
cadillac.diagnose()

# Calling a function by passing all relevant information explicitly
# Note: for the sake of variety the information about the car is represented in a dictionary
diagnose({"brand":"Cadillac", "wheels":4})
```

````

In some languages 'private' state can be used to prevent access to parts of your class.
In Python [truly private instance variables do not exist](https://docs.python.org/3/tutorial/classes.html#private-variables),
so it is not possible to prevent access to any part of your class.
The standard convention in Python is to prefix attribute names with a single underscore (`_my_class_attribute`)
to indicate that users shouldn't be concerned with these attributes.

In addition to private attributes, you can use the same naming convention to indicate that a method is 'private' and should not be used by users.
This can be useful when writing reusable low-level methods within an object, analogous to breaking a large function down into multiple smaller functions.
These private methods can then be called by high-level methods that are exposed to users.

```{caution}
In Python, the notion of 'private' does not mean secure.
The main goal of private attributes and methods is to expose less unnecessary information to the anyone using your class in their code.
```

```python
class BankAccount:
    def __init__(self, balance, credentials):
        self._balance = balance
        self._credentials = credentials

    def _private_withdraw(self, amount):
        """Private withdrawal helper method."""
        self._balance -= amount

    def _check_credentials(self, credentials):
        """Private check helper method."""
        if credentials == self._credentials:
            return True
        else:
            return False

    def withdraw(self, credentials, amount):
        """Public withdrawal method."""
        if _check_credentials(credentials):
            self._private_withdraw(amount)
```

When using classes in our code, we care more about what methods a class provides than what `type` it is defined as.
This is known as 'duck typing'; if a class has the same methods as another class, then you can use either class in your code.

> If it walks like a duck, and it quacks like a duck, then it must be a duck.

Given the example above, if we created a class `LoyaltyAccount` with the same `withdraw` method for withdrawing points,
we could feasible switch between using the `BankAccount` and `LoyaltyAccount` classes without affecting how our code runs.

Object-Orientated Programming introduces the concept of inheritance - where a class can 'inherit' methods from another class in order to extend it.
In this situation, a new class 'subclasses' the 'superclass' or 'parent' that it is inheriting from.
When defining multiple classes with similar functionality, inheritance can be used to store the shared logic in a separate class type,
which we can then extend by subclassing.
For example, we might create an `Account` class to store a `balance` and the logic behind our `withdraw` method.
Our `BankAccount` and `LoyaltyAccount` could then subclass `Account` to extend it with any additional logic that is specific to their account types.

```{note}
[Liskov substitution](https://en.wikipedia.org/wiki/Liskov_substitution_principle) states that
subclasses should not damage the functionality of their parent class in their implementation.
They should extend their usefulness, but retain their original functionality.
If our `BankAccount` class inherits from `Account` we should consider that 'a `BankAccount` is an `Account`'.
Liskov substitution strengthens this statement to '`BankAccount` is interchangeable with an `Account`';
we can replace any `Account` with `BankAccount` without changing how our code runs.
This is because `BankAccount` provides all of the same methods that an `Account` does, no less.

This can be similarly applied to functions.
If you were to increase the domain and range of a function, to account for new cases, then this function should observe the same interface as the previous function.

In short:

- Objects should be replaceable with instances of their subclasses, without altering the correctness of that program.
- Functions should be replaceable with similar functions that share the same interface.
```

However, we should be wary that inheritance locks our class in to the object that it inherits from.
If the superclass changes, our class is forced to change with it.
When using inheritance to reuse code from an unrelated class, 'encapsulation' may be more appropriate.
For example, a `Car` class might want to use a method from an `Engine` class, but a car could not be substituted for an engine.
It would not be suitable for `Car` to inherit from `Engine`.
Therefore, you might keep a private instance of the `Engine` class you wish to re-use, and delegate the work down to it in the `Car` methods.
Then, if you change your mind about using this `Engine` class in your `Car` class, you aren't tied to it and can easily replace it.

(interfaces)=
In OOP, an 'interface' can be defined to act as a blueprint or specification for writing classes.
An interface outlines the attributes and methods that a class must provide to be considered equivalent to a group of classes.
Perhaps we want to use classes to read and write data - this might require several different classes, with `read` and `write` methods for different file formats.
For example, one class could deal with storing data in a database, and another could store data in local `.csv` files instead.
In our code, we could switch which class is provided to downstream functions.
Our functions don't need to know if they are reading or writing from databases or `.csv` files,
however, they do require the `read` and `write` methods of the class to work in a standard way.
An `interface` would help to define the standard for interacting with this group of classes.

In Python, the `abc` module allows us to define ['abstract' base classes and methods](https://docs.python.org/3/library/abc.html)
to enforce that our classes provide the required methods.
When a subclass does not implement the required abstract methods, instances of the class cannot be created.
These abstract base classes achieve the same as interfaces in other object-based languages.
We can illustrate this concept in the following example:

```python
from abc import ABC, abstractmethod

class FileHandler(ABC):
    """An abstract class for reading and writing"""
    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def read(self, query):
        pass

class CsvHandler(FileHandler):
    ...
    def write(self, data):
       return write_to_file(data, self.filename)

    def read(self, query):
       data = read_csv(self.filename)
       data = parse(data)
       data = process(query, data)
       return data

class SqlHandler(FileHandler):
    ...
    def write(self, data):
       connect_to_database(self.connection_url)
       return write_to_database(data)

    def read(self, query):
       data = read_from_database(self.connection_url)
       data = process(query, data)
       return data
```

When multiple classes have a similar application programming interface (API, i.e. the methods they supply for users), we can easily switch between them.
A good real-world example of this can be seen in the `scikit-learn` package, where the different linear model types are represented by different classes.
Each linear model class supports a common set of methods, e.g. `fit()` and `predict()`.
As such, any model can then be used in a pipeline and swapped out with minimal effort.
Therefore, when thinking about how to break you code up into classes consider the use of standardised methods across similar objects to make them interchangeable.


(class-responsibilities)=

```{note}
A word of caution, when creating your own classes.
It is easy to start to mapping nouns in system descriptions to classes, and any adjectives applied to the nouns as methods.
For example: 'the model loads the data', which implies that `Model` is a class that should have a `load_data` method.
This works well for small systems, but as the complexity of your code grows you might find that one of your classes gains the majority of the underlying logic.
This often leads to one class with many methods, while other classes just store data with very few methods.
This can be described as 'Data Driven Design'.

When most of your code resides in a single class, this can indicate that this class is responsible for too much of your code's logic.
This class might become overly complex and hence difficult to maintain.
Consequently, changes to requirements will cause this one class to change, which may affect other unrelated functionality in the class.

For more complex analytical work, a better approach might be [Responsibility Driven Design](https://en.wikipedia.org/wiki/Responsibility-driven_design).
Here, we write small classes with a focussed responsibility.
This reduces complexity and helps classes to avoid being affected by changes to other, unrelated parts of our code.
However, be aware of the trade-off between the complexity of one large class versus many smaller classes.
```

[Responsibility Driven Design](https://en.wikipedia.org/wiki/Responsibility-driven_design) makes objects that are usually 'passive' become 'active'.
For example, with a banking system, an  object representing a bank account, and handling all money movements, might become overly complex.
Instead, objects representing `Cheques` and `Cash` might be designed with payment methods.
In this situation, a `Cheque` knows how much money it contains and how to pay itself into an account.
A `Cheque`'s responsibility is to retrieve money from its associated account and pay itself in to another bank account.
If we later needed to add new payment methods, the existing payment type classes (`Cheque` and `Cash`) will unlikely to be affected.
The bank account's responsibility is holding money, receiving it and paying it out.

```{tip}
Many [Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern) are available with OOP.
These are reusable solutions to common problems.
```

Finally, be wary when using classes to 'chain' methods together.
For instance, if a 'book' has a 'publisher' and the publisher has an 'address', you could write `book.publisher().address().postcode()`.
However, chains like this are fragile as they depend on multiple parts of the system not changing.
The 'Demeter' research project found that this style of code produce a high proportion of bugs,
resulting in the [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter): 'Only talk to your immediate friends'.
Namely, only access the objects you know about directly within a class.
This reduces the opportunity for your code to be damaged by a change in your dependencies.
There is a penalty for this - you replace with `book.publisherPostcode()` which internally would call `publisher.postcode()`,
so we've added a method to `publisher` as well as `book`; we're trading maintainability for complexity, so consider if it is worthwhile.

To summarise:

- Classes hide implementation detail from users, enabling implementation to be changed without affecting users.
- Look to use consistent methods in a group of related classes, so that you can switch between them without affecting the code using it.
Consider Python 'duck typing' or abstract classes and methods.
- Avoid storing all logic in a single class. Instead, distribute logic based on responsibilities.
- Be aware of trading maintainability for complexity - one large class or too many classes can be hard to understand.
- Design Patterns have solutions to many common problems and are a useful toolbox.
- Prefer encapsulation over inheritance, especially with code reuse.


### Split complex code into multiple scripts

Scripts are simply files containing code that you would like to execute.
In Python you commonly have a `main.py` script that orchestrates part of your codebase to achieve an outcome.
In machine-learning projects, you sometimes have `train.py` and `test.py`, which are scripts that train the model and produce performance metrics.

Scripts, if written well, are reproducible.
In languages like R and Python, when executed from the command line using commands like `python main.py` or `Rscript main.R`
they are read top to bottom and executed line by line.
This is in contrast to running code in an interactive interpreter or notebook, where the human has control of the order of execution.
Manually executing individual lines of code allows for a slew of errors when things are run in the wrong order.

Ultimately for code pipelines you will need to have some way of running your code - the humble script is
the primary way of orchestrating your functions and classes in a pipeline fashion.

<!-- The first sentence of the note below doesn't make sense to me. -->

```{note}
Using a script does not guarantee that your code will run reproducibly, but it does ensure that code is run in the same fashion across multiple runs.
```

To summarise:

- Scripts are a good way to orchestrate your functions and classes in order to build a simple, yet effective pipeline.
- They are text documents containing source code, which makes them easily human readable and auditable.
- They can be broken down into sections using [comments](code_documentation.md) for readability.


(modules)=
### Organise related classes and functions into modules

Simply put, modules are scripts that contain functions that you want to use in other scripts.
As you write your code and find opportunities to create classes or functions that reduce repetition and promote easier code comprehension,
you might decide that you want these functions to sit outside of your main pipeline script.
This is where modules come in, to separate reusable code into logical groups.

Consider a project where an analyst has created one large data analysis script.
Upon reflection, they decide to split the logic from their pipeline into groups of functions relating to 'data processing', 'data modelling' and 'result presentation'.
They then create a file to contain each of these groups of functions: `processing.py`, `modelling.py` and `reporting.py`.
They decide that they want to have a pipeline script called `main`, but they want to keep this script readable and simple.
In R, it's best to also use an R project file.
Working within a project allows you to use relative file paths and avoid the need to refer to specific script locations.
Their directory now looks something similar to:

`````{tabs}

```` {tab} Python
```
project
├── main.py 
├── modelling.py 
├── processing.py 
├── reporting.py 
├── README.md 
```
````

```` {tab} R
```
project 
├── main.R 
├── modelling.R 
├── processing.R 
├── reporting.R 
├── README.md
└── project.Rproj 
```
````
`````

````{warning}
R projects are a really useful and simple way to organise your projects better.
However, be sure to check your settings.
R projects save history and data by default.
This is not a good idea if you're using git, as it means data can easily make its way into the version history.
To disable these options in RStudio, open the project options menu in the tools tab.
In the menu, set the options "save workspace to .RDATA on exit" and "Always save history" to "No".
Alternatively, you can edit the .Rproj file in an editor of your choice by adding these settings:

```
SaveWorkspace: No
AlwaysSaveHistory: No
```
````

They then import the relevant functions into the main script from their modules as follows:

````{tabs}
```{code-tab} py
import pandas as pd

from modelling import predict_results
from processing import clean, preprocess
from reporting import generate_report, export

data = pd.read_csv("data/path.csv")
data = preprocess(clean(data))
results = predict_results(data)
report = generate_report(results)
export(report)
```

```{code-tab} r R
# These relative file paths only work while working within an R project
source("modelling.R")
source("processing.R")
source("reporting.R")

data <- read.csv("data/path.csv")
data <- preprocess(clean(data))
results <- predict_results(data)
report <- generate_report(results)
export(report)
```
````

```{note}
This is a minimal example of a pipeline script, illustrating how you might import reusable functions from other modules.
These main scripts lack the ability to configure things like the path to the input data.
This requires users to manually alter file paths in the code, which is highly discouraged.
```

``````{admonition} A step further
Another step that can be taken to improve clarity is to further wrap these modules into their own folder like so:

`````{tabs}
````{tab} Python
```
project
├── library
│   ├── __init__.py
│   ├── modelling.py
│   ├── processing.py
│   └── reporting.py
├── LICENSE
├── main.py
└── README.md
```
````

```` {tab} R
```
project
├──R
│   ├── modelling.R
│   ├── processing.R
│   └── reporting.R
├── LICENSE
├── main.R
├── README.md
└── project.Rproj
```
````
`````
``````


(packages)=
### Organise and document your modules as packages

Programming languages often come with quite a few in-built functions and classes that are available to the end-users.
However, when it comes to solving specialised problems, these in-built functions are often not enough.
In these cases, you may need to build functionality to address a given problem from scratch.
If the solutions you build are useful and reusable, you can then wrap them up in a package to allow other users to install it.
They can then reuse the work you have put in within their own code to solve similar problems.

In short, packages are self-contained collections of code written by someone else to solve a particular problem.
For example, packages like `dplyr` and `pandas` are essential when performing data wrangling in R and Python, respectively.
They contain a myriad of functions that allows us to avoid rewriting this functionality from scratch every time.
Inside these packages is a set of [modules](modules) containing relevant functions, classes and other code that someone has written.
These are wrapped up into a package structure so that the programming language you use can understand, install and make available the code for you to import.

```{note}
This section will not cover the practices required to package and distribute your code as a package.
However if you would like to know more please look to the [code documentation section](code_documentation.md)
and seek out the packaging guides for your programming language.
```

It is useful to keep in mind the question:
is my code solving a problem that someone else has not already solved in my programming language?
If the answer is 'Yes' then perhaps it is worth considering wrapping up your code and distributing it wider.

```{note}
Packaging code properly will involve applying many of the recommendations from this book.

You will have to consider how to test, document and lay out your code for it to be usable and packagable.
In the end, high quality packages are the cornerstone of open-source package ecosystems.
However, it is not trivial to maintain and develop well-regarded open-source packages.

If you feel like you are writing code that you might consider turning into a package,
consult this book and strive to apply as many of the recommendations as you go.
This will make the final polishing and packaging much simpler, and will produce packages that are easier for third-parties to trust and use.
```


### Think carefully about whether notebooks are a suitable way to organise your code

Jupyter and other code Notebooks allow you to include live code alongside text and visualisation.
Although individual notebooks could seem like a good way to modularise your analysis for distribution, for larger projects this is not usually the best idea.

Notebooks are inherently difficult to review and audit through version control software like `git`.
Simple text files like scripts can be version controlled easily as you can see which lines of text change from one version to another.
Notebooks store their internal workings in a much more complicated format,
so seeing the changes as differences line by line is not possible in common version control tools.

Furthermore, defining and keeping functions within notebooks is prohibitive to testing.
It is not simple to test individual cells of a notebook with standard external tooling.

Lastly, one of the key issues with notebooks when they are used as methods for running a pipeline is the ability to run cells out of order.
In practice this means that a user can accidentally execute the steps of the analysis in the wrong order causing issues and different results.
As such, notebook results may not always be reproducible.

That said, great strengths of notebooks include their flexibility in displaying results while you are exploring data,
and their ability to present final research code alongside a narrative.
Therefore the top 2 reasons to use notebooks in the project lifecycle is to:

- explore and 'play' with the data while developing your methods.
- turn notebooks into HTML reports to present results to end users.

In short, notebooks are not suitable for modularising analysis pipelines, however, they are a great way to do research analytics and to present results.
Therefore, as the exploratory part of your analysis draws to a close, or there is a need to produce similar analysis more regularly, it is wise to refactor notebooks.
Reusable functions and classes can be moved to modules and the main analysis pipeline might instead be reproducibly run from a script.
Here are a few suggestions to consider when refactoring code from notebooks:

- Review the repetitive cells and assess which of them can be turned into reusable functions.
- Extract existing functions into related groups, as modules.
- Document, test and improve these functions and modules following the guidance laid out in this book.
- Import the required functionality from these new modules into the notebook or pipeline script.
- For new analysis, reuse functionality from these modules in new notebooks and continue to document your analytical thinking alongside your code in these notebooks.

After this, you might turn existing notebooks into HTML to send them stakeholders, or save them as is so that analytical peers can re-run and review your notebooks.
The steps that you've taken to simplify your notebook code will make your code much easier to understand by readers.

Bear in mind that notebook files can still be run out of order by other analysts, and that they should not be used as the main method of actually generating outputs.
Output generation should instead be trusted to scripts, where human decisions do not alter the order that code is run.
