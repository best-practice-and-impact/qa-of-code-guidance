# Core programming practices

The principles outlined in this chapter represent good practices for general programming and software development. These have been tailored to a more analytical workflow.

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

```{epigraph}
Code is read more often than it is written.

-- Guido van Rossum (creator of Python)
```

When writing code, we should expect that at some point someone else will need to understand, use and adapt it. This might be yourself in six months time. As such, it is important to empathise with these potential users and write code that is tidy, understandable and does not add unnecessary complexity.

Common barriers to writing readable code include: 
* documentation that is hard to understand or absent
* walls of repetitive code that is hard to absorb
* over-complicated code where a simpler solution could be used

Avoiding these issues is essential to make sure that your analysis is reproducible, auditable and assured. Therefore it is our professional responsibility to avoid putting such barriers in place whenever possible.

This chapter highlights good coding practices that will improve the readability and maintainability of your code. Here, readability refers to how easily another analyst can gain a decent understand of how your code works, within a reasonable amount of time. Maintainability refers to how easily other analysts can understand your code well enough to modify and repair it.

(modular)=
## Modular code

Breaking your code down into smaller, more manageable chunks is a sensible way to improve readability. Regardless of the language, there are often techniques to containerise your code into self-contained parts such as modules, classes or functions.

### Functions

In the early stages of analysis we often copy and paste code to 'make it work'. As this work matures, it is worth taking repetitive code and turning it into functions. Functions allow us to make a  piece of logic reusable in a consistent and readable way, and also makes it easier for us to [test our logic](testing_code.md).

When starting to write functions, you should consider what is the right level of complexity for a single function. Namely, can the code containing my logic be turned into a concise and readable function as it is, without having to pass too many arguments to the resulting function? If not, it might be better to break the code into multiple smaller functions and then use these smaller functions to build up a larger high-level function that performs the group of actions that you need. These smaller functions might also be used in other places in your code. For example, in other high-level functions that perform similar tasks.

This approach helps you break complex logic down into small, understandable chunks that can be documented and tested more easily.

When writing functions, it's also important to consider how they interact with other parts of your code. As a general rule of thumb, your code should run in the same way if a call to your function was replaced by the value that it would have returned. This is called 'referential transparency'.

In practice, this means that your functions should not depend on or affect variables that have not been explicitly fed into them as arguments. For instance, a function should not add columns to a data table that has not been passed as an input to the function. Nor should the action of a function be affected by anything other than arguments that are passed to it. For example, running your function twice with the same inputs should always produce the same results.

Avoiding such behaviours makes your code more transparent; it will be easier for users and developers to understand which functions affect which data without being concerned about hidden behaviours.
In turn, this makes it easier to locate bugs in the code and assure its function by peer review.

When it is not possible or practical to follow these practices, you should ensure that any 'side-effects' are adequately documented for both users and developers. This may be the case where your code interacts with a file, database or an external service. Ultimately, if you do signal where these kind of things might happen, someone trying to debug issues will know where to look.

To summarise:

- Make sure that functions are not overcomplicated; break down your code into smaller functions and build up your functionality with larger functions from these small building blocks.
- Minimise the 'side-effects' of functions in order to make sure that your code is easy to debug and is transparent in its functionality.
- Strive to make sure that running your function with the same inputs will produce the same results every time.

### Classes

Classes are fundamental parts of [object-orientated programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming). They create an association between data (attributes of the class) and logic (methods of the class). As you will see in the examples below, classes can be useful when representing real objects in our code.

Although classes do exist in R, they are more widely used in Python (and other OOP enabling languages). Hence the following sub-section will focus primarily on Python classes.

With a more complex system, OOP can help to reduce complexity by hiding low-level details from users, such as an internal state.

```{note}
The 'state' of an object is usually a set of variables that are particular to a given instance of a class. To illustrate, imagine a bank account that is represented by an `Account` class. You can have many instances of this class (many unique bank accounts), each defined by the following internal state:
- owner name
- account number
- balance
```

Since the end user does not need to know all of the state associated with an object, when writing classes consider marking such state as 'private'. This prevents users from accessing attributes directly, instead accessing them through class methods (functions defined with the class).

````{admonition} Method vs Function
When talking about methods, we mean functions that are strictly 'attached' to a given class. The following example illustrates the difference between the two:

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

In some languages 'private' state can be used to prevent access to parts of your class. In Python [truly private instance variables do not exist](https://docs.python.org/3/tutorial/classes.html#private-variables), so it is not possible to prevent access to any part of your class. The standard convention in Python is to prefix attribute names with a single underscore (`_my_class_attribute`) to indicate that users shouldn't be concerned with these attributes.

In addition to private attributes, you can use the same naming convention to indicate that a method is 'private' and should not be used by users. This can be useful when writing reusable low-level methods within an object, analogous to breaking a large function down into multiple smaller functions. These private methods can then be called by high-level methods that are exposed to users.

```{caution}
In Python, the notion of 'private' does not mean secure. The main goal of private attributes and methods is to expose less unnecessary information to the anyone using your class in their code.
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


When using classes in our code, we care more about what methods a class provides than what `type` it is defined as. This is known as 'duck typing'; if a class has the same methods as another class, then you can use either class in your code.

> If it walks like a duck, and it quacks like a duck, then it must be a duck.

Given the example above, if we created a class `LoyaltyAccount` with the same `withdraw` method for withdrawing points, we could feasible switch between using the `BankAccount` and `LoyaltyAccount` classes without affecting how our code runs.

Object-Orientated Programming introduces the concept of inheritance - where a class can 'inherit' methods from another class in order to extend it. In this situation, a new class 'subclasses' the 'superclass' or 'parent' that it is inheriting from. When defining multiple classes with similar functionality, inheritance can be used to store the shared logic in a separate class type, which we can then extend by subclassing. For example, we might create an `Account` class to store a `balance` and the logic behind our `withdraw` method. Our `BankAccount` and `LoyaltyAccount` could then subclass `Account` to extend it with any additional logic that is specific to their account types.

```{note}
[Liskov substitution](https://en.wikipedia.org/wiki/Liskov_substitution_principle) states that subclasses should not damage the functionality of their parent class in their implementation.
They should extend their usefulness, but retain their original functionality. If our `BankAccount` class inherits from `Account` we should consider that 'a `BankAccount` is an `Account`'. Liskov substitution strengthens this statement to '`BankAccount` is interchangeable with an `Account`'; we can replace any `Account` with `BankAccount` without changing how our code runs. This is because `BankAccount` provides all of the same methods that an `Account` does, no less.

This can be similarly applied to functions. If you were to increase the domain and range of a function, to account for new cases, then this function should observe the same interface as the previous function.

In short:
- Objects should be replaceable with instances of their subclasses, without altering the correctness of that program.
- Functions should be replaceable with similar functions that share the same interface.

```

However, we should be wary that inheritance locks our class in to the object that it inherits from. If the superclass changes, our class is forced to change with it. When using inheritance to reuse code from an unrelated class, 'encapsulation' may be more appropriate. For example, a `Car` class might want use a method from an `Engine` class, but a car could not be substituted for an engine. It would not be suitable for `Car` to inherit from `Engine`. Therefore, you might keep a private instance of the `Engine` class you wish to re-use, and delegate the work down to it in the `Car` methods. Then, if you change your mind about using this `Engine` class in your `Car` class, you aren't tied to it and can easily replace it.

(interfaces)=

In OOP, an 'interface' can be defined to act as a blueprint or specification for writing classes. An interface outlines the attributes and methods that a class must provide to be considered equivalent to a group of classes. Perhaps we want to use classes to read and write data - this might require several different classes, with `read` and `write` methods for different file formats. For example, one class could deal with storing data in a database, and another could store data in local `.csv` files instead. In our code, we could switch which class is provided to downstream functions. Our functions don't need to know if they are reading or writing from databases or `.csv` files, however, they do require the `read` and `write` methods of the class to work in a standard way. An `interface` would help to define the standard for interacting with this group of classes.

In Python, the `abc` module allows us to define ['abstract' base classes and methods](https://docs.python.org/3/library/abc.html) to enforce that our classes provide the required methods. When a subclass does not implement the required abstract methods, instances of the class cannot be created. These abstract base classes achieve the same as interfaces in other object-based languages. We can illustrate this concept in the following example:

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

When multiple classes have a similar application programming interface (API, i.e. the methods they supply for users), we can easily switch between them. A good real-world example of this can be seen in the `scikit-learn` package, where the different linear model types are represented by different classes. Each linear model class supports a common set of methods, e.g. `fit()` and `predict()`. As such, any model can then be used in a pipeline and swapped out with minimal effort. Therefore, when thinking about how to break you code up into classes consider the use of standardised methods across similar objects to make them interchangeable.

(class-responsibilities)=

```{note}
A word of caution, when creating your own classes. It is easy to start to mapping nouns in system descriptions to classes, and any adjectives applied to the nouns as methods. For example: 'the model loads the data', which implies that `Model` is a class that should have a `load_data` method. This works well for small systems, but as the complexity of your code grows you might find that one of your classes gains the majority of the underlying logic. This often leads to one class with many methods, while other classes just store data with very few methods. This can be described as 'Data Driven Design'.

When most of your code resides in a single class, this can indicate that this class is responsible for too much of your code's logic. This class might become overly complex and hence difficult to maintain. Consequently, changes to requirements will cause this one class to change, which may affect other unrelated functionality in the class.

For more complex analytical work, a better approach might be [Responsibility Driven Design](https://en.wikipedia.org/wiki/Responsibility-driven_design). Here, we write small classes with a focussed responsibility. This reduces complexity and helps classes to avoid being affected by changes to other, unrelated parts of our code. However, be aware of the trade-off between the complexity of one large class versus many smaller classes.
```

[Responsibility Driven Design](https://en.wikipedia.org/wiki/Responsibility-driven_design) makes objects that are usually 'passive' become 'active'. For example, with a banking system, an  object representing a bank account, and handling all money movements, might become overly complex. Instead, objects representing `Cheques` and `Cash` might be designed with payment methods. In this situation, a `Cheque` knows how much money it contains and how to pay itself into an account. A `Cheque`'s responsibility is to retrieve money from its associated account and pay itself in to another bank account. If we later needed to add new payment methods, the existing payment type classes (`Cheque` and `Cash`) will unlikely to be affected. The bank account's responsibility is holding money, receiving it and paying it out. 

```{tip}
Many [Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern) are available with OOP. These are reusable solutions to common problems.
```

Finally, be wary when using classes to 'chain' methods together. For instance, if a 'book' has a 'publisher' and the publisher has an 'address', you could write `book.publisher().address().postcode()`. However, chains like this are fragile as they depend on multiple parts of the system not changing. The 'Demeter' research project found that this style of code produce a high proportion of bugs, resulting in the [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter): 'Only talk to your immediate friends'. Namely, only access the objects you know about directly within a class. This reduces the opportunity for your code to be damaged by a change in your dependencies. There is a penalty for this - you replace with `book.publisherPostcode()` which internally would call `publisher.postcode()`, so we've added a method to `publisher` as well as `book`; we're trading maintainability for complexity, so consider if it is worthwhile.

To summarise:

- Classes hide implementation detail from users, enabling implementation to be changed without affecting users.
- Look to use consistent methods in a group of related classes, so that you can switch between them without affecting the code using it. Consider Python 'duck typing' or abstract classes and methods.
- Avoid storing all logic in a single class. Instead, distribute logic based on responsibilities.
- Be aware of trading maintainability for complexity - one large class or too many classes can be hard to understand.
- Design Patterns have solutions to many common problems and are a useful toolbox.
- Prefer encapsulation over inheritance, especially with code reuse.

### Scripts

Scripts are simply files containing code that you would like to execute. In Python you commonly have a `main.py` script that orchestrates part of your codebase to achieve an outcome. In machine-learning projects, you sometimes have `train.py` and `test.py`, which are scripts that train the model and produce performance metrics.

Scripts, if written well, are reproducible. In languages like R and Python, when executed from the command line using commands like `python main.py` they are read top to bottom and executed line by line. This is in contrast to running code in an interactive interpreter or notebook, where the human has control of the order of execution. Manually executing individual lines of code allows for a slew of errors when things are run in the wrong order.

Ultimately for code pipelines you will need to have some way of running your code - the humble script is the primary way of orchestrating your functions and classes in a pipeline fashion.

<!-- The first sentence of the note below doesn't make sense to me. -->
```{note}
Using a script does not guarantee that your code will run reproducibly, but it does ensure that code is run in the same fashion across multiple runs.
```

To summarise:

- Scripts are a good way to orchestrate your functions and classes in order to build a simple, yet effective pipeline.
- They are text documents containing source code, which makes them easily human readable and auditable.
- They can be broken down into sections using [comments](code_documentation.md) for readability.

(modules)=

### Modules

Simply put, modules are scripts that contain functions that you want to use in other scripts. As you write your code and find opportunities to create classes or functions that reduce repetition and promote easier code comprehension, you might decide that you want these functions to sit outside of your main pipeline script. This is where modules come in, to separate reusable code into logical groups.

Consider a project where an analyst has created one large data analysis script. Upon reflection, they decide to split the logic from their pipeline into groups of functions relating to 'data processing', 'data modelling' and 'result presentation'. They then create a file to contain each of these groups of functions: `processing.py`, `modelling.py` and `reporting.py`. They decide that they want to have a pipeline script called `main`, but they want to keep this script readable and simple.  Their directory now looks something similar to:

```
project
| main.py
| modelling.py
| processing.py
| reporting.py
| README.md
```

They then import the relevant functions into `main.py` from their modules as follows:

```python
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

```{note}
This is a minimal example of a pipeline script, illustrating how you might import reusable functions from other modules. This `main.py` script lacks the ability to configure things like the path to the input data. This requires users to manually alter file paths in the code, which is highly discouraged.
```

````{admonition} A step further
Another step that can be taken to introduce clarity is to further wrap these modules into their own folder like so:

```
project
| library
  | __init__.py
  | modelling.py
  | processing.py
  | reporting.py
| LICENSE
| main.py
| README.md
```

And the expected python code then can be structured as follows:

```python
import pandas as pd

# Import required modules from functions
from library.modelling import predict_results
from library.processing import clean, preprocess
from library.reporting import generate_report, export

data = pd.read_csv("data/path.csv")
data = preprocess(clean(data))
results = predict_results(data)
report = generate_report(results)
export(report)
```

````

(packages)=

### Packages

Programming languages often come with quite a few in-built functions and classes that are available to the end-users. However, when it comes to solving specialised problems, these in-built functions are often not enough. In these cases, you may need to build functionality to address a given problem from scratch. If the solutions you build are useful and reusable, you can then wrap them up in a package to allow other users to install it. They can then reuse the work you have put in within their own code to solve similar problems.

In short, packages are self-contained collections of code written by someone else to solve a particular problem. For example, packages like `dplyr` and `pandas` are essential when performing data wrangling in R and Python, respectively. They contain a myriad of functions that allows us to avoid rewriting this functionality from scratch every time. Inside these packages is a set of [modules](modules) containing relevant functions, classes and other code that someone has written. These are wrapped up into a package structure so that the programming language you use can understand, install and make available the code for you to import.

```{note}
This section will not cover the practices required to package and distribute your code as a package. However if you would like to know more please look to the [code documentation section](code_documentation.md) and seek out the packaging guides for your programming language.
```

It is useful to keep in mind the question: is my code solving a problem that someone else has not already solved in my programming language? If the answer is 'Yes' then perhaps it is worth considering wrapping up your code and distributing it wider.

```{note}
Packaging code properly will involve applying many of the recommendations from this book.

You will have to consider how to test, document and lay out your code for it to be usable and packagable. In the end, high quality packages are the cornerstone of open-source package ecosystems. However, it is not trivial to maintain and develop well-regarded open-source packages.

If you feel like you are writing code that you might consider turning into a package, consult this book and strive to apply as many of the recommendations as you go. This will make the final polishing and packaging much simpler, and will produce packages that are easier for third-parties to trust and use.
```

## Notebooks

It is worth touching upon using Jupyter or other code Notebooks that allow running of your code.

Although individual notebooks could seem like a good way to modularise your analysis for distribution, for larger projects this is not always the best idea.

Notebooks are inherently difficult to review and audit through version control software like `git`. Simple text files like scripts can be version controlled easily as you can see which lines of text change from one version to another. Notebooks store their internal workings in a much more complicated format, hence seeing the changes from one notebook to another as differences line by line is not possible in common version control tools.

Furthermore, defining and keeping functions within notebooks is prohibitive to testing. It is not simple to test individual cells of a notebook with standard external tooling.

Lastly, one of the key issues with notebooks when they are used as methods for running a pipeline is the ability to run cells out of order. In practice this means that a user can accidentally execute the steps of the analysis in the wrong order causing issues and different results. As such, notebook results may not always be reproducible.

That said, great strengths of notebooks include their flexibility in displaying results while you are exploring data, and their ability to present final research code alongside a narrative. Therefore the top 2 reasons to use notebooks in the project lifecycle is to:

- explore and 'play' with the data while developing your methods.
- turn notebooks into HTML reports to present results to end users.

In short, notebooks are not suitable for modularising analysis pipelines, however, they are a great way to do research analytics and to present results. Therefore, as the exploratory part of your analysis draws to a close, or there is a need to produce similar analysis more regularly, it is wise to refactor notebooks. Reusable functions and classes can be moved to modules and the main analysis pipeline might instead be reproducibly run from a script. Here are a few suggestions to consider when refactoring code from notebooks:

- Review the repetitive cells and assess which of them can be turned into reusable functions.
- Extract existing functions into related groups, as modules.
- Document, test and improve these functions and modules following the guidance laid out in this book.
- Import the required functionality from these new modules into the notebook or pipeline script.
- For new analysis, reuse functionality from these modules in new notebooks and continue to document your analytical thinking alongside your code in these notebooks.

After this, you might turn existing notebooks into HTML to send them stakeholders, or save them as is so that analytical peers can re-run and review your notebooks. The steps that you've taken to simplify your notebook code will make your code much easier to understand by readers.

Bear in mind that notebook files can still be run out of order by other analysts, and that they should not be used as the main method of actually generating outputs. Output generation should instead be trusted to scripts, where human decisions do not alter the order that code is run.

## Clean code

```{epigraph}
Programs are meant to be read by humans and only incidentally for computers to execute.

-- Donald Knuth, The Art of Computer Programming
```

Code with high readability is often referred to as 'clean code'. Clean code helps us understand a program faster, as it avoids points of confusion and ambiguity.

The following sections will present some key aspects of writing clean code that are fairly widely applicable. That said, each individual programming language has idiomatic ways of writing code that are specific to its features. Additionally, each language usually has some form of accepted style guide.

Make sure to consult the style guides for your language as first point of call. This is an important point to stress, as these guides will capture the most up to date guidance for your language of choice, which may not be available in this document.

(naming)=

### Naming

The most important aspect of clean code is the naming of identifiers within your code. This includes variables, functions, classes and any other objects that can be assigned a name.

Someone reading your code will benefit greatly if you use names that are:

- informative and not misleading
- concise but not cryptic

(naming-variables)=

#### Naming variables

You may have previously come across code that contains variable names that are meaningless, or that imply an incorrect purpose:

````{tabs}

```{code-tab} py
import pandas as pd

x = "Sioban"

y = 42

z = pd.DataFrame()

my_favourite_number = "ssh, I'm a string"
```

```{code-tab} r R
x <- "Sioban"

y <- 42

z <- data.frame()

my_favourite_number <- "ssh, I'm a string"
```

````

Another developer, or even 'future you', would be unable to correctly interpret what these variable names to represent. Therefore, you should strive to avoid cryptic or single-letter identifiers.

That said, there are situations where some seemingly cryptic identifiers make sense. Using single letters to name variables is suitable when implementing methodologies from mathematical notation. However, even in these cases you must make sure that the formulas being implemented are clear, readily available to the reader and are consistent throughout your code. Be sure to cite the source of the mathematical formula in these cases.

In other cases, using variable names that contain a few (3 or so) informative words can drastically improve the readability of your code. How these words are separated (be it `CamelCase` or `snake_case`) will depend on your language of choice.

````{tabs}

```{code-tab} py
import pandas as pd

# Defining variables
first_name = "Sioban"

number_of_attendees = 42

empty_dataframe = pd.DataFrame()


# Using variables
print("Hi " + first_name)

number_of_attendees += 1

empty_dataframe.empty
```

```{code-tab} r R
# Defining variables
first_name <- "Sioban"

number_of_attendees <- 42

empty_dataframe <- data.frame()


# Using variables
print(paste("Hi" + first_name))

number_of_attendees <- number_of_attendees + 1

plyr::empty(empty_dataframe)
```

````

Ideally, the purpose of variables should be clear from reading their names.
In addition, the variable names should make logical sense in the context that they are used later on in the code. This removes the need for explanatory comments, as your intentions can be interpreted from the code itself ('self-documenting' code).

Naming is important for distinguishing between similar variables. A first instinct might be to assign numerical suffixes or other similar tags to differentiate variables. However, unless the suffix itself is meaningful within the context of the rest of the code, it will not make the code more understandable:

````{tabs}

```{code-tab} py
letters_1 = ["a", "b", "c"]
letters_2 = ["x", "y", "z"]
```

```{code-tab} r R
letters_1 <- c("a", "b", "c")
letters_2 <- c("x", "y", "z")
```

````

Here we can infer what these lists and vectors contain, but it is not apparent what makes `letters_1` different to `letters_2`.

Variable names can be used to document differences between variables, or to incrementally describe changes made to a variable.

````{tabs}

```{code-tab} py
letters_first_three = ["a", "b", "c"]
letters_last_three = ["x", "y", "z"]

letters_first_three_reversed = reversed(first_three_letters)
```

```{code-tab} r R
letters_first_three <- c("a", "b", "c")
letters_last_three <- c("x", "y", "z")

letters_first_three_reversed <- rev(first_three_letters)
```

````

Here the naming convention indicates that both lists are similar, but also describes the differences between them.
It is also clear how the third, new list relates to the first list that was used to create it.

With more informative names, we obviously lose the brevity of variable names:

```
letters_first_three_reversed_plus_t_minus_a_converted_to_greek
```

There is a clear trade-off between the usability and informativeness of variable names.
You'll need to use your best judgement to adapt variable names in order to keep them informative but reasonably concise.

```{note}
In languages like Python, where indentation is part of the syntax to denote code blocks, you will be much more aware of this trade-off.

In practice, the PEP8 style guide for Python recommends line widths of 79 characters and having overly descriptive names might impact your compliance with a style guide like that.
```

(naming-functions)=

#### Naming functions

Naming functions should respect the best practices already covered in the [Naming variables](naming-variables), however, there are a few other points worth raising that are exclusive to function and method names.

Firstly, your user should be able to infer the purpose or action of a function from its name. If you can't describe the overall task performed by the function in a few words, then it may be that your function is overly complex or it requires further detail in its documentation.

Where a function performs a specific task, it can be effective to describe this task in the function name, starting with a verb:

````{tabs}

```{code-tab} py
def process_text(data):
    ...

processed_text = process_text("The following document was handled using...")
```

```{code-tab} r R
process_text <- function(data) {
    ...
}

processed_text = process_text("The following document was handled using...")
```

````

This is often a tidy way to structure high-level functions in your pipeline. Well defined, verb-based names often lead to clear pipelines such as:

```python
data_path = "path/to/data"

# in short
report_data = generate_report( model( clean( load( data_path ))))

# or, more explicitly
data = load(data_path)
clean_data = clean(data)
model_results = model(clean_data)
report_data = generate_report(model_results)
```

In cases where a function responds with a Boolean (True or False) value, it is often useful to name this function in the form of a question.

````{tabs}

```{code-tab} py
def are_missing_values_present(data):
    if None in data:
        return True
    else:
        return False
```

```{code-tab} r R
are_missing_values_present <- function(data) {
  if (NA %in% data){
      TRUE
  } else {
      FALSE
  }
}
```

````

This improves the readability of code that applies these functions.

````{tabs}
```{code-tab} py
if is_clean(data):
   model(data)
```

```{code-tab} r R
if (is_clean(data)) {
    model(data)
}
```
````

#### Naming classes

Class names are usually started with a capital letter, and in `CamelCase`, as this differentiates them from `variableNames` and `variable_names`. Class names follow the same advice as for [](naming-functions) - namely, is it obvious from the class name what it does? If its too complex to name concisely, it is an indication of too many [responsibilities](class-responsibilities) and you should refactor your code into more, smaller classes.

Method names in a class closely follow the requirements for [](naming-functions), as methods are just functions that are tied to a class. They should ideally read clearly when called from a class instance - such as `bookParser = TextParser(book_data)` followed with `bookParser.getNextWord()`. Compare this against `bp = Reader(book_data)` then `bp.fetch()`, where there is not enough context.

(code-style)=

### Code style

Programming languages can differ in a myriad of ways. One way R and Python differ, for example, is their use of indentation. Indentation is part of the well defined syntax of Python while it is not for R. This does not mean that you shouldn't use indentation in R to make your code more readable. If in doubt it is often wise to consult how to use formatting to write more readable code by finding the style guidelines for your language.

Generally, code style guides provide a standard or convention for formatting and laying out your code. The purpose of these style guides is to increase consistency across the programming community for a given language.

They might include how to appropriately:

- comment or document your code
- name your functions, variables or classes
- separate elements of your code with whitespace
- use indentation to make sure your code is readable
- provide other useful guidance regarding formatting

The existence of such style guides does not necessarily mean that each individual or team will apply these conventions to the letter. Organisations and developer teams often have needs that might not be addressed in a general style guidance document. After all, these documents aim to capture the needs of a diverse group of developers. Therefore, these guides are more useful as starting points in a discussion on 'how should our team be consistent internally in the way we write code?'.

```{figure} ./_static/code_quality.png
---
width: 80%
name: code_quality
alt: Comic strip describing a brutal code review.
---
Code Quality, from [xkcd](https://xkcd.com/1513/)
```

The core idea around these guides is that individual teams have to either adopt them or adapt them for use while writing code. The goals are readability and consistency.
This consistency between developers will most likely aid speed of development and review, as well as the ability of one developer to comprehend code written by their colleagues.

```{admonition} Common Style Guides
[PEP8](https://www.python.org/dev/peps/pep-0008/) is an official Python style guide, which is widely used.
The [Google](https://google.github.io/styleguide/Rguide.html) and [tidyverse](https://style.tidyverse.org/) style guides are commonly used for R.
```

#### Idiomatic code

There is perhaps a misconception that following style guidelines and formatting your code accordingly is the fundamental goal of writing good code in a given language.

In reality, guidelines may encourage code-reviews to focus on style over more fundamental problems with the code. They have the potential to detract from assessment of whether the code is making the best use of a given language.

The notion of style goes beyond simple spacing or capitalisation. In the same way that knowing and using common idioms such as 'over the moon' or 'cold feet' make you seem like a more fluent speaker of English, a part of being fluent in a programming language is being able to write 'idiomatic' code. Idiomatic stands for 'using, containing, or denoting expressions that are natural to a native speaker'. In Python, idiomatic approaches to writing code are commonly referred to as 'pythonic'.

This might mean simplifying complex and perhaps hard to read patterns into a simpler, but well established alternative. In Python for example these two pieces of code are equivalent:

```python
# Example 1 - very unpythonic
i = 0
my_data = []
while i < 100:
  my_data += [i * i / 356]
  i += 1

# Example 2 - more use of Python features, such as `range` and `append`
my_data = []
for i in range(100):
  my_data.append(i**2 / 356)

# Example 3 - making full use pythonic idioms, `range` with list comprehension
my_data = [i**2 / 356 for i in range(100)]
```

The ability to write idiomatic code in a given language comes with time. However, it is important to think about it while looking at a given piece of code: is it using everything that language 'X' has to offer?

That said, we should still prefer readability over idioms that might make our code more complex. For example, attempting to fit too much logic into a single line of code can make it considerably harder to understand.

#### Checking code style

It is good practice to follow a style guide from the beginning of a project. However, it can be tedious to check that code continues to follow a particular style, or to fix code formatting when it doesn't. Hence, automated support can be sought to speed up this work, either by providing suggestions as the code is written or by reformatting your code to comply with some style.

Two main types of tool exist for these tasks:

- Linters - these analyse your code to flag stylistic errors (and sometimes bugs or security issues too).
- Formatters - these not only detect when you have diverged from a style, but will automatically correct the formatting of your code to conform to a particular style.

```{list-table} Packages that can be used for linting or formatting in Python and R
:header-rows: 1
:name: linters

* - Language
  - Linters
  - Formatters
* - Python
  - `flake8`, `pylint`, `Bandit`
  - `Black`, `Isort`
* - R
  - `lintr`
  - `formatR`, `styler`
```

Be sure to read the documentation for any of these tools, to understand what they are checking or changing in your code. Some can be configured to ignore or detect specific types of formatting error. You can run multiple of these, to catch a broader range of stylistic or programmatic errors.

If you're considering these tools as part of a project, see [Continuous Integration](continuous-integration) for advice on automating them. Alternatively, explore other options, such as [pre-commit](https://pre-commit.com/), that do the formatting and checking on your machine prior to a Git commit.

(software-ideas-for-analysts)=

## Software ideas for analysts

It's important to remember that when we write code for analysis, we are developing software. Over many years, software engineering teams have developed good practices for creating robust software. These practices help to make our code simple, readable and easier to maintain. Analysts using code as a means to perform analysis can benefit from at least partially applying such practices in their own codebases.

This chapter will try to condense key messages and guidelines from these practices, for use by analysts who write code. That said, reading and learning more about these practices is likely to benefit the quality of your code and is highly encouraged.

### Keep it simple

The ability to convey information in a simple and clear way matters.

This is particularly true when explaining concepts that are already complex. When writing code you are often trying to solve problems that are complex in nature. You should avoid introducing extra complexity to these problems, wherever possible. 

Here are a few tips to make sure you keep your project nice and simple:

- Solve the problem - do not get distracted and make sure you have a clear outcome in mind.
- Try not to 'reinvent the wheel' - use existing packages when they solve the problem. They will most likely be better documented and won't need extra maintenance.
- Split your code into understandable parts - consider how to [make your code modular](modular).
- Don't over-engineer your solution - if it is understandable and works, refrain from over-complicating for the sake of small increases in efficiency.


```{note}
It's important to capture the requirements of your code before writing it. This includes when your code needs to be adapted to meet changing needs. You should then aim to meet these requirements in the functionality that your code provides.

It can be tempting to try to account for every eventuality in your program, but developing anything more than these requirements may not be beneficial. There's a good chance that many cases that you account for will never occur, so you should try to prioritise based on what you're certain is needed from your code.

> You ain't gonna need it

Remember that additional features will require more documentation and testing to ensure that they are working correctly. Really consider if adding these extras will make your code more or less maintainable, user-friendly and correct. 
```

Lastly, it is worth stressing that complex problems might require complex solutions. In those cases make sure that you only introduce complexity where it is needed. You should address necessary complexity with proportionate quality assurance - through documentation, testing and review. For instance, if the execution time of your code is critical, then making the code more complex to achieve a faster runtime may be an acceptable trade-off.

### Don't repeat yourself

In the section on [modular code](modular), you were encouraged to refactor your code into more self-contained components for ease of testing, reproducibility and reusability. However, it is worth stressing that 'quick and dirty' solutions often involve copy-pasted code that is functionally identical. This is expected and is natural in the initial stages of a project. Nonetheless, repetition not only wastes your time, but it also makes your code more difficult to read.
Consider a script that contains three copies of a similar piece of code. If the code that is used to perform the repetitive task is found to be incorrect, or if a developer wishes to modify the task being performed by this code, they must implement a similar change in each of the three copies. If only two copies were spotted and amended, there is now a bug sleeping in the code waiting to be triggered... Moreover, anyone reviewing the code would need to check that the right logic is being used three times over.

To put this in context, let us use an example where the developer wants to get the odd numbers from three different lists of numbers:

````{tabs}

```{code-tab} py
first_ten_numbers = list(range(1, 11))
second_ten_numbers = list(range(10, 21))
third_ten_numbers = list(range(20, 31))

odd_first = []
for number in first_ten_numbers:
    if number % 2 == 1:
        odd_first.append(number)

odd_second = []
for number in second_ten_numbers:
    if number % 2 == 1:
        odd_second.append(number)

odd_third = []
for number in third_ten_numbers:
    if number % 2 == 0:
        odd_third.append(number)
```

```{code-tab} r R
first_ten_numbers = 1:10
second_ten_numbers = 11:20
third_ten_numbers = 21:30

odd_first <- c()
for (number in first_ten_numbers) {
  if (number %% 2 == 1) {
    odd_first <- c(odd_first, number)
  }
}


odd_second = c()
for (number in second_ten_numbers) {
  if (number %% 2 == 1) {
    odd_second <- c(odd_second, number)
  }
}

odd_third = c()
for (number in third_ten_numbers) {
  if (number %% 2 == 0) {
    odd_third <- c(odd_third, number)
  }
}
```

````

In this example, the third repeated snippet of code actually collects even numbers, but incorrectly assigns them to the `odd_third` variable. Because each copy looks very similar, you might assume that all copies of the code are performing the same task. Even when you are aware of the difference between the copies, you might be unable to tell if the difference is intentional or a mistake. The example demonstrates how repetition can add confusion when trying to maintain or review code.

Modifying multiple copies of a code snippet is laborious and presents a risk - some copies of the repeated code may be modified while others erroneously remain the same. This is analogous to modifying the formula in individual cells of a spreadsheet. If you refactor repetitive code into functions or classes, then bug fixes or modifications need only be carried out once to change all uses of that code. New, intended behaviour is then consistently given by each call of the function or method.

The following presents how one could change the previous example for the better:

````{tabs}

```{code-tab} py
def get_odd(numbers):
    """Get only the odd numbers"""
    return [number for number in numbers if number % 2 == 1]

first_ten_numbers = list(range(1, 11))
second_ten_numbers = list(range(20, 21))
third_ten_numbers = list(range(20, 21))

odd_first = get_odd(first_ten_numbers)
odd_second = get_odd(second_ten_numbers)
odd_third = get_odd(third_ten_numbers)
```

```{code-tab} r R
get_odd <- function(numbers) {
  odd_numbers = []
  for (number in first_ten_numbers) {
    if (number % 2 == 1) {
      odd_first_ten_numbers.append(number)
    }
  }
  return odd_numbers
}


first_ten_numbers = 1:10
second_ten_numbers = 11:20
third_ten_numbers = 21:30

odd_first = get_odd(first_ten_numbers)
odd_second = get_odd(second_ten_numbers)
odd_third = get_odd(third_ten_numbers)
```

````

If the functionality of `get_odd` needs to be modified, it now need only be done once. Additionally, this code is more concise and its purpose is easier to interpret.

`````{note}
If two slightly different tasks must be carried out, for example you need both the odd and the even numbers, you might approach this in one of two ways:

- Develop two functions containing the different elements of code, with names that express the difference in their purpose.
- Add a parameter to your function that will allow a user to differentiate between the two tasks.

````{tabs}

```{code-tab} py
# Simple and modular
def is_odd(number):
    """Check if a number is odd."""
    if number % 2 == 1:
        return True
    else:
        return False

def get_odd(numbers):
    """Get only the odd numbers."""
    return [number for number in numbers if is_odd(number)]

def get_even(numbers):
    """Get only the even numbers."""
    return [number for number in numbers if is_odd(number) == False]


# More concise, but also more complex - not always best
def get_numbers_with_parity(numbers, parity):
    """Get numbers with a given parity ('odd' or 'even')."""
    if parity not in ["odd", "even"]:
        raise ValueError("parity must be 'odd' or 'even'")
    remainder = 1 if parity == "odd" else 0:
    return [number for number in numbers if number % 2 == remainder]

odd_numbers = get_numbers_with_parity(list(range(1, 11), "odd"))
```

```{code-tab} r R
# Simple and modular
is_odd <- function(number) {
  if (number %% 2 == 1) {
    TRUE
  } else {
    FALSE
  }
}

get_odd <- function(numbers) {
  odd_numbers = c()
  for (number in numbers) {
    if (is_odd(number)) {
      odd_numbers = c(odd_numbers, number)
    }
  }
  return(odd_numbers)
}

get_even <- function(numbers) {
  even_numbers = c()
  for (number in numbers) {
    if (!is_odd(number)) {
      even_numbers = c(even_numbers, number)
    }
  }
  return(even_numbers)
}


# More concise, but also more complex - not always best
get_numbers_with_parity <- function(numbers, parity) {
  numbers_with_parity = c()
  if (parity == "odd") {
    remainder = 1
  } else if (parity == "even") {
    remainder = 0
  } else {
    stop("parity must be 'odd' or 'even'")
  }
  numbers[numbers %% 2 == remainder]
}
odd_numbers <- get_numbers_with_parity(1:10, "odd")
```

````

You should use your best judgement to decide which is most appropriate in a given situation.

`````

It can be difficult to decide when repetition warrants refactoring of code into reusable functions or classes. The 'Rule of Three' suggests that if similar code has been written more than two times, then it is worth extracting its logic to a reproducible procedure like a function or class. However, as you write code you should try to anticipate whether it is likely to be reused in future. If the answer is yes, you might opt to write it straight into something more modular and reusable.

### Be explicit

In the literary sense of the word!

```{epigraph}
Explicit is better than implicit

-- The Zen of Python (`import this`)
```

In some programming languages, it is possible to perform a task or decision by relying on an implied interpretation of your code.
For example, in Python `1`, `100`, `["A list of text"]` and many other objects evaluate to `True`, while `0`, `[]` and `None` evaluate to `False`.

To make your intentions clear, you should explicitly state your intended comparison in the code.

````{tabs}

```{code-tab} py
student_count = None

# Relying on falseness of None
if student_count:
    print("There are " + student_count + " students!")
```

```{code-tab} r R
student_count <- FALSE

# Relying on falseness of FALSE
if (student_count) {
  print("There are " + student_count + " students!")
}
```

````

In the example above, the student count is not printed because `None` and `FALSE` evaluate to `False`.
In Python and R, `0` will also evaluate to `False`.
Therefore, it is unclear whether the programmer intended that the statement is printed when the count is 0.
If a count of 0 should be printed, then this lack of specificity has created a bug.

To perform the same decision explicitly, we should specify the exact condition under which the student count should be printed.

````{tabs}

```{code-tab} py
student_count = 0

# Explicitly print only if more than 0
if student_count >= 0:
    print("There are " + student_count + " students!")
```

```{code-tab} r R
student_count = 0

# Explicitly only print if more than 0
if (student_count >= 0) {
  print("There are " + student_count + " students!")
}
```

````

Now the count is printed if it is more than or equal to 0.
It's clear that we intend for this to be the case.

### Separate responsibilities

> An object should have a single responsibility.
> Only changes to one part of the software's specification should be able to affect the specification of the class.

Th 'single responsibility' principle suggests that a single element of your code (a function or class) should be responsible for a single part of your software's functionality. It should take on one task and perform it well. This is because each piece of code is more robust if there are fewer reasons to change it in the future.

When you work with code that is designed to multitask, it is often difficult to modify this code without having an unintentional effect on other aspects of the software.

Imagine trying to create a model of the economy, which is a complex web of interconnected interactions. Creating 'abstractions' in the form of classes or functions that try to model multiple aspects of the economy at once might seem helpful, but when used incorrectly might instead add to the complexity.

For example, consider a class that represents a whole country (`Country`). This would represent a model that is trying to predict economic statistics for a country such as unemployment or inflation. One can imagine that this class will quickly grow into something unmanageable, as its responsibilities grow in the form of additional methods and attributes.

Based on the other chapters in this guidance, you might eventually realise that you need to break this class down further. If you had applied the idea of single responsibility, you might have broken the `Country` class down into smaller components such as `UnemploymentModel`, `InflationModel`. These classes would be responsible for doing specific modelling, while the `Country` class might only responsible for presenting the results to, lets say, a higher level economy model that tries to model cross-country trade.

This simplicity also increases usability, by minimising the number of parameters that each function or class might require.

```{note}
If you remember the [section on interfaces](interfaces), the different model classes here are a prime example where defining an interface would help you make sure each `*Model` object is interchangeable.
```

The 'separation of concerns' principle captures a similar concept to single responsibility, but on a higher level. This principle suggests that your software should be separated into distinct sections that each address a single concern.

In the previous economic modelling example, you might establish your concerns to be:

- Model economy at low level: `UnemploymentModel` and `InflationModel`.

  These are concerned with the 'low-level' details of giving estimates of economic output. They are independent of each other and concerned only by what they are trying to estimate.

- Model country level interactions and trade blocks: `Country` and `TradeBlock`.

  These parts of your code relate to higher level concepts. They will be using the lower level `Model` classes, but are primarily concerned with interactions between countries.

- Run simulations given a description of the desired economy.

  Once the model is ready, there might be a `SimulationRunner` that takes in your model of the world economy and runs simulations. In this case, this part of your codebase will only revolve around running the actual simulations.

In each of these distinct sections of your codebase there will be multiple classes and functions, which should follow the single responsibility concepts outlined earlier.

For example, within the section of your code concerned with modelling data, you might have a set of functions to download data from an external data store. These functions should only be responsible for receiving the required data safely and providing it to the `Model` object. If you had the need to download data from different sources online (i.e. Database, CSV or other), you might create several download functions. To pick the right function for each model you might create a ['LoaderFactory'](<https://en.wikipedia.org/wiki/Factory_(object-oriented_programming)>) who's only responsibility is to provide the `Model` with the right loading function for the right data source.

```{figure} ./_static/separation_of_concerns.png
---
width: 80%
name: separation_of_concerns
alt: Representation of concerns and responsibilities within a piece of software.
---
Representation of concerns and responsibilities within a piece of software
```

As such, separate sections of your software should be responsible for each of the concerns.
Within each section of your software, distinct functions or classes should be responsible for each task that is required for that section's overall functionality.

```{admonition} In the context of functions
The previous example was heavily focused on classes and Object-Oriented Programming. The same principles apply in the world of functions. You define each concern that is addressed by a module containing functions who follow the single responsibility principle.

So the previous example could equally include:
- An `unemployment_model` - function running the unemployment modelling.
- An `inflation_model` - function running the inflation modelling.

These functions would produce data about a given country, to be stored in an object. Another function might then take these data for multiple countries and start modelling it across country boundaries.

The same core concepts still fully apply.
```

### Open-closed

> Objects and functions should be open for extension, but closed for modification.

This means that it should be possible to extend the functionality of classes or functions, without modifying their source code or how they work.

```python
# some function that we want to keep closed for modification
def core_method(data):
    ...
    return result

# if we want to extend a function without modifying it, we can always do the following
def extended_methodology(data):
     core_results = core_method(data)
     return extended_functionality(core_results)

```

Same would apply with classes through ideas like inheritance.

When you think about the consequences of this, the open-closed principle gives you:

1. Confidence that essential behaviour of parts of your code should not be expected to change.
2. The ability to easily add more functionality, as your code evolves.

````{note}
In functional programming we use higher-order functions and functional composition to enact these principles. 'Functional composition' deserves a brief explanation, as a concept that might be keenly used in a data analytics pipeline.

In simple terms, functional composition is a mathematical idea that takes two functions $f$ and $g$ and produces function $h$, such that $h(x) = g(f(x))$. Analysts familiar with R's `%>%` operator will find this idea familiar.

Imagine you have a task to perform modelling and report generation from data. You can lay out your code to be easily composable with the following functions, with single responsibilities:
- `load` - loads data.
- `model` - runs the model on data.
- `report` - runs report generation.

So when it comes to creating a pipeline you end up with something like:

```python
report = report(model(load(filepath)))
```

We will now assume that these individual functions are closed for modification. However, we can extend the functionality of `load` by adding a `clean` function that cleans the data. In which case, we end up with:

```python
# We can extend this without modifying the source code of `load`
report = report(model(clean(load(filepath))))


# or we can first define a new load as follows
def new_load(filepath):
    return clean(load(filepath))

report = report(model(new_load(filepath)))


# or with the help of anonymous (lambda)
new_load = lambda data: clean(load(data))
report = report(model(new_load(filepath)))


# We can even use this to create a single function to run our defined pipeline
pipeline = lambda data: report(model(clean(load(filepath))))
report = pipeline(filepath)
```

````
